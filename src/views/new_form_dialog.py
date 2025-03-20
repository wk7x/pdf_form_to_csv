import tkinter as tk

class NewFormDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add New PDF Form")
        self.geometry("600x400")
        self.column_entries = []
        self._create_widgets()
        self.add_column_row()

    def _create_widgets(self):
        # Name section
        name_frame = tk.Frame(self)
        name_frame.pack(pady=5)

        name_label = tk.Label(name_frame, text="PDF Form Name:")
        name_label.pack(side=tk.LEFT)
        self.name_entry = tk.Entry(name_frame)
        self.name_entry.pack(side=tk.LEFT)

        # Columns frame
        self.columns_frame = tk.Frame(self)
        self.columns_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Headers
        headers_frame = tk.Frame(self.columns_frame)
        headers_frame.pack(fill=tk.X)
        tk.Label(headers_frame, text="Column Name", width=20).pack(side=tk.LEFT, padx=5)
        tk.Label(headers_frame, text="Start,End Markers", width=40).pack(side=tk.LEFT, padx=5)

        # Add Column button
        tk.Button(self, text="Add Column", command=self.add_column_row).pack(pady=5)

        # Save/cancel frame
        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)
        self.save_button = tk.Button(button_frame, text="Save")  # Command will be set by controller
        self.save_button.pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", command=self.destroy).pack(side=tk.LEFT, padx=5)

    def add_column_row(self):
        row_frame = tk.Frame(self.columns_frame)
        row_frame.pack(pady=2)

        # Column name entry
        column_entry = tk.Entry(row_frame, width=20)
        column_entry.pack(side=tk.LEFT, padx=5)

        # Markers entry
        markers_entry = tk.Entry(row_frame, width=40)
        markers_entry.pack(side=tk.LEFT, padx=5)

        # Remove button
        remove_btn = tk.Button(row_frame, text="X", 
                             command=lambda: self.remove_row(row_frame, column_entry, markers_entry))
        remove_btn.pack(side=tk.LEFT)

        # Store the entries
        self.column_entries.append((column_entry, markers_entry))

    def remove_row(self, row_frame, col_entry, marker_entry):
        self.column_entries.remove((col_entry, marker_entry))
        row_frame.destroy() 