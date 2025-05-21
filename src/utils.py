"""
utils.py
--------
General-purpose helper functions: file I/O, formatting, cleaning, etc.
"""

import os
import json
import re


def clean_text(text):
    """
    Removes extra whitespace and non-printable characters.

    Parameters:
        text (str): Raw input text.

    Returns:
        str: Cleaned text.
    """
    return re.sub(r'\s+', ' ', text).strip()


def get_pdf_files(folder_path):
    """
    Get list of all PDF files in a folder.

    Parameters:
        folder_path (str): Directory to scan.

    Returns:
        List[str]: List of full PDF file paths.
    """
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(".pdf")
    ]


def save_json(data, output_path):
    """
    Save a Python dictionary as a JSON file.

    Parameters:
        data (dict): Data to be saved.
        output_path (str): Full path to output file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def pretty_print_json(data):
    """
    Print formatted JSON to the console for readability.

    Parameters:
        data (dict): Dictionary to print.
    """
    print(json.dumps(data, indent=4, ensure_ascii=False))
