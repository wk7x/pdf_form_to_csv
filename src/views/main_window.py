import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Form Selection")
        self.geometry("400x400")
        self._create_widgets()

    def _create_widgets(self):
        # Input section
        self._create_input_section()
        # Output section
        self._create_output_section()
        # Form type section
        self._create_form_section()
        # Message section
        self._create_message_section()

    def _create_input_section(self):
        tk.Label(self, text="Input PDF:").pack(pady=5)
        
        input_frame = tk.Frame(self)
        input_frame.pack(fill=tk.X, padx=5)
        
        self.input_path = tk.Entry(input_frame)
        self.input_path.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.bulk_button = tk.Button(input_frame, text="Select Folder")
        self.bulk_button.pack(side=tk.RIGHT, padx=5)
        
        self.input_button = tk.Button(input_frame, text="Select File")
        self.input_button.pack(side=tk.RIGHT)

    def _create_output_section(self):
        tk.Label(self, text="Output CSV:").pack(pady=5)
        
        output_frame = tk.Frame(self)
        output_frame.pack(fill=tk.X, padx=5)
        
        self.output_path = tk.Entry(output_frame)
        self.output_path.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.output_button = tk.Button(output_frame, text="Browse")
        self.output_button.pack(side=tk.RIGHT)

    def _create_form_section(self):
        tk.Label(self, text="Form Type:").pack(pady=5)
        self.form_type = ttk.Combobox(self)
        self.form_type.pack(pady=5)
        
        self.add_form_button = tk.Button(self, text="Add New Form")
        self.add_form_button.pack(pady=5)

    def _create_message_section(self):
        tk.Label(self, text="Messages:").pack(pady=5)
        self.message_area = tk.Text(self, height=8, width=45)
        self.message_area.pack(pady=5, padx=5)
        
        self.process_button = tk.Button(self, text="Process Form")
        self.process_button.pack(pady=5)

    def log_message(self, message):
        self.message_area.insert(tk.END, message + '\n')
        self.message_area.see(tk.END) 