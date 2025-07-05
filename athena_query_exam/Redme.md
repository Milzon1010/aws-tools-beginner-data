
Athena Query Example

This project demonstrates how to run a simple Athena query using boto3.

## 🧠 What It Does
- Runs a SQL query against a sample Athena database
- Saves results to an S3 bucket
- Logs query execution ID

## 📂 Files
- `athena_run.py` — script to trigger Athena query
- `query.sql` — example query
- `README.md` — instructions

## 🛠️ Before Running
- Update `DATABASE`, `TABLE`, and `OUTPUT_LOCATION` in `athena_run.py`
- Ensure your AWS CLI credentials are configured properly
