# Load the model
import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as model_in:
    model = pickle.load(model_in)

with open(dv_file, 'rb') as dv_in:
    dv = pickle.load(dv_in)

app = Flask('bankCredit')

@app.route('/predict_flask', methods = ['POST'])
def predict():

    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0,1]
    bank_credit = y_pred >= 0.5

    result = {
        'bank_credit_probability': float(y_pred),
        'bank_credit': bool(bank_credit)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)