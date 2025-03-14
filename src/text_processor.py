class TextProcessor:
    #add class attribute that keeps track of the field markers in each form
    field_markers = {
        "search_request_form": {
            "Date of request": "Transplant centre",
            "Transplant centre": "Searches to be run",
            "Searches to be run": "Time to transplant",
            "Time to transplant": "Patient type",
            "Patient type": "Adults / Paeds",
            "Adults / Paeds": "PATIENT IDENTIFICATION",
            "First name": "Middle Name",
            "Surname": "Sex at Birth",
            "Sex at Birth": "DOB",
            "DOB (day/month/year)": "Hospital number",
            "Hospital number": "Diagnosis",
            "Diagnosis": "Date of Diagnosis",
            "Date of Diagnosis": "Weight (kg)",
            "Weight (kg)": "ABO RhD",
            "ABO RhD": "CMV Status",
            "CMV Status": "Patient"
            }
        }
    
    def __init__(self, text, form_type, normalize_spacing=True):
        self.text = text
        self.form_type = form_type
        self.extracted_data = {}
        if normalize_spacing:
            self.normalize_spacing()

    def normalize_spacing(self):
        self.text = ' '.join(self.text.split())

    def extract_data(self):
        for start_word, end_word in self.field_markers[self.form_type].items():
            start_idx = self.text.index(start_word) + len(start_word)
            end_idx = self.text.index(end_word)
            extracted_data = self.text[start_idx:end_idx].strip()
            # check to see if the field is a checkbox field
            if "☒" in extracted_data:
                # get all text to the right of the checked box
                extracted_data = extracted_data.split("☒")[1].strip()
                # remove leading spaces only
                extracted_data = extracted_data.lstrip()
                # split on spaces and take the first element
                extracted_data = extracted_data.split(" ")[0]
            # if no checkbox is filled out set the data to an empty string
            elif "☐" in extracted_data:
                extracted_data = ""
            self.extracted_data[start_word] = extracted_data
        return self.extracted_data
