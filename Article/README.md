# Balancing the Game: Undersampling and Oversampling

![UNBALANCED](/Article/images/unbalance.jpg)

## INTRODUCTION

Imagine that you are implementing machine learning to create a classification model, and you realize that one of the classes in the target variable predominates significantly over the other class by a considerably higher percentage: this is known as data imbalance or the imbalanced data problem, where the number of instances in the categories of the target variable is not distributed evenly. This issue can have a significant impact on the model's ability to generalize and accurately classify the minority class. The model may lean towards predicting the majority class, ignoring the other classes, resulting in poor model performance. Therefore, it is crucial to apply different strategies to ensure that the model effectively learns from all classes of the target variable and can classify accurately in real-world situations.

This time, we aim to address the problem by applying data balancing techniques, specifically: undersampling and oversampling.

### UNDERSAMPLING

The main objective of this technique is to balance the data by randomly removing instances from the majority class, in order to equalize the number of instances in the minority class and thus achieve an equitable distribution for both classes.

This type of technique helps reduce data storage and code execution time, as the amount of data will be much smaller. On the other hand, if the amount of data is not high enough, the dataset will be so reduced that, when implementing a classification model, it will likely exhibit underfitting as it won't have enough data to produce a good result from the trained model.

### OVERSAMPLING

Similarly, this technique aims to balance the classes of the target variable. Its main difference is that it seeks to randomly replicate instances of the minority class to equalize the number of instances in the majority class. In other words, it creates "new" instances that are copies of the existing ones from the minority class so that the distribution of the classes becomes equitable.

The major advantage of this technique is that there is no loss of information since, instead of removing records, "new" ones are created. This results in the dataset having more records for training the model. However, the act of replicating data means that our model has repeated data in its training, which can lead to overfitting. Since the data is identical, the model may not generalize well to new data, failing to learn how to classify them optimally.

## IMPLEMENTATION

For the implementation of the different data balancing techniques, the breast cancer dataset will be used. This dataset consists of 31 columns and 310 instances. In this case, the target variable has two classes, '0' and '1', representing patients without cancer and patients with cancer.

![imagen 1](/Article/images/1_Librerias.png)

![imagen 2](/Article/images/Imagen2_cargardatos.png)

![imagen 3](/Article/images/Imagen3_desbalancedatos.png)

![imagen 4](/Article/images/Imagen4_barplot.png)

The 310 records are divided between '0' and '1' with 290 and 20 records respectively, representing 94% and 6% of the data for each class, which can be considered as data imbalance.

The previous code cell is performing a partition of the 'df' dataframe based on the values in the column at position 30 (target variable). The logic of this code is as follows:

- cancer = df[df[30]==1]: Creates a new dataframe called 'cancer' that contains only the rows where column 30 has the value 1, indicating cancer cases.
- no_cancer = df[df[30]==0]: Creates another new dataframe called 'no_cancer' that contains the rows where column 30 has the value 0, indicating cases without cancer.

### UNDERSAMPLING

As explained in the definition, the idea is to reduce the number of records from class '0' (majority class) to match the 20 records of class '1' (minority class), and this is done as follows:

![imagen 5](/Article/images/Imagen5_separaciondatos.png)

This part of the code is using the sample method from pandas to perform undersampling. Here are the details:

![imagen 6](/Article/images/Imagen6_undersampling.png)

- n=20: 20 samples are randomly selected from the 'no_cancer' dataframe. This means the size of 'no_cancer' will be reduced to 20 instances.
- replace=False: This indicates that samples are selected without replacement. In other words, each selected sample cannot be chosen again, ensuring there are no duplicates in the dataset.
- random_state=0: Sets a seed for random number generation, ensuring that if you run this code multiple times, you will get the same random selection each time.
- undersampling_no_cancer: This stores the result of undersampling in the variable 'undersampling_no_cancer'. This new dataframe will contain only 20 random instances from 'no_cancer'.

![imagen 7](/Article/images/Imagen7_undersamplingdivision.png)

Finally, the data of patients with cancer is concatenated with the previous dataframe to create the balanced dataset through undersampling. Additionally, we separate the dataset into input data (X_undersampling) and output data (y_undersampling), corresponding to the respective classes for each instance.

### OVERSAMPLING

As per its definition, the objective is to replicate instances of class '1' (minority class) until matching the number of records in class '0' (majority class) with 290 instances each.

![imagen 8](/Article/images/Imagen8_oversampling.png)

