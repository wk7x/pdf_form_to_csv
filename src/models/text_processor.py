from models.form_config import FormConfig

class TextProcessor:
    
    def __init__(self, text, form_type, normalize_spacing=True):
        self.text = text
        self.form_type = form_type
        self.form_configs = FormConfig()
        self.configs = self.form_configs.get_configs()
        self.fields = list(self.configs[form_type].keys())
        self.extracted_data = {}
        if normalize_spacing:
            self.normalize_spacing()

    def normalize_spacing(self):
        self.text = ' '.join(self.text.split())

    def verify_form_type(self):
        if self.form_type not in self.configs:
            raise ValueError(f"Invalid form type: {self.form_type}")
        
        fieldcount = len(self.fields)
        fieldsfound = 0
        for field in self.fields:
            if field in self.text:
                fieldsfound += 1
        if fieldsfound != fieldcount:
            raise ValueError(f"Required fields not found in the form")

    def extract_data(self):
        self.verify_form_type()

        # Get the form markers for the form type
        form_markers = self.configs[self.form_type]
        
        for column_name, [start_word, end_word] in form_markers.items():
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
            self.extracted_data[column_name] = extracted_data
        return self.extracted_data
    