import pandas as pd  # Import pandas for easy data handling


def load_data(file_path):
    """Read the CSV file and return a DataFrame."""
    try:
        data = pd.read_csv(file_path)  # Read the CSV file into a DataFrame
        print("Data loaded successfully.")  # Let the user know the load worked
        return data  # Return the loaded data
    except FileNotFoundError:
        print("Error: CSV file not found. Please check the file path.")  # Clear error message
        return None  # Return None so the program can handle the failure
    except Exception as error:
        print(f"Error while loading data: {error}")  # Print any unexpected error
        return None  # Return None to stop further processing


def clean_data(data):
    """Remove rows with missing values."""
    if data is None:
        print("No data to clean.")  # Inform the user there is nothing to clean
        return None  # Return None to signal the failure

    cleaned_data = data.dropna()  # Remove rows that have any missing values
    print("Data cleaned successfully.")  # Confirm cleaning step
    return cleaned_data  # Return the cleaned data


def generate_report(cleaned_data):
    """Create a summary report using describe()."""
    if cleaned_data is None or cleaned_data.empty:
        print("No data available to generate report.")  # Inform the user about missing data
        return None  # Return None to avoid errors

    report = cleaned_data.describe()  # Generate summary statistics for numeric columns
    print("Report generated successfully.")  # Confirm report creation
    return report  # Return the summary report


def main():
    """Control the full automation flow."""
    input_path = "data/sales_data.csv"  # Path to input CSV file
    output_path = "output/summary_report.csv"  # Path to output report file

    data = load_data(input_path)  # Step 1: Load the data
    cleaned_data = clean_data(data)  # Step 2: Clean the data
    report = generate_report(cleaned_data)  # Step 3: Generate the report

    if report is not None:
        try:
            report.to_csv(output_path)  # Save the report as a CSV file
            print(f"Summary report saved to {output_path}.")  # Success message
        except Exception as error:
            print(f"Error while saving report: {error}")  # Show save error


if __name__ == "__main__":
    main()  # Run the program when this file is executed
