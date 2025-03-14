import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pdf_extractor import PDFExtractor
from text_processor import TextProcessor
from csv_handler import CSVHandler

class FormSelectionGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Form Selection")
        self.root.geometry("400x400")  # Made window taller for message area

        # Input PDF file selection
        self.input_label = tk.Label(self.root, text="Input PDF:")
        self.input_label.pack(pady=5)
        
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill=tk.X, padx=5)
        
        self.input_path = tk.Entry(self.input_frame)
        self.input_path.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.input_button = tk.Button(self.input_frame, text="Browse", command=self.browse_input)
        self.input_button.pack(side=tk.RIGHT)

        # Output CSV file selection
        self.output_label = tk.Label(self.root, text="Output CSV:")
        self.output_label.pack(pady=5)
        
        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(fill=tk.X, padx=5)
        
        self.output_path = tk.Entry(self.output_frame)
        self.output_path.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.output_button = tk.Button(self.output_frame, text="Browse", command=self.browse_output)
        self.output_button.pack(side=tk.RIGHT)

        # Form type selection
        self.type_label = tk.Label(self.root, text="Form Type:")
        self.type_label.pack(pady=5)
        
        self.form_type = ttk.Combobox(self.root, values=["search_request_form", ])
        self.form_type.pack(pady=5)
        self.form_type.set("")

        # Add message area
        self.message_label = tk.Label(self.root, text="Messages:")
        self.message_label.pack(pady=5)
        
        self.message_area = tk.Text(self.root, height=8, width=45)
        self.message_area.pack(pady=5, padx=5)

        # Process button
        self.process_button = tk.Button(self.root, text="Process Form", command=self.process_form)
        self.process_button.pack(pady=5)

    def browse_input(self):
        filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if filename:
            self.input_path.delete(0, tk.END)
            self.input_path.insert(0, filename)

    def browse_output(self):
        filename = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")],
            title="Select CSV file to append to"
        )
        if filename:
            self.output_path.delete(0, tk.END)
            self.output_path.insert(0, filename)

    def log_message(self, message):
        """Add message to text area and scroll to end"""
        self.message_area.insert(tk.END, message + '\n')
        self.message_area.see(tk.END)  # Scroll to bottom

    def process_form(self):
        input_file = self.input_path.get()
        output_file = self.output_path.get()
        form_type = self.form_type.get()
        
        if not input_file or not output_file or not form_type:
            self.log_message("Error: Please fill in all fields")
            return
            
        try:
            self.log_message(f"Processing {input_file}")
            self.log_message(f"Output to: {output_file}")
            self.log_message(f"Form type: {form_type}")
            
            # PROCESSING CODE
            # extract text from pdf
            form_extractor = PDFExtractor(input_file)
            extracted_text = form_extractor.extract_text()

            # process text
            form_processor = TextProcessor(extracted_text, form_type)
            processed_text = form_processor.extract_data()

            # write to csv
            csv_handler = CSVHandler(processed_text, output_file)
            csv_handler.write_to_csv()
            
            
            self.log_message("Success: File information was appended to the CSV file.")
            
        except Exception as e:
            self.log_message(f"Error: {str(e)}")

    def run(self):
        self.root.mainloop()