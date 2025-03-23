import tkinter as tk
from tkinter import ttk
from models.csv_handler import CSVHandler
from views.style_config import StyleConfig

class BulkPreviewDialog(tk.Toplevel):
    def __init__(self, parent, data_list, csv_path):
        super().__init__(parent)
        self.title("Preview Bulk Data")
        self.geometry("800x600")
        self.data_list = data_list
        self.csv_path = csv_path
        self.style_config = StyleConfig()
        self.style_config.configure_window(self)
        self._create_widgets()

    def _create_widgets(self):
        # Create frame for treeview with both scrollbars
        tree_frame = ttk.Frame(self)
        tree_frame.pack(padx=10, pady=10, fill='both', expand=True)
        
        # Create horizontal and vertical scrollbars
        v_scrollbar = ttk.Scrollbar(tree_frame, orient="vertical")
        h_scrollbar = ttk.Scrollbar(tree_frame, orient="horizontal")
        
        # Create Treeview with both scrollbars
        self.tree = ttk.Treeview(tree_frame, 
                                yscrollcommand=v_scrollbar.set,
                                xscrollcommand=h_scrollbar.set)
        
        # Configure scrollbar commands
        v_scrollbar.config(command=self.tree.yview)
        h_scrollbar.config(command=self.tree.xview)
        
        # Get headers from first data item
        if self.data_list:
            headers = list(self.data_list[0].keys())
            self.tree["columns"] = headers
            
            # Configure columns - make them all same width and allow resize
            self.tree.column("#0", width=0, stretch=False)
            for header in headers:
                self.tree.column(header, width=100, minwidth=50)
                self.tree.heading(header, text=header)
            
            # Add all data rows
            for data in self.data_list:
                values = [data.get(header, "") for header in headers]
                self.tree.insert("", "end", values=values)
        
        # Grid layout for scrollable tree
        self.tree.grid(row=0, column=0, sticky='nsew')
        v_scrollbar.grid(row=0, column=1, sticky='ns')
        h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        # Configure grid weights
        tree_frame.grid_rowconfigure(0, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)
        
        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(pady=10)
        
        self.confirm_button = tk.Button(button_frame, text="Confirm")
        self.style_config.configure_button(self.confirm_button)
        self.confirm_button.pack(side='left', padx=5)
        
        tk.Button(button_frame, text="Cancel", 
                  command=self.destroy).pack(side='left', padx=5) 