from PyPDF2 import PdfReader

class TextExtractor:
    @staticmethod
    def extract_text_from_pdf(pdf_path):
        """Extrahiert Text aus PDF-Datei"""
        with open(pdf_path, "rb") as f:
            reader = PdfReader(f)
            return "\n".join([page.extract_text() for page in reader.pages])