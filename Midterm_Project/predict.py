# Load the model
import pickle
from flask import Flask
from flask import request
from flask import jsonify
import numpy as np


model_file = 'final_model.bin'


with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('stress_level')

@app.route('/predict', methods = ['POST'])
def predict():

    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict(X)

    result = {
        'stress_level': int(y_pred)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)