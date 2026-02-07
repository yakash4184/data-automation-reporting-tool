# Data Automation & Reporting Tool

## What This Project Does
This project reads sales data from a CSV file, cleans the data by removing missing values, generates a summary report, and saves the report as a new CSV file. It is designed to be simple and easy to explain in interviews.

## Why It Is Useful
In real companies, data often comes in messy spreadsheets. This tool shows how to automate a basic data workflow so teams can quickly get clean data and summary insights for reporting and decision-making.

## Technologies Used
- Python
- Pandas

## Project Structure
```
data-automation-reporting-tool/
│
├── data/
│   └── sales_data.csv
│
├── output/
│   └── summary_report.csv
│
├── automation.py
├── requirements.txt
└── README.md
```

## How To Run (Step-by-Step)
1. Open a terminal in the project folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python automation.py
   ```

## What Output Is Generated
- The cleaned data is used to create a summary report.
- The report is saved to:
  `output/summary_report.csv`

The report contains summary statistics like count, mean, min, and max for the numeric columns (sales and profit).

## Interview Talking Points
- Python basics: functions, variables, file paths, and error handling
- Data handling: reading CSV, cleaning missing values, and generating summaries
- Automation: running a repeatable process with clear steps
- Error handling: try-except blocks for safe execution
