from flask import Flask
from flask_restful import Api, Resource, reqparse
import joblib
import numpy as np

APP = Flask(__name__)
API = Api(APP)

model = joblib.load('api.joblib')

class Predict(Resource):

    @staticmethod
    def post():

        parser = reqparse.RequestParser()
        parser.add_argument('Hour')
        parser.add_argument('Temperature')
        parser.add_argument('Humidity')
        parser.add_argument('windSpeed')
        parser.add_argument('Visibility')
        parser.add_argument('dpTemperature')
        parser.add_argument('solarRadiation')
        parser.add_argument('Rainfall')
        parser.add_argument('Snowfall')
        parser.add_argument('Seasons')
        parser.add_argument('Holiday')
        parser.add_argument('functioningDay')
        parser.add_argument('Snowy')
        parser.add_argument('Rainy')
        parser.add_argument('Sunny')
        parser.add_argument('VisMax')
        parser.add_argument('Month')
        args = parser.parse_args()

        X_new = np.fromiter(args.values(), dtype=float) 


        out = {'Pred_model': model.predict([X_new])[0]}

        return out


API.add_resource(Predict, '/predict')

if __name__ == '__main__':
    APP.run(debug=False, port='5000')
