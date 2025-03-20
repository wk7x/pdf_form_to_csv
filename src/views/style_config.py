import tkinter as tk
from tkinter import ttk

class StyleConfig:
    # Color scheme
    MAIN_BG = '#2E8B57'      # Sea green
    DARK_BG = '#006400'      # Dark green
    ENTRY_BG = '#98FB98'     # Light green
    TEXT_COLOR = 'white'
    
    def __init__(self):
        self.style = ttk.Style()
        self.style.configure('TFrame', background=self.MAIN_BG)
        self.style.configure('TLabel', background=self.MAIN_BG, foreground=self.TEXT_COLOR)
        self.style.configure('TButton', background=self.DARK_BG)
        self.style.configure('Treeview', background=self.ENTRY_BG)
    
    def configure_window(self, window):
        window.configure(bg=self.MAIN_BG)
        
    def configure_button(self, button):
        button.configure(bg=self.DARK_BG, fg=self.TEXT_COLOR)
        
    def configure_entry(self, entry):
        entry.configure(bg=self.ENTRY_BG) 