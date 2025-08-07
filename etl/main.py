from extract import fetch_weather_data
from transform import clean_weather_data
from load import load_to_sqlite

def run_etl():
    raw = fetch_weather_data()
    cleaned = clean_weather_data(raw)
    load_to_sqlite(cleaned)

if __name__ == "__main__":
    run_etl()
