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

## 9.3. TensorFlow Lite

* Why not TensorFlow
    * TF is so large library / Instead use a light library (TF-Lite)
* Converting de model
* Using the TF-Lite model for making predictions

## 9.4. Preparing the Lambda code

* Moving the code from notebook to script
* Testing it locally

## 9.5. Preparing a Docker image

* Lambda base images
* Preparing the docker file
* Using the right TF-Lite wheel

## 9.6. Creating the lambda function

* Publishin the image to AWS ECR
* Creating the function
* Configuring it
* Testing the function from the AWS Console
* Pricing

## 9.7. API Gateway: exposing the lambda functtion

* Creating and configuring the gateway