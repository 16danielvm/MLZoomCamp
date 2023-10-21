
# *Heart Attack Risk Analysis* 

## Problem Description

This project originates from a Kaggle competition with a crucial objective: predicting the risk of a patient experiencing a heart attack. Cardiovascular health is a global concern, and the ability to anticipate potential cardiovascular events can be a determining factor for early medical intervention and prevention.

### Context 

The dataset encompasses a wide range of features pertinent to heart health and lifestyle choices, covering patient-specific details such as age, gender, cholesterol levels, blood pressure, heart rate, and factors like diabetes, family history, smoking habits, obesity, and alcohol consumption. Additionally, it includes lifestyle elements such as exercise hours, dietary patterns, stress levels, and sedentary hours. Medical aspects, including prior heart issues, medication usage, and triglyceride levels, are taken into account. Socioeconomic factors like income and geographical attributes such as country, continent, and hemisphere are also integrated.

### Significance

Early prediction of cardiovascular risk can be crucial for informed medical decision-making. If this model can identify significant patterns and correlations in the data, it could become a valuable tool for healthcare professionals. Furthermore, the ability to efficiently perform risk assessments could enhance resource allocation and personalized care for patients.


## Data

The data used in this project is the [Heart Attack Risk Analysis competition](https://kaggle.com/competitions/heart-attack-risk-analysis) dataset, which can be found in [Kaggle](https://www.kaggle.com/).

Take a thorough look at the characteristics presented in the dataset, including their descriptions and the unit of measurement, if relevant.

| Feature Name | Feature Description |
| :----------: | :-----------------: |
| Patient ID   | Unique identifier for each patient |
| Age          | Age of the patient  |
| Sex | Gender of the patient (Male/Female) |
| Cholesterol | Cholesterol levels of the patient |
| Blood Pressure | Blood pressure of the patient (systolic/diastolic) |
| Heart Rate | Heart rate of the patient |
| Diabetes | Whether the patient has diabetes (Yes/No) |
| Family History | Family History of the heart-related problems (1: Yes, 0: No) |
| Smoking | Smoking status of the patient (1: Smoker, 0: Non-smoker) |
| Obesity | Obesity status of the patient (1: Obese, 0: Not obese) |
| Alcohol Consumption | Level of alcohol consumption by the patient (None/Light/Moderate/Heavy) |
| Exercise Hours Per Week | Number of exercise hours per week |
| Diet | Dietary habits of the patient (Healthy/Average/Unhealthy) |
| Previous Heart Problems | Previous heart problems of the patient (1: yes, 0: No) |
| Medication Use | Medication usage by the patient (1: Yes, 0: No) |
| Stress Level | Stress level reported by the patient (1-10) |
| Sedentary Hours Per Day | Hours of sedentary activity per day|
| Income | Income level of the patient | 
| BMI | Body Mass Index (BMI) of the patient | 
| Triglycerides | Triglyceride levels of the patient |
| Physical Activity Days Per Week | Days of physical activity per week | 
| Sleep Hours Per Day | Hourse of sleed day | 
| Country | Country of the patient | 
| Continent | Continent where the patient resides | 
| Hemisphere | Hemisphere where the patient resides | 
| Heart Attack Risk | Presence of heart attack risk (1: Yes, 0: No) |

## Getting Started

This is a set of instructions on setting up this project locally. To get a local copy up and running follow these simple example steps.

Prerequisites This is an example of how to list things you need to use this software.

- Python
- Pipenv
- Docker 

### Installing Dependencies

Youc can install the dependencies with pipenv, as they are specified in the 'Pipfile' and 'Pipfile.lock', by running the following commands:

'''
pipenv install
pipenv shell
'''