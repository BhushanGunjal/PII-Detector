"""
reader.py
---------
Handles extraction of text from PDF documents using PyMuPDF.
"""

import fitz  # PyMuPDF


def extract_text_from_pdf(file_path):
    """
    Extract text from all pages of a PDF.

    Parameters:
        file_path (str): Path to the PDF file.

    Returns:
        List[str]: List of text content from each page.
    """
    doc = fitz.open(file_path)
    text_by_page = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_text = page.get_text()
        text_by_page.append(page_text)

    return text_by_page
