# Weather App 🌤️

A REST API backend built with Python and Flask that returns real-time weather data for any city.

## Tech Stack
- Python
- Flask
- OpenWeather API

## How to Run
1. Clone the repo
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install flask requests python-dotenv`
5. Add your OpenWeather API key to a `.env` file: `OPENWEATHER_API_KEY=your_key`
6. Run: `python3 app.py`

## Endpoints
`GET /weather?city=London` — Returns temperature, humidity, and weather description for a given city