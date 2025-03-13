import pypdf


pdf_path = "/home/alekseiostlund/pdf_to_csv_appender/testfiles/sampleform.pdf"
class PDFExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.pdf_reader = pypdf.PdfReader(pdf_path)

    def extract_text(self):
        text = ""
        for page in self.pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    
form_extractor = PDFExtractor(pdf_path)
print(form_extractor.extract_text())