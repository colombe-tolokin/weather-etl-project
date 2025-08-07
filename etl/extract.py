import requests

def fetch_weather_data(latitude=45.42, longitude=-75.69):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
