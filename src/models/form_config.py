import json
import os
import sys

class FormConfig:
    def __init__(self):
        if sys.platform == "linux":
            # Use XDG_DATA_HOME for data files
            config_dir = os.environ.get('XDG_DATA_HOME', 
                                        os.path.join(os.path.expanduser('~'), '.local', 'share'))
            config_dir = os.path.join(config_dir, 'PDFProcessor')
            self.config_file_path = os.path.join(config_dir, 'form_configs.json')

        elif sys.platform == "win32":
            config_dir = os.path.join(os.environ.get('LOCALAPPDATA'), 'PDFProcessor')
            self.config_file_path = os.path.join(config_dir, 'form_configs.json')
        
        else:
            raise SystemError(f"This application is only supported on windows or linux. You are running on {sys.platform}.")
        
        # Create directory in Linux home
        os.makedirs(config_dir, exist_ok=True)
        
        self.default_configs = {
            "search_request_form": {
                "date_requested": ["Date of request", "Transplant centre"],
                "transplant_centre": ["Transplant centre", "Searches to be run"],
                "searches_to_run": ["Searches to be run", "Time to transplant"],
                "time_to_transplant": ["Time to transplant", "Patient type"],
                "patient_type": ["Patient type", "Adults / Paeds"],
                "age_group": ["Adults / Paeds", "PATIENT IDENTIFICATION"],
                "first_name": ["First name", "Middle Name"],
                "surname": ["Surname", "Sex at Birth"],
                "sex": ["Sex at Birth", "DOB"],
                "dob": ["DOB (day/month/year)", "Hospital number"],
                "hospital_number": ["Hospital number", "Diagnosis"],
                "diagnosis": ["Diagnosis", "Date of Diagnosis"],
                "diagnosis_date": ["Date of Diagnosis", "Weight (kg)"],
                "weight": ["Weight (kg)", "ABO RhD"],
                "blood_type": ["ABO RhD", "CMV Status"],
                "cmv_status": ["CMV Status", "Patient"]
            }
        }

        # Create config file if it doesn't exist
        if not os.path.exists(self.config_file_path):
            self.create_default_config()

    def create_default_config(self):
        with open(self.config_file_path, 'w') as f:
            json.dump(self.default_configs, f, indent=4)
            
    def get_configs(self):
        with open(self.config_file_path, 'r') as f:
            return json.load(f)

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
        
        # Add new pdf form to the configs
        configs = self.get_configs()
        configs[form_name] = column_marker_dict

        # Update the config json file
        with open(self.config_file_path, 'w') as f:
            json.dump(configs, f, indent=4)