import pypdf

class PDFExtractor:
    def __init__(self, pdf_path):
        self.pdf_reader = pypdf.PdfReader(pdf_path)

    def extract_text(self):
        text = ""
        for page in self.pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text