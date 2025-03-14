from pdf_extractor import PDFExtractor
from text_processor import TextProcessor
from csv_handler import CSVHandler

def main():
    # PDF path
    pdf_path = "/home/alekseiostlund/pdf_to_csv_appender/testfiles/sampleform.pdf"
    csv_path = "/home/alekseiostlund/pdf_to_csv_appender/testfiles/output.csv"

    # Extract text from PDF
    form_extractor = PDFExtractor(pdf_path)
    extracted_text = form_extractor.extract_text()

    # Process the text
    form_processor = TextProcessor(extracted_text, "search_request_form")
    extracted_data = form_processor.extract_data()

    # Write to CSV
    csv_handler = CSVHandler(extracted_data, csv_path)
    csv_handler.write_to_csv()

if __name__ == "__main__":
    main()
