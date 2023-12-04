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
* Wrapping the script into a Flask app

## 10.4 Running everything locally with Docker-compose

* Preparing th images
* Instralling docker-compose
* Running the service
* Testing the service

## 10.5 Introduction to Kubernetes

* The anatomy of a kubernetes

## 10.6 Depoying a simple service to Kubernetes

* Installing kubectl
* Setting up a local Kubernetes cluster with kind
* Creating a deployment
* Creating a service

## 10.7 Deploying TensowFlow models to kubernetes

* Deploying the TF-Serving model
* Deploying the Gateway
* Testing the service

## 10.8 Deployinh to EKS

* Creating a EKS cluster on AWS
* Publishing the image to ECR
* Configure kubectl




