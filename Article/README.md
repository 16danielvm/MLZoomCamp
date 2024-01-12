# Balancing the Game: Undersampling and Oversampling

![UNBALANCED](Article\images\unbalance.jpg)

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