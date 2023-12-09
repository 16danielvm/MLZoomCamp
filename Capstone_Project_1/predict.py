# Load the model
import pickle
from flask import Flask
from flask import request
from flask import jsonify
import xgboost as xgb


model_file = 'final_model.bin'


with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('status')

@app.route('/predict', methods = ['POST'])
def predict():

    customer = request.get_json()

    X = dv.transform([customer])
    features = dv.feature_names_ 
    dval = xgb.DMatrix(X, feature_names=features)
    y_pred = model.predict(dval)

    result = {
        'status': int(y_pred)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)