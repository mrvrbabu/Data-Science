FROM python:3.10-slim-bullseye
LABEL maintainer="mrvrbabu"
LABEL description="MLflow is an open-source platform for managing the ML lifecycle, including experimentation, reproducibility, and deployment."
LABEL version="1.0"
ENV TZ="ASIA/Kolkata"
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV GIT_PYTHON_REFRESH=quiet
ENV LC_CTYPE C.UTF-8


RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  

COPY requirements.txt . 

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# CMD ["python3", "-m", "mlflow", "run", "--host=0.0.0.0", "--port=5000", "--backend-store-uri=sqlite:///mlflow.db", "--default-artifact-root=./artifacts"]
CMD ["mlflow", "server", "-h", "0.0.0.0"]
EXPOSE 5000


# mlflow run --host=192.168.0.10