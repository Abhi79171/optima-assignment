#  F1 Data Pipeline (Cloud Deployment Guide)


##  Cloud Architecture Overview

The local Python script is restructured to run serverlessly using **AWS Lambda** triggered by **S3 file uploads**.

### What Happens

1. A user uploads `races.csv` and `results.csv` into an input S3 bucket.
2. This triggers a Lambda function.
3. The function processes the data and writes:
   - `stats_{year}.json`
   - `errors_{year}.json`
   into the same S3 bucket output folder.

---

## Why AWS?

AWS is chosen for its:

- Native support for event-driven architecture (S3 triggers for Lambda)
- Free-tier friendly usage
- Simple integration and permission model
- Fast setup for prototype/demo use cases


---

## Important Note on Security

This current version **does not include any security or access control**.

- Buckets have public read/write enabled
- No IAM policies are there to restrict who can invoke Lambda or write to S3
- There’s no input validation or rate limiting

This was intentional to keep the setup minimal for a demo.

---

##  How to Test It Publicly (Postman or Curl)

### 1. Upload Input Files (Public S3)

Use `PUT` or `POST` to upload `races.csv` and `results.csv` to input folder in S3 bucket.

**Example using Postman:**

- Method: `PUT`
- URL: [https://datapipeline-f1-bucket.s3.eu-west-2.amazonaws.com/input/races.csv](https://datapipeline-f1-bucket.s3.eu-west-2.amazonaws.com/input/races.csv)
- Body: select `binary` and upload `races.csv` file

Repeat the same for `results.csv`.

The Lambda function will auto-trigger and generate the outputs.

### 2. Download Output Files

Once processed, check the `output/` folder in the same S3 bucket. Files will be named:

- `stats_2024.json`
- `errors_2024.json` (if applicable)

These can also be accessed via public S3 URLs like:
[https://datapipeline-f1-bucket.s3.eu-west-2.amazonaws.com/output/stats_2019.json](https://datapipeline-f1-bucket.s3.eu-west-2.amazonaws.com/output/stats_2019.json)


---

##  Future Improvements with Terraform (IaC - Infrastructure as Code)

This entire setup (S3 + Lambda + IAM Roles + Trigger config) can be automated using **Terraform**, allowing Infrastructure-as-Code deployment.

### What Terraform Would Manage:

- S3 buckets (input/output, versioning, ACLs)
- Lambda function packaging and deployment
- IAM roles and permissions
- S3 event triggers for Lambda
- Output variables for testing (e.g., bucket URLs)

Using Terraform ensures reproducibility, auditability, and clean teardown after the demo.

---

## Summary

- AWS S3 + Lambda is used for zero-server deployment.
- Anyone can test by uploading two files (`races.csv`, `results.csv`) to the public bucket.
- Output JSONs are auto-generated and publicly accessible.
- Security is intentionally skipped for now only for internal or temporary testing.
- Terraform can be introduced to manage infra cleanly in future iterations.

---


This version is intended for Cloud Deployment and testing.

For local deployment and testing please refer [local_setup.md](local_setup.md)
