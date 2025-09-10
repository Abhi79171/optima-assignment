# F1 Data Pipeline Solution

This project is a complete end-to-end data pipeline built for rapid post-race processing of Formula 1 datasets. It meets all `core requirements` and `stretch goals` as outlined in the original assignment.

---

## Features Implemented

- Reads `races.csv` and `results.csv` to automatically generate structured JSON output files (one per year)
- Handles missing or malformed race times with fallback values
- Extracts winning driver and fastest lap per race
- Outputs:
  - `stats_{year}.json`  per-race structured data
  - `errors_{year}.json`  skipped races with reasons
- Proper formatting in ISO 8601 (`YYYY-MM-DDTHH:MM:SS.000`)
- Data type correctness in output JSON (e.g., no unnecessary strings)
- Full unit test coverage for all core logic functions
- GitHub Actions workflow for automated CI on pull requests and commits
- Fully deployed on **AWS using S3 + Lambda** for serverless execution

---

## Testing & CI

- Unit tests for all validation and processing functions are available in `test_pipeline.py`
- GitHub Actions (`.github/workflows/test.yml`) automatically runs tests on every commit and pull request

---

## Deployment

This project is **already deployed** using AWS S3 + AWS Lambda for serverless execution.

To view the deployed architecture and testing steps, please refer:  
 [release_notes.md](release_notes.md)

---

## Local Development

To run and test the project locally (including unit testing), please refer to:  
 [local_setup.md](local_setup.md)

---

## File Breakdown

- `README.local.md` — local setup and usage
- `README.release.md` — AWS deployment architecture and testing steps
- `main.py` — core pipeline logic
- `requirements.txt` — Python dependencies (e.g., `pandas`)
- `test_pipeline.py` — unit tests

## Demo Videos

Execution walkthroughs covering the local testing, cloud deployment and testing, and also Postman based testing are available at the following link:
[https://drive.google.com/drive/folders/1lXFr5kxnVFgCLx0_lSyR1paFpCRxc6MR?usp=sharing](https://drive.google.com/drive/folders/1lXFr5kxnVFgCLx0_lSyR1paFpCRxc6MR?usp=sharing)
