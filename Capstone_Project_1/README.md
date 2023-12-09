# *Multi-Class Prediction of Cirrhosis Outcomes* 

## Problem Description:

The problem addresses the multi-class prediction of outcomes related to cirrhosis. Cirrhosis is a chronic medical condition characterized by damage and scarring of the liver tissue. This model aims to forecast different categories of outcomes associated with cirrhosis, which could include various severity levels, disease stages, or specific outcomes.

## Context:

In the medical field, the ability to foresee cirrhosis outcomes is crucial for clinical decision-making. A multi-class model would provide a more detailed and specific insight compared to binary approaches, as it can distinguish between various manifestations and degrees of liver disease progression. This could be especially valuable for personalizing treatments, allocating medical resources more efficiently, and improving the quality of life for patients with cirrhosis.

## Significance:

The significance of this problem lies in its potential impact on personalized healthcare and the enhancement of outcomes for patients with cirrhosis. By anticipating and classifying diverse outcomes, healthcare professionals can tailor treatment strategies, interventions, and follow-ups to address the specific needs of each patient. Furthermore, an accurate model can contribute to more effective management of medical resources and early identification of high-risk cases, significantly improving clinical outcomes and the efficiency of the healthcare system.

## Data

The data used in this project is from [Multi-Class Prediction of Cirrhosis Outcomes competition](https://www.kaggle.com/competitions/playground-series-s3e26) dataset, which can be found in [Kaggle](https://www.kaggle.com/)

Take a thorough look at the characteristics presented in the dataset, including their descriptions and the unit of measurement, if relevant.

| Feature       |Description                                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------------|
| id            | A unique identifier for each entry in the dataset.                                                               |
| N_Days        | Number of days elapsed since some reference point or significant event. It could be an indicator of the duration of follow-up. |
| Drug          | The type of medication administered or used in treatment.                                                          |
| Age           | The patient's age in years.                                                                                      |
| Sex           | The patient's gender, typically represented as male (M) or female (F).                                           |
| Ascites       | Presence or absence of ascites, an abnormal accumulation of fluid in the abdominal cavity.                         |
| Hepatomegaly  | Indicates whether there is hepatomegaly, which is the enlargement of the liver.                                   |
| Spiders       | Presence or absence of "spiders" (vascular lesions), which are skin lesions associated with liver diseases.       |
| Edema         | Presence or absence of edema, the accumulation of fluid in tissues.                                                |
| Bilirubin     | Levels of bilirubin in the blood, a yellow pigment produced during the breakdown of red blood cells.               |
| Cholesterol   | Levels of cholesterol in the blood.                                                                              |
| Albumin       | Levels of albumin in the blood, a protein produced by the liver.                                                  |
| Copper        | Levels of copper in the body.                                                                                    |
| Alk_Phos      | Levels of alkaline phosphatase in the blood, an enzyme produced mainly by the liver and bones.                     |
| SGOT          | Levels of the enzyme aspartate aminotransferase (SGOT or AST) in the blood, which can be an indicator of liver damage. |
| Triglycerides | Levels of triglycerides in the blood, a type of fat.                                                               |
| Platelets     | Quantity of platelets in the blood, important for clotting.                                                        |
| Prothrombin   | Prothrombin time, an indicator of blood clotting ability.                                                          |
| Stage         | The stage of the disease or medical condition of the patient.                                                      |
| Status        | The patient's status, indicating whether they have experienced certain outcomes or events.                        |