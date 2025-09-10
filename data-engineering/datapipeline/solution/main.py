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

def main():
    print("Loading data...")
    races_df = pd.read_csv(RACES_CSV)
    results_df = pd.read_csv(RESULTS_CSV)

    print("Cleaning time column...")
    races_df = clean_time_column(races_df)

    # It creates a results folder if it's not available
    print("Preparing output directory...")
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # It Groups results by raceId for faster lookup
    grouped_results = results_df.groupby("raceId")

    print("Processing races by year...")
    for year in sorted(races_df["year"].unique()):
        races_in_year = races_df[races_df["year"] == year]
        year_output = []  # For each year this list stores final JSON entries
        error_log = []    # For each year this list stores errors (if any)

        for race in races_in_year.itertuples(index=False):
            # It formats datetime as ISO 8601(this is format is used in example provided)
            race_datetime = f"{race.date}T{race.time}.000"

            # It extracts the winner details by calling extract_winner function
            driver_id, fastest_lap, error_reason = extract_winner(race.raceId, grouped_results)

            if error_reason:
                # If error_reason is not null then the error details are  stored in error_log list
                error_log.append({
                    "Race Id": int(race.raceId),
                    "Race Name": race.name,
                    "Reason": error_reason
                })
                continue

            # Structured output entry for a race as mentioned in example
            race_entry = {
                "Race Name": race.name,
                "Race Round": int(race.round),
                "Race Datetime": race_datetime,
                "Race Winning driverId": driver_id,
                "Race Fastest Lap": fastest_lap
            }

            year_output.append(race_entry)

        # It writes output JSON for a particular year
        output_path = os.path.join(RESULTS_DIR, f"stats_{year}.json")
        with open(output_path, "w") as f:
            json.dump(year_output, f, indent=2)
        print(f"stats_{year}.json written with {len(year_output)} races.")

        # It writes error log if any races failed processing
        if error_log:
            error_path = os.path.join(RESULTS_DIR, f"errors_{year}.json")
            with open(error_path, "w") as f:
                json.dump(error_log, f, indent=2)
            print(f"errors_{year}.json written with {len(error_log)} issues.")

    print("All done. please check the 'results/' folder.")


# Entry point of the script
if __name__ == "__main__":
    main()
