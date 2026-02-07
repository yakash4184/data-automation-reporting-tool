from http.server import BaseHTTPRequestHandler  # Simple HTTP handler for Vercel
from io import StringIO  # Convert text into a file-like object
import json  # Parse JSON request bodies
import pandas as pd  # Data processing library


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """Accept CSV text in the request body and return a summary report."""
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(content_length)  # Read the request body

            content_type = self.headers.get("Content-Type", "")
            csv_text = ""

            if "application/json" in content_type:
                payload = json.loads(body.decode("utf-8"))  # Convert JSON to dict
                csv_text = payload.get("csv", "")  # Get CSV text from payload
            elif "text/csv" in content_type:
                csv_text = body.decode("utf-8")  # Treat body as raw CSV
            else:
                self.send_response(415)  # Unsupported media type
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(
                    json.dumps({"error": "Send CSV as JSON {csv: '...'} or text/csv."}).encode("utf-8")
                )
                return

            if not csv_text.strip():
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": "CSV content is empty."}).encode("utf-8"))
                return

            def normalize_column(name):
                return str(name).strip().lstrip("\ufeff").lower()

            data = pd.read_csv(StringIO(csv_text), skipinitialspace=True)  # Load CSV from text
            data.columns = [normalize_column(col) for col in data.columns]  # Normalize headers

            required_columns = {"date", "sales", "profit"}
            if not required_columns.issubset(set(data.columns)):
                # Try reading again without header (user may have omitted it)
                data = pd.read_csv(StringIO(csv_text), header=None, skipinitialspace=True)

                if data.shape[1] == 3:
                    # If first row looks like a header, drop it
                    first_row = [normalize_column(value) for value in data.iloc[0].tolist()]
                    if first_row == ["date", "sales", "profit"]:
                        data = data.iloc[1:].reset_index(drop=True)
                    data.columns = ["date", "sales", "profit"]
                else:
                    self.send_response(400)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(
                        json.dumps(
                            {
                                "error": "CSV must contain columns: date, sales, profit.",
                                "example": "date,sales,profit\n2025-01-01,1200,300",
                            }
                        ).encode("utf-8")
                    )
                    return

            cleaned = data.dropna()  # Remove rows with missing values
            report = cleaned.describe()  # Create summary statistics

            csv_report = report.to_csv()  # Convert report to CSV text

            self.send_response(200)
            self.send_header("Content-Type", "text/csv")
            self.end_headers()
            self.wfile.write(csv_report.encode("utf-8"))
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Invalid JSON format."}).encode("utf-8"))
        except Exception as error:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(error)}).encode("utf-8"))
