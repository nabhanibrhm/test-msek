# test-msek

📊 Mandiri Sekuritas Technical Test

This repository contains solutions for the Mandiri Sekuritas Technical Test, organized into two tasks:

Task 1: Complaint Resolution Analysis (static PDF report)

Task 2: Luxury Loan Portfolio Dashboard (interactive Plotly Dash app)

m-sek/
├─ db/                         # Postgres init scripts
│   └─ init/01_create_and_load.sql
├─ task1/                      # Task 1: Static report
│   ├─ data/                   # CSVs and SQL for analysis
│   │   ├─ CRMEvents.csv
│   │   ├─ CRMCallCenterLogs.csv
│   │   └─ analysis.sql
│   ├─ generate_report.py       # Script to generate PDF report
│   └─ Complaint_Resolution_Report.pdf (output)
├─ task2/                      # Task 2: Plotly Dash app
│   ├─ data/LuxuryLoanPortfolio.csv
│   └─ app.py
├─ Dockerfile.task1            # Image for Task 1 (pandas, matplotlib, reportlab)
├─ Dockerfile.task2            # Image for Task 2 (pandas, dash, plotly)
└─ docker-compose.yml
