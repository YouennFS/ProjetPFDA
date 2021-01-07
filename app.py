from joblib import load
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)


@app.route('/api/', methods=['POST','GET'])
def makecalc():
    data = request.get_json()
    data = np.asarray(data)
    data = data.reshape(1,-1)
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    #modelfile = 'models/final_prediction.pickle'
    model = load(open('api.joblib','rb'))
    app.run(debug=False, host='0.0.0.0')