# Links 

https://www.analyticsvidhya.com/blog/2022/06/iris-flowers-classification-using-machine-learning/

https://medium.com/@kachiann/a-beginners-guide-to-machine-learning-with-python-iris-flower-prediction-61814e095268

https://www.kaggle.com/code/jchen2186/machine-learning-with-iris-dataset


rbabu@k8s-master:~/Data-Science/iris$ streamlit run iris_prediction_app.py

Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.10:8501
  External URL: http://49.205.39.142:8501

^C  Stopping...




from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Step 1: Initialize the KNN model
knn = KNeighborsClassifier(n_neighbors=3)

# Step 2: Train the model on the training data
knn.fit(X_train, y_train)

# Step 3: Use the trained model to make predictions on the test data
y_pred = knn.predict(X_test)

# Step 4: Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Step 5: Print the accuracy as a percentage
print(f'Accuracy: {accuracy * 100:.2f}%')