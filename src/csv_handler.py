import csv

class CSVHandler:
    def __init__(self, extracted_data, csv_path):
        self.extracted_data = extracted_data
        self.csv_path = csv_path

    def write_to_csv(self):
        with open(self.csv_path, "a") as f:
            writer = csv.writer(f)
            writer.writerow(list(self.extracted_data.keys()))
            writer.writerow(list(self.extracted_data.values())) 