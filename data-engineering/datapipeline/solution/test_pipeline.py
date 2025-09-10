import pandas as pd
from main import clean_time_column  
from main import extract_winner

def test_clean_time_column():
    df = pd.DataFrame({
        "time": ["13:00:00", "invalid", "", None, " 15:30:00 "]
    })

    result = clean_time_column(df.copy())

    assert result["time"].tolist() == [
        "13:00:00",
        "00:00:00",
        "00:00:00",
        "00:00:00",
        "15:30:00"
    ]


def test_extract_winner_valid():
    df = pd.DataFrame({
        "raceId": [1, 1, 2],
        "driverId": [101, 102, 103],
        "position": [1.0, 2.0, 1.0],
        "fastestLapTime": ["01:23.4", "01:24.1", "01:22.9"]
    })

    grouped = df.groupby("raceId")
    driver_id, lap, err = extract_winner(1, grouped)
    assert driver_id == 101
    assert lap == "01:23.4"
    assert err is None

def test_extract_winner_no_winner():
    df = pd.DataFrame({
        "raceId": [1, 1],
        "driverId": [101, 102],
        "position": [2.0, 3.0],
        "fastestLapTime": ["01:23.4", "01:24.1"]
    })

    grouped = df.groupby("raceId")
    driver_id, lap, err = extract_winner(1, grouped)
    assert driver_id is None
    assert lap is None
    assert err == "No winner (position == 1.0) found"

def test_extract_winner_race_missing():
    df = pd.DataFrame({
        "raceId": [1],
        "driverId": [101],
        "position": [1.0],
        "fastestLapTime": ["01:23.4"]
    })

    grouped = df.groupby("raceId")
    driver_id, lap, err = extract_winner(99, grouped)
    assert driver_id is None
    assert lap is None
    assert err == "No results found for raceId"
