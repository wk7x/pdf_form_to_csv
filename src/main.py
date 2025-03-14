from pdf_extractor import PDFExtractor
from text_processor import TextProcessor
from csv_handler import CSVHandler
from gui import FormSelectionGUI
import tkinter as tk

def main():
    app = FormSelectionGUI()
    app.run()

if __name__ == "__main__":
    main()
