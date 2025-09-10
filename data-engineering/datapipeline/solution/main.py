import pandas as pd
import json
import os
from datetime import datetime

# It defines source and destination directories
SOURCE_DATA_DIR = "../source-data"
RESULTS_DIR = "../results"

# CSV file paths
RACES_CSV = os.path.join(SOURCE_DATA_DIR, "races.csv")
RESULTS_CSV = os.path.join(SOURCE_DATA_DIR, "results.csv")


def clean_time_column(df):
    """
    It cleans up the 'time' column in races.csv by performing below validation.
    If a time value is missing or malformed, set it to '00:00:00'.
    """
    cleaned = []
    for t in df["time"]:
        if pd.isna(t) or str(t).strip() == "":
            cleaned.append("00:00:00")
        else:
            try:
                t_str = str(t).strip()
                parsed = datetime.strptime(t_str, "%H:%M:%S")
                cleaned.append(parsed.strftime("%H:%M:%S"))
            except Exception:
                # If time format is invalid, like for example 2pm it fall backs to default
                cleaned.append("00:00:00")
    df["time"] = cleaned
    return df
