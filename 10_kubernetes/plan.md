# 10. Kubernets and Tensorflow Serving

Wee'll deploy de clothers classification model we trained previously using Kubernetes and Tensorflow Serving

## 10.1 Overview

* What we'll cover this week
* Two-tier architecture

## 10.2 Tensorflow serving

* The saved_model format
    * Descargar el modelo en .h5
    * En cmd:
        * python:
            * import tensorflow as tf
            * from tensorflow import keras
            * model = keras.model.load_model('./nombredelmodelo.h5')
            * model
            * tf.saved_model.save(model,'nombrenuevo') -> creara una carpeta con el nombrenuevo   
        * saved_model_cli show --dir clothing-model --all
        * Copiar y pegar: 
            *   signature_def['serving_default']:
                The given SavedModel SignatureDef contains the following input(s):
                    inputs['input_16'] tensor_info:
                        dtype: DT_FLOAT
                        shape: (-1, 299, 299, 3)
                        name: serving_default_input_16:0
                The given SavedModel SignatureDef contains the following output(s):
                    outputs['dense_13'] tensor_info:
                        dtype: DT_FLOAT
                        shape: (-1, 10)
                        name: StatefulPartitionedCall:0
                Method name is: tensorflow/serving/predict
        * Crear model_description.txt:
            *   serving_default
                input_16 - input
                dense_13 - output
* Running TF-Serving locally with Docker
    * Correr en cmd: 
        * docker run -it --rm -p 8500:8500 -v "$(pwd)/clothing-model:/models/clothing-model/1" -e MODEL_NAME="clothing-model" tensorflow/serving:2.7.0 
        * OJO pwd se refiere a el path absoluto, no el path relativo va desde C:/blablabla/blabla/...
* Invoking the model from jupyter
    * Crear tf-serving-connect.ipynb

## 10.3 Creating a pre-processing service

* Converting the notebook to a Python Script
    * crear gateway-sinflask.py

* Wrapping the script into a Flask app
    * crear gateway.py
    * crear test.py

* Para probarlo es necesario 3 terminales:
    * Primer cmd: ejecutas la linea de comando de docker (Correr tensorflow serving)
    * Segundo cmd: Correr gateway.py
    * Tercer cmd: Correr test.py

* Putting everythinh into a Pipenv
    * Crar un Pipenv # SI ES CON python 3.10:
        * pipenv install grpcio==1.42.0 flask waitress keras-image-helper
        * pipenv install tensorflow-protobuf==2.7.0
        * pipenv install protobuf==3.20.1
        
        * # SI ES CON PYTHON 3.9
            * pipenv install --python 3.9.13 requests grpcio==1.42.0 flask gunicorn keras-image-helper tensorflow-protobuf==2.7.0 protobuf==3.19.6

    * Crear proto.py y copiamos el codigo de : https://github.com/alexeygrigorev/tensorflow-protobuf
    * Modificar gateway.py
    * Ejecutar el pipenv en cmd CON EL PYTHON QUE SE USO:
        * pipenv shell
        * python gateway.py
    * Modificar gateway.py (descomentar/comentar solo lo ultimo)


## 10.4 Running everything locally with Docker-compose

* Preparing th images
    * Crear image-model.dockerfile
    * en cmd: 
        * docker build -t zoomcamp-10-model:xception-v4-001 -f image-model.dockerfile .
        * docker run -it --rm -p 8500:8500 zoomcamp-10-model:xception-v4-001
    * Crear image-gateway.dockerfile
    * en cmd: 
        * docker build -t zoomcamp-10-gateway:001 -f image-gateway.dockerfile .
        * docker run -it --rm -p 9696:9696 zoomcamp-10-gateway:001
* Installing docker-compose
    * crear docker-compose.yaml
    * modificar gateway.py
    * En cmd:
        * docker build -t zoomcamp-10-gateway:002 -f image-gateway.dockerfile .
    
* Running the service
    * En cmd:
        * docker-compose up
* Testing the service
    * En cmd:
        * python test.py

* EXTRA:
    * docker-compose -d = hace que en segundo plano se ejecute el dockercompose y seguir en el mismo terminal
    * docker-compose down = acaba con todo

## 10.5 Introduction to Kubernetes

* The anatomy of a kubernetes

## 10.6 Depoying a simple service to Kubernetes

* Installing kubectl
    * kubectl ya viene instalado por docker desktop
* Setting up a local Kubernetes cluster with kind
    * En cmd: wget "https://kind.sigs.k8s.io/dl/v0.20.0/kind-windows-amd64" -O kind-windows-amd64.exe
    * en cmd: Move-Item kind-windows-amd64.exe C:/kind/kind.exe
    * Para este caso y poder ejecutar kind... C:/kind/kind.exe create cluster
    * kubectl cluster-info --context kind-kind
* Creating a deployment
    * crear deployment.yaml
    * en cmd: kubectl apply -f deployment.yaml
    * en cmd: kubectl get deployment
    * en cmd: kubectl get pod 
    * en cmd: kubectl describe pod <NOMBRE DEL POD>
    * en cmd: kind load docker-image ping:v001
    * en cmd: kubectl get pod 
    * en cmd: kubectl port-forward <nombre del pod> 9696:9696
* Creating a service
    * crear service.yaml
    * en cmd: kubectl apply -f service.yaml
    * en cmd: kubectl get service
    * en cmd: kubectl get svc
    * Se modificó service agregando type: LoadBalancer
    * en cmd: kubectl apply -f service.yaml
    * en cmd: kubectl get svc
    * en cmd: kubectl port-forward service/ping 8080:80

* PARA BORRAR
    * EN CMD: kubectl delete -f deployment.yaml
## 10.7 Deploying TensowFlow models to kubernetes

* Deploying the TF-Serving model
    * crear model-deployment.yaml
    * en cmd: kubectl apply -f deployment.yaml
    * en cmd: kubectl get pod
    * en cmd: kubectl describe pod <NOMBRE DEL POD>
    * en cmd: kubectl port-forward <NOMBRE DEL POD> 8500:8500
    * PARA PROBAR:
        * En otro cmd: python gateway.py despues de comentar la ultima linea y descomentar las 3 anteriores
    
    * crear model-service.yaml
    * en cmd: kubectl apply -f model-service.yaml
    * en cmd: kubectl get service
    * en cmd: kubectl port-forward service/<nombre del servicio> 8500:8500
    * PARA PROBAR:
        * En otro cmd: python gateway.py despues de comentar la ultima linea y descomentar las 3 anteriores

    * crear gateway-deployment.yaml
    * en cmd: C:/kind/kind.exe load docker-image zoomcamp-10-gateway:002
    * Seguir modificando gateway-deployment.yaml:
        * se agrega: 
                    env:
                    - name: TF-SERVING-HOSt
                    value: tf-serving-clothing-model.default.svc.cluster.local:8500
    * en cmd: kubectl apply -f gateway-deployment.yaml
    * en cmd: kubectl get pod
    * en cmd: kubectl port-forward <NOMBRE DEL POD> 9696:9696

    * crear gateway-service.yaml
    * en cmd: kubectl apply -f gateway-service.yaml
    * en cmd: kubectl get service
    * en cmd: kubectl port-forward service/<nombre del servicio> 8500:8500
* Deploying the Gateway
* Testing the service

## 10.8 Deployinh to EKS

* Creating a EKS cluster on AWS
* Publishing the image to ECR
* Configure kubectl




