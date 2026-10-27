from pathlib import Path
import pandas as pd
import os
import psycopg
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

df = pd.read_csv(DATA_DIR / "ttc_subway_delay_data_since_2025.csv")

df = df.rename(columns={
    "_id": "id",
    "Day": "day",
    "Station": "station",
    "Code": "code",
    "Min Delay": "min_delay",
    "Min Gap": "min_gap",
    "Bound": "bound",
    "Line": "line",
    "Vehicle": "vehicle_id",})

df["occurred_at"] = pd.to_datetime(df["Date"] + " " + df["Time"])
df = df.drop(columns=["Date", "Time"])

load_dotenv()

columns = ["id", "occurred_at", "day", "station", "code",
           "min_delay", "min_gap", "bound", "line", "vehicle_id"]

df = df[columns].astype(object).where(df[columns].notna(), None)
rows = list(df.itertuples(index=False, name=None))

sql = """
INSERT INTO ttc_delay_since_2025
    (id, occurred_at, day, station, code, min_delay, min_gap, bound, line, vehicle_id)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (id) DO NOTHING
"""

with psycopg.connect(
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
) as conn:
    with conn.cursor() as cur:
        cur.executemany(sql, rows)

