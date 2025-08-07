import sqlite3

def load_to_sqlite(df, db_path="data/weather.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("weather_data", conn, if_exists="append", index=False)
    conn.close()
