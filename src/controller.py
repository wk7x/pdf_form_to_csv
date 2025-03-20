import os
import tkinter as tk
from tkinter import filedialog, messagebox
from views.main_window import MainWindow
from views.new_form_dialog import NewFormDialog
from models.form_config import FormConfig
from models.pdf_extractor import PDFExtractor
from models.text_processor import TextProcessor
from models.csv_handler import CSVHandler
from views.preview_dialog import PreviewDialog
from views.bulk_preview_dialog import BulkPreviewDialog

class FormController:
    def __init__(self):
        self.view = MainWindow()
        
        self.form_config = FormConfig()
        
        self._bind_events()
        
        self._update_form_list()

    def _bind_events(self):
        self.view.add_form_button.config(command=self._show_new_form)
        self.view.delete_form_button.config(command=self._delete_form)
        self.view.process_button.config(command=self._process_form)
        self.view.input_button.config(command=self._browse_input)
        self.view.bulk_button.config(command=self._browse_folder)
        self.view.output_button.config(command=self._browse_output)

    def _update_form_list(self):
        forms = self.form_config.get_configs()
        self.view.form_type['values'] = list(forms.keys())

    def _show_new_form(self):
        dialog = NewFormDialog(self.view)
        dialog.save_button.config(command=lambda: self._save_new_form(dialog))

    def _save_new_form(self, dialog):
        form_name = dialog.name_entry.get().strip()
        if not form_name:
            messagebox.showerror("Error", "Please enter a form name")
            return

        configs = {}
        for col_entry, marker_entry in dialog.column_entries:
            col_name = col_entry.get().strip()
            markers = marker_entry.get().strip().split(',')
            if col_name and len(markers) == 2:
                configs[col_name] = [m.strip() for m in markers]

        if not configs:
            messagebox.showerror("Error", "Please add at least one valid column")
            return

        try:
            self.form_config.save_new_form(form_name, configs)
            self._update_form_list()
            dialog.destroy()
            messagebox.showinfo("Success", "Form saved successfully")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _process_form(self):
        input_path = self.view.input_path.get()
        output_path = self.view.output_path.get()
        form_type = self.view.form_type.get()
        
        if not all([input_path, output_path, form_type]):
            self.view.log_message("Error: Please fill in all fields")
            return
            
        try:
            if os.path.isdir(input_path):
                self._process_folder(input_path, output_path, form_type)
            else:
                self._process_file(input_path, output_path, form_type)
        except Exception as e:
            self.view.log_message(f"Error: {str(e)}")

    def _process_file(self, input_path, output_path, form_type):
        extractor = PDFExtractor(input_path)
        extracted_text = extractor.extract_text()

        processor = TextProcessor(extracted_text, form_type)
        processed_text = processor.extract_data()

        # Show preview before saving
        self._show_preview(processed_text, output_path)

    def _process_folder(self, folder_path, output_path, form_type):
        pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
        if not pdf_files:
            self.view.log_message("Error: No PDF files in the folder")
            return

        self.view.log_message(f"Processing {len(pdf_files)} files")
        
        # Process each file and collect data
        all_data = []
        for pdf_file in pdf_files:
            try:
                extractor = PDFExtractor(os.path.join(folder_path, pdf_file))
                extracted_text = extractor.extract_text()
                processor = TextProcessor(extracted_text, form_type)
                processed_text = processor.extract_data()
                all_data.append(processed_text)
            except Exception as e:
                self.view.log_message(f"Error processing {pdf_file}: {str(e)}")
        
        # Create the preview dialog and pass the data
        if all_data:
            preview = BulkPreviewDialog(self.view, all_data, output_path)
            preview.confirm_button.config(
                command=lambda: self._save_bulk_to_csv(preview, all_data, output_path)
            )

    def _browse_input(self):
        filename = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if filename:
            self.view.input_path.delete(0, tk.END)
            self.view.input_path.insert(0, filename)
            self.view.log_message(f"Selected file: {filename}")

    def _browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.view.input_path.delete(0, tk.END)
            self.view.input_path.insert(0, folder)
            self.view.log_message(f"Selected folder: {folder}")

    def _browse_output(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Select or Create CSV File"
        )
        if filename:
            self.view.output_path.delete(0, tk.END)
            self.view.output_path.insert(0, filename)

    def _show_preview(self, data, output_path):
        preview = PreviewDialog(self.view, data, output_path)
        preview.confirm_button.config(
            command=lambda: self._save_to_csv(preview, data, output_path)
        )

    def _save_to_csv(self, preview_window, data, output_path):
        csv_handler = CSVHandler(data, output_path)
        csv_handler.write_to_csv()
        preview_window.destroy()
        self.view.log_message("1 row appended to CSV file successfully.")

    def _save_bulk_to_csv(self, preview_window, data_list, output_path):
        csv_handler = CSVHandler(data_list, output_path)
        csv_handler.write_to_csv()
        preview_window.destroy()
        self.view.log_message(f"{len(data_list)} rows appended to CSV file successfully.")

    def _delete_form(self):
        form_type = self.view.form_type.get()
        if not form_type:
            messagebox.showerror("Error", "Please select a form to delete")
            return
        
        # Ask for confirmation
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the form '{form_type}'?"):
            try:
                self.form_config.delete_form(form_type)
                self._update_form_list()
                self.view.form_type.set('')  # Clear the selection
                messagebox.showinfo("Success", f"Form '{form_type}' deleted successfully")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def run(self):
        self.view.mainloop() 