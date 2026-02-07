from http.server import BaseHTTPRequestHandler  # Simple HTTP handler for Vercel
from pathlib import Path  # Safe file path handling
import json  # Build JSON error responses
import pandas as pd  # Data processing library


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Return the summary report as CSV."""
        try:
            # Build a path to the input CSV using the project root
            project_root = Path(__file__).resolve().parent.parent
            data_path = project_root / "data" / "sales_data.csv"

            data = pd.read_csv(data_path)  # Load the CSV data
            cleaned = data.dropna()  # Remove rows with missing values
            report = cleaned.describe()  # Create summary statistics

            csv_text = report.to_csv()  # Convert report to CSV text

            self.send_response(200)  # HTTP 200 OK
            self.send_header("Content-Type", "text/csv")  # Let clients know it's CSV
            self.end_headers()
            self.wfile.write(csv_text.encode("utf-8"))  # Send the response body
        except FileNotFoundError:
            self.send_response(404)  # HTTP 404 if the CSV file is missing
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "sales_data.csv not found"}).encode("utf-8"))
        except Exception as error:
            self.send_response(500)  # HTTP 500 for unexpected errors
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(error)}).encode("utf-8"))
