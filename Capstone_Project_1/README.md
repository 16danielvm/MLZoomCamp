# *Multi-Class Prediction of Cirrhosis Outcomes* 

## Problem Description:

The problem addresses the multi-class prediction of outcomes related to cirrhosis. Cirrhosis is a chronic medical condition characterized by damage and scarring of the liver tissue. This model aims to forecast different categories of outcomes associated with cirrhosis, which could include various severity levels, disease stages, or specific outcomes.

### Context:

In the medical field, the ability to foresee cirrhosis outcomes is crucial for clinical decision-making. A multi-class model would provide a more detailed and specific insight compared to binary approaches, as it can distinguish between various manifestations and degrees of liver disease progression. This could be especially valuable for personalizing treatments, allocating medical resources more efficiently, and improving the quality of life for patients with cirrhosis.

### Significance:

The significance of this problem lies in its potential impact on personalized healthcare and the enhancement of outcomes for patients with cirrhosis. By anticipating and classifying diverse outcomes, healthcare professionals can tailor treatment strategies, interventions, and follow-ups to address the specific needs of each patient. Furthermore, an accurate model can contribute to more effective management of medical resources and early identification of high-risk cases, significantly improving clinical outcomes and the efficiency of the healthcare system.

## Data

The data used in this project is from [Multi-Class Prediction of Cirrhosis Outcomes competition](https://www.kaggle.com/competitions/playground-series-s3e26) dataset, which can be found in [Kaggle](https://www.kaggle.com/)

Take a thorough look at the characteristics presented in the dataset, including their descriptions and the unit of measurement, if relevant.

| Variable       | Description                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------------------|
| id             | A unique identifier for each patient.                                                                         |
| N_Days         | Number of days elapsed from a reference point.                                                                 |
| Drug           | The type of medication administered or used in treatment.                                                      |
| Age            | The age of the patient in years.                                                                               |
| Sex            | The gender of the patient.                                                                                    |
| Ascites        | Presence or absence of ascites, an abnormal accumulation of fluid in the abdominal cavity.                      |
| Hepatomegaly   | Indicates whether there is hepatomegaly, which is the enlargement of the liver.                                |
| Spiders        | Presence or absence of "spiders" (vascular lesions), which are skin lesions associated with liver diseases.    |
| Edema          | Presence or absence of edema, the accumulation of fluid in tissues.                                             |
| Bilirubin      | Levels of bilirubin in the blood.                                                                             |
| Cholesterol    | Levels of cholesterol in the blood.                                                                          |
| Albumin        | Levels of albumin in the blood.                                                                              |
| Copper         | Levels of copper in the body.                                                                               |
| Alk_Phos       | Levels of alkaline phosphatase in the blood.                                                                 |
| SGOT           | Levels of the enzyme aspartate aminotransferase (SGOT or AST) in the blood, an indicator of liver damage.      |
| Tryglicerides  | Levels of triglycerides in the blood.                                                                        |
| Platelets      | Quantity of platelets in the blood.                                                                          |
| Prothrombin    | Prothrombin time.                                                                                           |
| Stage          | The stage of the disease or medical condition of the patient.                                                 |
| Status         | The status of the patient, with values 'C' (Compensated), 'D' (Decompensated), or 'CL' (Controlled).          |                     |

## Exploratory Data Analysis (EDA)

In the project development, I chose to use the `ydata-profiling` library for exploratory data analysis (EDA). This tool provide a detailed and understandable view of the structure and characteristics of the involved datasets.

`ydata-profiling` stands out for its ability to generate comprehensive reports covering various aspects of the data. From value distribution to key statistics, the library offers a complete overview that facilitates the identification of patterns, anomalies, and trends in the data. Moreover, its capability to highlight null values, provide clear visualizations, and summarize descriptive statistics significantly contributes to streamlining the analysis process.

In eda folder, you can find the notebook_eda file where I showed how implement the `ydata-profiling`, the **insights** that i found with it, the **data preparation**, implementing of **feature selection**, **deployment of several algorithms**, and the **selection of final model**. Also, you can see the eda_report exported in html file for a better view of the report and the **standarizing features** file.

## Getting Started

This is a set of instructions on setting up this project locally. To get a local copy up and running follow these simple example steps.

Prerequisites This is an example of how to list things you need to use this software.

- Python
- Pipenv
- Docker 

### Installing Dependencies

You have to install the **dependencies** with pipenv (because the version of model XgBoost that i used on this project has to be the same), as they are specified in the `Pipfile` and `Pipfile.lock`, by running the following commands:

```
pipenv install
pipenv shell
```

### Building the model

You have the option to execute either the `train.py` file (This file is in **final_model** folder)  to carry out all the necessary steps for training the final model used in this project.

To initiate the model training, you can use the following command:

```
python train.py
```

## Serving the model (Locally)

For the purpose of testing the model locally, two files were created (`predict_test.py`, `predict.py`), which serve to load and execute the model, and similarly, submit new input for prediction.

To testing the model:
    
1. Open a new terminal and run the `predict.py` file:
        
```
python predict.py

```
2. At the same time, open another new terminal and run the `predict_test.py` file:
        
```
python predict_test.py
```

3. Now, you can see the response for the new data. It must be: `{'status': 0} Your Cirrhosis status is C`.


Similarly, an attempt was made to implement serverless to deploy this model. To do this, the `lambda_function.py` file was created, which can be tested locally as follows.

1. Open a new terminal and do the following:
        
```
python
```

```
import lambda_function
```

```
lambda_function.predict({
                            "Bilirubin": -0.707522,
                            "Copper": 0.799566,
                            "N_Days": -0.261788,
                            "Stage": 2,
                            "Hepatomegaly": 0,
                            "Prothrombin": -1.224804,
                            "SGOT": -0.913350,
                            "Edema": 0,
                            "Platelets": 0.568196,
                            "Age": 1.336986,
                            "Cholesterol": -1.178809,
                            "Drug": 1
                        })
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
event =   {'customer' : {
                            "Bilirubin": -0.707522,
                            "Copper": 0.799566,
                            "N_Days": -0.261788,
                            "Stage": 2,
                            "Hepatomegaly": 0,
                            "Prothrombin": -1.224804,
                            "SGOT": -0.913350,
                            "Edema": 0,
                            "Platelets": 0.568196,
                            "Age": 1.336986,
                            "Cholesterol": -1.178809,
                            "Drug": 1
                        }
            }
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
     - Open a new terminal, enter the 'Capstone_Project_1' folder and run the following command:

       ```
       docker build -t capstone-project .
       ```
        
        - REMEMBER THE DOT (.) IN THE LAST COMMAND!!!This command builds a Docker image from the provided files.

    - *Run the previous image*

      ```
      docker run -it --rm -p 8080:8080 capstone-project:latest
      ```
### Testing the model

Finally, you can test the model. At the same time, open another terminal, and:

```
python test.py
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

     {"customer" : {
                "Bilirubin": -0.707522,
                "Copper": 0.799566,
                "N_Days": -0.261788,
                "Stage": 2,
                "Hepatomegaly": 0,
                "Prothrombin": -1.224804,
                "SGOT": -0.913350,
                "Edema": 0,
                "Platelets": 0.568196,
                "Age": 1.336986,
                "Cholesterol": -1.178809,
                "Drug": 1
            }}
   - Implement the API and create a new stage for testing.

### Testing the model serverless (If you want test the Serverless, do this)

Open a new terminal and execute the `testServerless.py` file:
```
python testServerless.py
```
Finally, you will have the classification of the patient's Cirrhosis level.

## Citation 

1. Walter Reade, Ashley Chow. (2023). Multi-Class Prediction of Cirrhosis Outcomes. Kaggle. https://kaggle.com/competitions/playground-series-s3e26
