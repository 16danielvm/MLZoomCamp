# *Mask detection* 

## Problem Description:



### Context:



### Significance:



## Data

The data used in this project is from [Multi-Class Prediction of Cirrhosis Outcomes competition](https://www.kaggle.com/competitions/playground-series-s3e26) dataset, which can be found in [Kaggle](https://www.kaggle.com/)

Take a thorough look at the characteristics presented in the dataset, including their descriptions and the unit of measurement, if relevant.


## Exploratory Data Analysis (EDA)


## Getting Started

This is a set of instructions on setting up this project locally. To get a local copy up and running follow these simple example steps.

Prerequisites This is an example of how to list things you need to use this software.

- Python
- Pipenv
- Docker 

### Installing Dependencies

You have to install the **dependencies** with pipenv, as they are specified in the `Pipfile` and `Pipfile.lock`, by running the following commands:

```
pipenv install
pipenv shell
```

### Building the model

You have the option to execute either the `train.py` file (This file is in **final_model** folder)  to carry out all the necessary steps for training the final model used in this project. This file exports the model with the best metric (it can export several models, you have to select the model with the maximum last number in its name)

To initiate the model training, you can use the following command:

```
python train.py
```

Additionally, you can find the `final_model.ipynb` file. With this, you can convert de model exported to '.tflite' and test the model.

## Serving the model (Locally)

For the purpose of testing the model locally, an attempt was made to implement serverless to deploy this model. To do this, the `lambda_function.py` file was created, which can be tested locally as follows.

1. Open a new terminal and do the following:
        
```
python
```

```
import lambda_function
```

```
lambda_function.predict('https://raw.githubusercontent.com/16danielvm/MLZoomCamp/master/Capstone_Project_2/final_model/45.png')
```
        
- Ready!, You should get the same response as before.

2. Another way is using the `lambda_handler()` function, as follows: Open a new terminal
        
```
python
```

```
import lambda_function
```

```
event = {'url': 'https://raw.githubusercontent.com/16danielvm/MLZoomCamp/master/Capstone_Project_2/final_model/45.png'}
```

```
lambda_function.lambda_handler(event,None)
```

- Ready! Again, You should get the same response as before.

Also, you can use the model with docker:

1. **First install docker**
2. **Click and initialize the DOCKER Desltop app after intalling it**
3. **Build the docker image:**
   - *Build the docker image*
     - Open a new terminal, inside the 'Capstone_Project_2' folder and run the following command:

       ```
       docker build -t capstone-project2-model .
       ```
        
        - REMEMBER THE DOT (.) IN THE LAST COMMAND!!!This command builds a Docker image from the provided files.

    - *Run the previous image*

      ```
      docker run -it --rm -p 8080:8080 capstone-project2-model:latest
      ```
### Testing the model

Finally, you can test the model. At the same time, open another terminal, and:

```
python test_docker_locally.py
```

## Cloud Deployment

### Serverless model (You don't have to do these steps. It is just to show what i do to implement serverless, check the last section)

For the serverless implementation after creating the Docker image, follow these steps:

1. Lambda Function Creation:

   1.1. Publish Docker Image to AWS ECR:

   - Create an AWS ECR (Elastic Container Registry) to store the image.
   - Set up an IAM user with keys for authentication.
   - Create a policy to grant permissions for ECR creation. (If you want to know which permission policy you need, check out this [tweet](https://twitter.com/16danielvm/status/1728486982861693336/photo/1) that I posted)
   - Publish the image to ECR using AWS CLI.

   1.2. Create Lambda Function:

   - Through AWS Lambda, create a new function using the previously created Docker container image.

3. API Gateway: Testing the Lambda Function:

   2.1. Create and Configure API Gateway:
   - Using API Gateway in AWS, create a new REST API and give it a name.
   - Create a resource named "predict" and a POST method to integrate with the Lambda function.
   - Perform console tests by providing input data. For example:

     {"url" = "https://raw.githubusercontent.com/16danielvm/MLZoomCamp/master/Capstone_Project_2/final_model/45.png"}
   - Implement the API and create a new stage for testing.

### Testing the model serverless (If you want test the Serverless, do this)

Open a new terminal and execute the `testServerless.py` file:
```
python testServerless.py
```
Finally, you will have the mask detection.

## Citation 

1. Walter Reade, Ashley Chow. (2023). Multi-Class Prediction of Cirrhosis Outcomes. Kaggle. https://kaggle.com/competitions/playground-series-s3e26
