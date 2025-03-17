import json
import os
import sys

class FormConfig:
    def __init__(self):
        if not sys.platform == "win32":
            raise SystemError("This application is only supported on Windows")
        
        self.config_file_path = os.path.join(os.environ.get('APPDATA'),
                                    'PDFProcessor',
                                    'form_configs.json')
        
        self.default_configs = {
            "search_request_form": {
                # column_name: [start_marker, end_marker]
                "date_requested": ["Date of request", "Transplant centre"],
                "transplant_centre": ["Transplant centre", "Searches to be run"],
                "Searches to be run": ["Searches to be run", "Time to transplant"],
                "Time to transplant": ["Time to transplant", "Patient type"],
                "Patient type": ["Patient type", "Adults / Paeds"],
                "Adults / Paeds": ["Adults / Paeds", "PATIENT IDENTIFICATION"],
                "First name": ["First name", "Middle Name"],
                "Surname": ["Surname", "Sex at Birth"],
                "Sex at Birth": ["Sex at Birth", "DOB"],
                "DOB (day/month/year)": ["DOB (day/month/year)", "Hospital number"],
                "Hospital number": ["Hospital number", "Diagnosis"],
                "Diagnosis": ["Diagnosis", "Date of Diagnosis"],
                "Date of Diagnosis": ["Date of Diagnosis", "Weight (kg)"],
                "Weight (kg)": ["Weight (kg)", "ABO RhD"],
                "ABO RhD": ["ABO RhD", "CMV Status"],
                "CMV Status": ["CMV Status", "Patient"]
            }
        }

        # Create PDFProcessor folder if it doesn't exist
        os.makedirs(os.path.dirname(self.config_file_path), exist_ok=True)

        # Create config file if it doesn't exist
        if not os.path.exists(self.config_file_path):
            self.create_default_config()

    def create_default_config(self):
        with open(self.config_file_path, 'w') as f:
            json.dump(self.default_configs, f, indent=4)
            
    def get_configs(self):
        with open(self.config_file_path, 'r') as f:
            return json.load(f)

    def add_pdf_form(self, form_name, field_markers):
        """
        Add a new PDF form to the config file.

        Args:
            form_name (str): The name of the form to add.
            field_markers (dict): A dictionary of field markers for the form.
                The keys are the column names in the target csv file, 
                and the values are a tuple of the start and end markers.
        """
        self.default_configs[form_name] = field_markers
        with open(self.config_file_path, 'w') as f:
            json.dump(self.default_configs, f, indent=4)

    def save_new_form(self, form_name, column_marker_dict):
        """Add a new PDF form to the config file.

        Args:
            form_name (str): The name of the form to add
            column_marker_dict (dict): Dictionary mapping column names from target CSV file 
                to start/end markers
                {column_name: [start_marker, end_marker]}
        """
        
        # Validate the new form input for proper formatting
        for column, markers in column_marker_dict.items():
            if not isinstance(markers, list) or len(markers) != 2:
                raise ValueError(f"Start and end markers for column '{column}' must be a list of [start, end]")
        
        # Add new pdf form key to the config
        configs = self.get_configs()
        configs[form_name] = column_marker_dict

        # Update the config file
        with open(self.config_file_path, 'w') as f:
            json.dump(configs, f, indent=4)