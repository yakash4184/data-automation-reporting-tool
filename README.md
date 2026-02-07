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

## Live on Vercel (Optional)
This repo includes a simple API endpoint at `api/report.py`. Vercel deploys files inside `api/` as serverless functions, so your report becomes available at `/api/report` after deployment.

### Steps (GitHub Import)
1. Push this repository to GitHub (already done).
2. In the Vercel dashboard, create a New Project and import the GitHub repo.
3. Keep the default settings and deploy.

### Homepage
After deployment, the root URL shows a simple landing page with a link to the report endpoint.

### Test The Live Endpoint
Open the URL below in a browser after deployment:
```
https://<your-project>.vercel.app/api/report
```
You should see the summary report as CSV.

### Notes About Serverless Behavior
- The function reads `data/sales_data.csv` at request time and generates the report on the fly.
- Vercel functions use a read-only file system at runtime, so the report is returned as a response instead of being written to the repo.
- The `vercel.json` file explicitly includes `data/sales_data.csv` in the function bundle.


## Upload Your Own CSV (Live Demo)
The homepage allows users to upload their own CSV file or paste CSV text. The server generates a summary report and returns it as CSV.

**Required CSV format:**
```
date,sales,profit
2025-01-01,1200,300
2025-01-02,1500,420
```

**Rules:**
- Columns must be exactly: `date`, `sales`, `profit`
- `date` should be in `YYYY-MM-DD`
- `sales` and `profit` should be numeric
- Missing values are allowed (they will be removed during cleaning)

**Endpoint used:**
`/api/report_upload`

