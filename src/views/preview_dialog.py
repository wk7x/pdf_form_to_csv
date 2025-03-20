import tkinter as tk
from tkinter import ttk
from models.csv_handler import CSVHandler

class PreviewDialog(tk.Toplevel):
    def __init__(self, parent, data, csv_path):
        super().__init__(parent)
        self.title("Preview Data")
        self.geometry("600x400")
        self.data = data
        self.csv_path = csv_path
        self._create_widgets()

    def _create_widgets(self):
        # Create Treeview with scrollbar
        tree_frame = ttk.Frame(self)
        tree_frame.pack(padx=10, pady=10, fill='both', expand=True)
        
        self.tree = ttk.Treeview(tree_frame)
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Get headers from data
        headers = list(self.data.keys())
        self.tree["columns"] = headers
        
        # Configure columns
        self.tree.column("#0", width=0, stretch=False)  # Hide first column
        for header in headers:
            self.tree.column(header, width=150, minwidth=100)
            self.tree.heading(header, text=header)
        
        # Add data row
        values = [self.data.get(header, "") for header in headers]
        self.tree.insert("", "end", values=values)
        
        # Pack tree and scrollbar
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)
        
        self.confirm_button = ttk.Button(button_frame, text="Confirm")
        self.confirm_button.pack(side='left', padx=5)
        
        ttk.Button(button_frame, text="Cancel", 
                  command=self.destroy).pack(side='left', padx=5) 