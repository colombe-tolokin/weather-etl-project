import pandas as pd

def clean_weather_data(raw_json):
    current = raw_json.get("current_weather", {})
    df = pd.DataFrame([current])
    df["timestamp"] = pd.Timestamp.now()
    return df
