# PDF Form to CSV File Converter

A Python application that extracts data from standardized PDF forms and appends it to a CSV file. The application supports both single file and bulk processing through a graphical user interface.

## Features

- GUI interface for easy file selection and processing
- Support for single PDF or bulk folder processing
- Form type verification to ensure correct data extraction
- Automatic CSV header management
- Progress logging in GUI
- Checkbox field support

## Dependencies

- pypdf (5.3.1)
- tkinter

## Notes

- CSV files are appended to, not overwritten
- Headers are only added if the CSV file is new/empty
- Form verification ensures all required fields are present and that the form type is supported by the text processor
- Invalid forms don't stop bulk processing