- .sample(n=290, replace=True, random_state=0): This part of the code line uses the pandas sample method to perform oversampling. Here are the details:
- n=290: 290 random samples are extracted from the 'cancer' dataframe. These samples will be replicated to perform oversampling.
- replace=True: This indicates that samples are selected with replacement, meaning that the same observation from the original dataset can be selected multiple times to be part of the new dataset.
- random_state=0: Sets a seed for random number generation. Using a seed ensures that if you run this code multiple times, you will get the same set of random samples each time.

![imagen 9](/Article/images/Imagen9_oversamplingdivision.png)

Finally, we combine the data of patients without cancer with the newly created dataframe to have a balanced dataset through oversampling. Additionally, we separate the dataset into input data and output data.

## CLASSIFICATION MODEL

To observe how these types of techniques enhance the performance of a model, we created three classification models using Logistic Regression for each dataset. The first one using the imbalanced dataset, the second one with the data balanced through undersampling, and the last model using the dataset balanced through oversampling.

![imagen 10](/Article/images/Imagen10_unbalanceddata.png)

To validate the model's performance, a test dataset with 20 instances (10 from patients with cancer and 10 from patients without cancer) was loaded, which the trained model will not have seen before:

![imagen 11](/Article/images/Imagen11_testdata.png)

### Model 1

The first model is trained with the imbalanced data:

![imagen 12](/Article/images/Imagen12_modelo1.png)

Using the confusion matrix, it is evident that the trained model successfully classifies all patients without cancer optimally, while it only correctly classifies 4 patients with cancer and fails to classify the remaining 6. Additionally, it is observed that the accuracy is 70%.

### Model 2

The second model is trained with data balanced using the undersampling technique:

![imagen 13](/Article/images/Imagen13_modelo2.png)

In this case, using the confusion matrix, it is evident that the trained model successfully classifies all patients without cancer optimally. It only fails in classifying 1 patient with cancer, while correctly classifying the remaining 9. Additionally, it is observed that the accuracy has increased to 95%, which is an improvement compared to the previous model.

### Model 3

The last model is trained with the dataset balanced through oversampling:

![imagen 14](/Article/images/Imagen14_modelo3.png)

In this last model, using the confusion matrix, the same results as the previous model were obtained – all cancer patients were classified correctly, while for patients without cancer, there is an error in one data point, and the remaining nine are classified correctly. Additionally, an accuracy of 95% is achieved, improving the score obtained with the imbalanced dataset.

### How to choose between undersampling and oversampling?

The choice between undersampling and oversampling depends on the specific case. Undersampling can be effective when the dataset is large, and redundant information can be removed without severely impacting the model's performance. On the other hand, oversampling is useful when the amount of data is limited, and there is a need to strengthen the representation of minority classes.

### EXTRA INFORMATION

There are other advanced techniques beyond traditional undersampling and oversampling. One example is SMOTE (Synthetic Minority Over-sampling Technique), which creates synthetic instances for minority classes, intelligently expanding the dataset without replicating data, thereby avoiding repeated or duplicated data.

## CONCLUSIONS

![BALANCE](/Article/images/balance.jpg)

In the journey towards more precise and high-performance models, data balancing becomes an indispensable ally. Whether instances are reduced or minority classes are expanded, these techniques stand out as essential tools for solving challenges in the field of data science.

As observed, both techniques improved the model's performance, preventing it from misclassifying data that was not possible to achieve with imbalanced data. Additionally, the accuracy increased significantly. But what happens when data balancing techniques cannot be implemented? There are other types of solutions, such as considering alternative metrics like f1-score or recall, which provide a different understanding of what machine learning aims to address. Another approach involves assigning weights to trained models to account for data imbalance. However, these topics will be discussed on another occasion.

## RELATED REFERENCES

- Gutiérrez-García, J.O. [Código Máquina]. (2023, August 7). Qué son los Datos Desbalanceados y Cómo balancearlos usando Submuestreo y Sobremuestreo con Python [Video]. YouTube. [https://www.youtube.com/watch?v=2J90FG6QKL4&ab_channel=CodigoMaquina].
- Cómo actuar ante el desbalance de datos | by Nicolás Arrioja Landa Cosio | Medium https://medium.com/@nicolasarrioja/c%C3%B3mo-actuar-ante-el-desbalance-de-datos-a0d64f2b9619
- Gutiérrez-García, J.O. [Código Máquina]. (2022, August 20). Métricas para Clasificadores de Machine Learning: Matriz de Confusión, Precision, Accuracy, Recall, F1 [Video]. YouTube. [https://www.youtube.com/watch?v=uaGMk43XTOw&ab_channel=CodigoMaquina]

#### *By Daniel Augusto Muñoz Viveros*