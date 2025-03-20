import csv
import os

class CSVHandler:
    def __init__(self, extracted_data, csv_path):
        self.extracted_data = extracted_data
        self.csv_path = csv_path

    def get_headers(self):
        with open(self.csv_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
        return headers
    
    def write_to_csv(self):
        # Check if file exists and has something written to it
        file_exists = os.path.exists(self.csv_path) and os.path.getsize(self.csv_path) > 0

        with open(self.csv_path, "a") as f:
            writer = csv.writer(f)
            
            # Only write headers if file doesn't exist or is empty
            if not file_exists and isinstance(self.extracted_data, dict):
                writer.writerow(list(self.extracted_data.keys()))
            
            # Handle both single dict and list of dicts
            if isinstance(self.extracted_data, dict):
                writer.writerow(list(self.extracted_data.values()))
            elif isinstance(self.extracted_data, list):
                # For bulk processing, write each row
                for data in self.extracted_data:
                    writer.writerow(list(data.values())) 