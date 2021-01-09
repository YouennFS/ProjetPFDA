import requests

url = 'http://127.0.0.1:5000/predict'  # localhost and the defined port + endpoint
body = {
        "Hour":0,
        "Temperature":-5.2,
        "Humidity":37,
        "windSpeed":2.2,
        "Visibility":2000,
        "dpTemperature":-17.6,
        "solarRadiation":0.0,
        "Rainfall":0.0,
        "Snowfall":0.0,
        "Seasons":0,
        "Holiday":0,
        "functioningDay":1,
        "Snowy":0,
        "Rainy":0,
        "Sunny":0,
        "VisMax":0,
        "Month":12
        
}
response = requests.post(url, data=body)
response.json()
    
