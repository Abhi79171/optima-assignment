# F1 Data Pipeline (Local Development Guide)

## What This Pipeline Does
This Python-based data pipeline reads Formula 1 race data from `races.csv` and `results.csv`, and generates structured JSON files one per year with key information for each race:

- Race Name
- Round Number
- Full Race Datetime in UTC (ISO 8601 format)
- Winning Driver ID
- Fastest Lap Time

This pipeline also logs any races that couldn’t be processed due to missing or malformed data.

## How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Abhi79171/optima-assignment.git
cd optima-assignment/data-engineering/datapipeline/solution
```
## 2. Install Requirements

It is recommended to use a virtual environment. Then install dependencies:

```bash
pip install -r requirements.txt
```
## 3. Check Input CSVs

Verify weather `races.csv` and `results.csv` files are inside the `source-data/` folder.  

## 4. Run the Pipeline

```bash
python main.py
```
This will process all races and write output files to the `results/` folder.

You’ll see two types of output per year:

- `stats_2024.json`: Structured race data  
- `errors_2024.json`: It will only generate if that particular year has any races skipped due to missing or invalid data 

## 5. Validations Performed

- **Time Cleanup**: Any missing or invalid times in `races.csv` are replaced with `00:00:00`.  
- **ISO Datetime Format**: Each race’s date and time is converted to ISO 8601 format: `YYYY-MM-DDTHH:MM:SS.000`.  
- **Winner Extraction**: From `results.csv`, the driver with `position == 1.0` is treated as the winner. If this is missing, the race is logged as an error.  

## 6. Unit Testing

Unit tests are included in `test_pipeline.py`.

To run all tests:

```bash
pytest test_pipeline.py
```

### 7. Test Coverage

- `test_clean_time_column()`: Validates handling of missing/invalid times.  
- `test_extract_winner_valid()`: Checks correct winner and lap time extraction.  
- `test_extract_winner_no_winner()`: Handles races with no winner.  
- `test_extract_winner_race_missing()`: Handles missing race IDs.  




This version is intended for local development and testing.

For cloud deployment (AWS S3 + Lambda) and public testing via Postman please refer [README.release.md](README.release.md)
