# SAP Sales Data Engineering Pipeline

# SAP Sales Data Engineering Pipeline

I built this project to get more hands on experience with data engineering workflows using real world style SAP sales data instead of small toy datasets.

In this project, I worked with SAP style billing and sales records from Excel files, cleaned and validated the data, generated reporting outputs, exported cleaned datasets, and loaded the results into a SQL database. I mainly built this project to practice creating a structured ETL workflow while improving my skills in Python, SQL, data validation, logging, and pipeline organization.

One of my main goals with this project was to keep the workflow modular and maintainable instead of putting everything into one large script. I also added automated validation checks, logging, reporting, and export functionality to better simulate how real data pipelines are handled in production environments.

---

# Features

- Excel-based SAP dataset ingestion
- Data cleaning and column normalization
- Duplicate record validation
- Missing-value validation
- Business-rule validation checks
- Automated CSV export workflows
- Validation summary report generation
- SQLite database loading
- Pipeline logging and monitoring
- Modular ETL pipeline structure

---

# Tech stack

- Python
- pandas
- SQLAlchemy
- SQLite
- Git/GitHub

---

# Project structure

```text
sap-sales-data-engineering-pipeline/
│
├── data/
│   ├── raw/
│   ├── processed/
│
├── logs/
├── reports/
├── sql/
├── src/
│   ├── extract/
│   ├── transform/
│   ├── validate/
│   ├── export/
│   ├── load/
│   ├── reports/
│   └── utils/
│
├── tests/
├── README.md
├── requirements.txt
└── sap_sales.db
```

---

# Pipeline workflow

```text
Raw SAP Billing Data
        ↓
Extract
        ↓
Transform / Normalize
        ↓
Validate Data Quality
        ↓
Generate Reports
        ↓
Export Clean CSV
        ↓
Load Into SQL Database
```

---

# Validation checks

The pipeline currently validates:

- Duplicate billing document/item combinations
- Missing required values
- Invalid business-rule values
- Dataset integrity and row consistency

---

# Outputs

Generated outputs include:

```text
reports/validation_summary.csv
data/processed/clean_vbrp.csv
logs/pipeline.log
sap_sales.db
```

---

# Example pipeline log

```text
INFO - Pipeline started
INFO - Loaded dataset with 500 rows
INFO - Duplicate records found: 0
INFO - Missing required value records: 0
INFO - Invalid business value records: 0
INFO - Validation summary report generated
INFO - Clean CSV export completed
INFO - SQLite load completed
INFO - Pipeline completed successfully
```

---

# Currently working on

- Migrating the pipeline from SQLite to PostgreSQL for a more production-style database workflow