# Program to read a pdf file:
from pypdf import PdfReader
from voice import voice_generate
import os

def read_file(filename):
    reader = PdfReader(f"uploads/{filename}")
    # print(f"Number of Pages: {len(reader.pages)}")
    for page in reader.pages:
        voice_generate(page.extract_text())

    # Removing uploaded file once task is done
    os.remove(f"uploads/{filename}")
