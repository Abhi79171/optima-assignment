# F1 Data Pipeline — Local Development Guide

## What This Pipeline Does
This Python-based data pipeline reads Formula 1 race data from `races.csv` and `results.csv`, and generates structured JSON files—one per year—with key information for each race:

- Race Name
- Round Number
- Full Race Datetime in UTC (ISO 8601 format)
- Winning Driver ID
- Fastest Lap Time

The pipeline also logs any races that couldn’t be processed due to missing or malformed data.

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

