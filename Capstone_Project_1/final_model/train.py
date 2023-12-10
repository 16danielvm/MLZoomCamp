import pickle

import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction import DictVectorizer

from sklearn.metrics import roc_auc_score

import xgboost as xgb

output_file = 'final_model.bin'

#Data preparation

DATA_PATH = '../data/train.csv'
df = pd.read_csv(DATA_PATH)

df['Cholesterol'] = df['Cholesterol'].astype('int64')
df['Copper'] = df['Copper'].astype('int64')
df['Tryglicerides'] = df['Tryglicerides'].astype('int64')
df['Platelets'] = df['Platelets'].astype('int64')
df['Stage'] = df['Stage'].astype('int64')

# Encoding the categorical variables
le = LabelEncoder()
df = df.apply(le.fit_transform)

# Scaling the numerical variables
scaler = StandardScaler()
df[['N_Days', 'Age', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos','SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin']] = scaler.fit_transform(df[['N_Days', 'Age', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper', 'Alk_Phos','SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin']]) 

# Dropping the id column
df = df.drop(['id'], axis=1)


df_train, df_val = train_test_split(df, test_size=0.20, random_state=1, stratify=df.Status)

# check the notebook for feature selection
most_importan_features = ['Bilirubin', 'Copper', 'N_Days', 'Stage', 'Hepatomegaly', 'Prothrombin', 'SGOT', 'Edema', 'Platelets', 'Age', 'Cholesterol', 'Drug']

xgb_params = {
    'eta': 0.1,
    'max_depth': 3,
    'min_child_weight':10,

    'objective': 'multi:softmax',
    'num_class': 3,
    'eval_metric': 'logloss',

    'nthread': 8,
    'seed': 1,
    'verbosity': 1
}

# Training
def train(df_train, y_train):
    dicts = df_train[most_importan_features].to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    features = dv.feature_names_
    dtrain = xgb.DMatrix(X_train, label= y_train, feature_names=features)

    model = xgb.train(xgb_params, dtrain, num_boost_round = 300 )
    
    return dv, model

def predict(df, y_val, dv, model):
    dicts = df[most_importan_features].to_dict(orient='records')

    X_val = dv.transform(dicts)
    features = dv.feature_names_ 
    dval = xgb.DMatrix(X_val, label=y_val, feature_names=features)
    
    y_pred = model.predict(dval)
    probabilities = model.predict(dval, output_margin=True)
    probabilities = np.exp(probabilities) / np.sum(np.exp(probabilities), axis=1, keepdims=True)

    return y_pred, probabilities

# Training the final model
print('training the final model')

dv, model = train(df_train, df_train.Status.values)
y_pred, probabilities = predict(df_val,df_val.Status.values, dv, model)

y_test = df_val.Status.values
auc = roc_auc_score(y_test, probabilities , multi_class='ovr')

print('AUC: %.3f' % auc)

# Save the model

# model.save_model('modelo_guardado.json')
print('Model saved to modelo_guardado.json')

with open(output_file, 'wb') as f_out:
    pickle.dump((dv,model), f_out)

print('Model saved to %s' % output_file)


