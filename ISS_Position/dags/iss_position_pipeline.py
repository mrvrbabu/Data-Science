# Import libraries 

from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago
from airflow.decorators import task
import requests
import json



# Define the variables 
#LATITUDE = 37.7749
# LONGITUDE = -122.4194

POSTGRES_CONN_ID = 'iss_postgres'
API_CONN_ID = 'iss_api'

# Define the DAG

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1)
}

## DAG 
with DAG(dag_id = 'iss_position',
         default_args=default_args,
         schedule_interval='@hourly',
         catchup=False) as dag:


    @task()
    def extract_jason_data():
        """Extract data from the API and return the JSON response."""
        
        # Use the HttpHook to make a GET the ISS live position with connection details from Airflow connections 
        http_hook = HttpHook(method='GET', http_conn_id=API_CONN_ID)
        
        # Build the API endpoint
        # http://api.open-notify.org
        endpoint = f'/iss-now.json'
        
        
        ## Make the request via the HttpHook
        response = http_hook.run(endpoint)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")
        
        
    
    @task()
    def transform_iss_data(iss_data):
        """Transform the ISS data to extract latitude and longitude."""
        
        # Extract latitude and longitude from the JSON response
        current_position = iss_data['iss_position']
        transformed_iss_data = {
            'latitude': current_position['latitude'],
            'longitude': current_position['longitude'],
            'timestamp': iss_data['timestamp']
        }

        return transformed_iss_data
    
    @task()
    def load_iss_data(transformed_iss_data):
        """Load the transformed ISS data into PostgreSQL."""
        
        pg_hook = PostgresHook(postgres_conn_id = POSTGRES_CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()
        
        # Create table if it doesn't exist
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS iss (
            id SERIAL PRIMARY KEY,
            latitude FLOAT NOT NULL,
            longitude FLOAT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        # Insert the transformed data into the table
        cursor.execute("""
        INSERT INTO iss (latitude, longitude)
        VALUES (%s, %s);
        """, (transformed_iss_data['latitude'], 
              transformed_iss_data['longitude']))
        
        conn.commit()
        cursor.close()
        conn.close()
        
    # Define the task dependencies
    iss_data = extract_jason_data()
    transformed_iss_data = transform_iss_data(iss_data)
    load_iss_data(transformed_iss_data)
                
