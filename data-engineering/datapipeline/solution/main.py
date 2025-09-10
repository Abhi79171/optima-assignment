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

def extract_winner(race_id, grouped_results):
    """
    By passing a race ID, it extracts the winning driver's ID and fastest lap time.
    If race or winner info is missing, it returns an error message.
    """
    try:
        race_results = grouped_results.get_group(race_id)
    except KeyError:
        return None, None, "No results found for raceId"

    # Finds the row with position == 1 (winner)
    winner_row = race_results[race_results['position'] == 1.0]
    if winner_row.empty:
        return None, None, "No winner (position == 1.0) found"

    winner = winner_row.iloc[0]
    return int(winner['driverId']), winner['fastestLapTime'], None
