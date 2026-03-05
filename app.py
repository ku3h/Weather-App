from flask import Flask, jsonify, request
from dotenv import load_dotenv
import requests
import os

load_dotenv() 

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/weather", methods=["GET"]) 
def get_weather():
    city = request.args.get("city") 
    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    response = requests.get(BASE_URL, params={
        "q": city,
        "appid": API_KEY,
        "units": "imperial"
    })

    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404

    data = response.json()

    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"]
    }

    return jsonify(weather) 

if __name__ == "__main__":
    app.run(debug=True)