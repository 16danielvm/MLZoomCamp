# 9. Serverless Deep Learning

We'll deploy the clothes classification model we trained previously

## 9.1. Introduction to serverless

* What we'll cover this week

## 9.2. AWS Lambda

* Intro to AWS Lambda
    * Search Lambda
    * Crear desde cero / Author from scratch
    * Nombre de la funcion / Function name
    * Seleccionar the environment / Runtime -> Python 3.10
    * Arquitectura / Architecture -> x86_64
    * Crear la funcion / Create de function

* Look the code of lambda function 
    import json

    def lambda_handler(event, context):
        print("parameters:", event)
        # TODO implement
        return "PONG"

    * Click Test
    * Configure test event
        * Event name -> test
        * Create or Save
    
    * Click test again
    * Now change the code of lambda function
        import json

        def lambda_handler(event, context):
            print("parameters:", event)
            url = event['url]
            results = predict(url)
            return results
    * Click deploy and then test
    * Configure the event:
            {
                "url": "some-url-of-pant"
            }

* Serverless vs serverfull
* ELIMINATE!!!

## 9.3. TensorFlow Lite

* Why not TensorFlow
    * TF is so large library / Instead use a light library (TF-Lite)
* Converting de model
* Using the TF-Lite model for making predictions

## 9.4. Preparing the Lambda code

* Moving the code from notebook to script
    * lambda_function.py without lambda_handler()
* Testing it locally
    * cmd: python
        * import lambda_function
        * lambda_function.predict('http://bit.ly/mlbookcamp-pants')
        * Ready!!
* Agg lambda_handler()
* Testing it locally
    * cmd: python
        * import lambda_function
        * event = {'url': 'http://bit.ly/mlbookcamp-pants'}
        * lambda_function.lambda_handler(event, None)
        * Ready!!

## 9.5. Preparing a Docker image

* Lambda base images
* Preparing the docker file
    * create docker file
    * build the image: docker build -t clothing-model .
    * test: docker run -it --rm -p 8080:8080 clothing-model:latest
* Create test.py
* Using the right TF-Lite wheel

## 9.6. Creating the lambda function

* Publishin the image to AWS ECR
    * Crear un ECR... primero hay que crear un usuario IAM con las keys y aws configura
    * Crear una politica para darle el permiso de crear ECR
    * En cmd: aws ecr create-repository --repository-name clothing-tflite-images
    * Buscar en AWS: ECR que se haya creado
    * Ahora la idea es ingresar al ECR:
        * En un powershell: aws ecr get-login-password --region us-east-2 | ForEach-Object { docker login -u AWS -p $_ 
393556504128.dkr.ecr.us-east-2.amazonaws.com/clothing-tflite-images } 
        * Ahora grabamos la imagen en el ecr creado:  
            * docker tag clothing-model:latest 393556504128.dkr.ecr.us-east-2.amazonaws.com/clothing-tflite-images 
            * docker push 393556504128.dkr.ecr.us-east-2.amazonaws.com/clothing-tflite-images 
* Creating the function
    * Ir a lambda en AWS crear una funcion
    * Darle nombre
    * Seleccionar la imagen ya creada!!!
* Configuring it
* Testing the function from the AWS Console
    * Probar 
    {
        "url": "http://bit.ly/mlbookcamp-pants"
    }
    * Configuration -> dar 1024 de CPU y hasta 30 segundos
    * LISTO!
* Pricing

## 9.7. API Gateway: exposing the lambda functtion

* Creating and configuring the gateway

    * Buscar API gateway en AWS
        * Crear API
        * REST API : Crear
            * nombrar la API : "clothes-classification" 
            * Click Crear recurso
                * nombre del recurso: predict
                * Crear
            * Click Crear metodo:
                * Tipo de metodo: POST
                * Tipo de integracion: Lambda Function
                * Lambda Region : la que se necesita donde esta todo
                * Seleccion la funcion lambda que ya se creó
                * Crear
            * Testearla:
                * Buscar pestaña "pruebas"
                    * En el apartado de codigo: {"url": "http://bit.ly/mlbookcamp-pants"}
            * Implementar la API:
                * Click en "Implementar API"
                * "New stage"
                * Name:  test
                * click Implementar
        * Cambiar test.py
            * Agregar url = 'https://x6pd0gia6i.execute-api.us-east-2.amazonaws.com/test/predict'