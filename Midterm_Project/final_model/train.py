import pickle

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction import DictVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Parameters

solver = 'liblinear'
random_state = 1

output_file = 'final_model.bin'

#Data preparation

DATA_PATH = '../data/SaYoPillow.csv'
df = pd.read_csv(DATA_PATH)

df.columns = ['snoring_rate','respiration_rate','body_temperature','limb_movement','blood_oxygen','eye_movement','sleeping_hours','heart_rate','stress_level']

df_train, df_val = train_test_split(df, test_size=0.20, random_state=1, stratify=df.stress_level)

# check the notebook for feature selection
most_importan_features = ['limb_movement', 'sleeping_hours', 'snoring_rate', 'eye_movement', 'body_temperature']

# Training

def train(df_train, y_train, solver=solver, random_state=random_state):
    dicts = df_train[most_importan_features].to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    model = LogisticRegression(solver= solver, random_state=random_state)
    model.fit(X_train, y_train)

    return dv, model

def predict(df, dv, model):
    dicts = df[most_importan_features].to_dict(orient='records')

    X = dv.transform(dicts)
    y_pred = model.predict(X)

    return y_pred

# Training the final model
print('training the final model')

dv, model = train(df_train, df_train.stress_level.values, solver, random_state)
y_pred = predict(df_val, dv, model)

y_test = df_val.stress_level.values
acc = accuracy_score(y_test, y_pred)

print('Accuracy: %.3f' % acc)

# Save the model

with open(output_file, 'wb') as f_out:
    pickle.dump((dv,model), f_out)

print('Model saved to %s' % output_file)


