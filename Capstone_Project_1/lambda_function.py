import pickle
import xgboost as xgb

model_file = 'final_model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)


def predict(customer):
    
    X = dv.transform([customer])
    features = dv.feature_names_ 
    dval = xgb.DMatrix(X, feature_names=features)
    y_pred = model.predict(dval) 
    
    if y_pred == 0:
        return ('Your Cirrhosis status is C.')
    elif y_pred == 1:
        return('Your Cirrhosis status is CL.')
    elif y_pred == 2:
        return('Your Cirrhosis status is D.')
    

def lambda_handler(event, context):
    customer = event['customer']
    result = predict(customer)
    return result





