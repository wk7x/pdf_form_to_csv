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
            "Date of request": ("Date of request", "Transplant centre"),
            "Transplant centre": ("Transplant centre", "Searches to be run"),
            "Searches to be run": ("Searches to be run", "Time to transplant"),
            "Time to transplant": ("Time to transplant", "Patient type"),
            "Patient type": ("Patient type", "Adults / Paeds"),
            "Adults / Paeds": ("Adults / Paeds", "PATIENT IDENTIFICATION"),
            "First name": ("First name", "Middle Name"),
            "Surname": ("Surname", "Sex at Birth"),
            "Sex at Birth": ("Sex at Birth", "DOB"),
            "DOB (day/month/year)": ("DOB (day/month/year)", "Hospital number"),
            "Hospital number": ("Hospital number", "Diagnosis"),
            "Diagnosis": ("Diagnosis", "Date of Diagnosis"),
            "Date of Diagnosis": ("Date of Diagnosis", "Weight (kg)"),
            "Weight (kg)": ("Weight (kg)", "ABO RhD"),
            "ABO RhD": ("ABO RhD", "CMV Status"),
            "CMV Status": ("CMV Status", "Patient")
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
                The keys are the field names, and the values are the field markers.
        """
        self.default_configs[form_name] = field_markers
        with open(self.config_file_path, 'w') as f:
            json.dump(self.default_configs, f, indent=4)
            