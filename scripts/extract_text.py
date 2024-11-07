from pdf2image import convert_from_path
import pytesseract
import json
import os

RAW_PDF_DIR = 'data/raw_pdfs/'
PROCESSED_TEXT_DIR = 'data/processed_texts/'

def pdf_to_text(pdf_path):
    text_data = ""
    pages = convert_from_path(pdf_path)
    for page in pages:
        text = pytesseract.image_to_string(page)
        text_data += text + "\n"
    return text_data

def save_text_data(filename, text_data):
    with open(f"{PROCESSED_TEXT_DIR}/{filename}.json", "w") as json_file:
        json.dump({"text": text_data}, json_file)

def process_all_pdfs():
    if not os.path.exists(PROCESSED_TEXT_DIR):
        os.makedirs(PROCESSED_TEXT_DIR)

    for pdf_file in os.listdir(RAW_PDF_DIR):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(RAW_PDF_DIR, pdf_file)
            text_data = pdf_to_text(pdf_path)
            save_text_data(pdf_file.replace('.pdf', ''), text_data)

if __name__ == "__main__":
    process_all_pdfs()
