"""
PII Detection Module
--------------------
Detects personally identifiable information (PII) such as names, emails, phone numbers, etc.
"""

import re
import spacy
from src.constants.regex_patterns import (
    DOB_PATTERNS,
    AADHAAR_PATTERN,
    PHONE_PATTERN,
    PAN_PATTERN,
    EMAIL_PATTERN,
    IP_PATTERN,
    BANK_PATTERNS
)

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")


def detect_all_pii(text_pages):
    """
    Detects PII across all pages and returns results by page.
    """
    results = {"pages": []}

    for page_num, text in enumerate(text_pages, start=1):
        page_result = {
            "page": page_num,
            "pii": {
                "name": detect_names(text),
                "dob": detect_dobs(text),
                "aadhaar": detect_aadhaar(text),
                "phone": detect_phones(text),
                "pan": detect_pan(text),
                "email": detect_emails(text),
                "address": detect_addresses(text),
                "ip": detect_ip_addresses(text),
                "bank": detect_bank_details(text)
            }
        }
        results["pages"].append(page_result)

    return results


def detect_names(text):
    doc = nlp(text)
    return list({ent.text.strip() for ent in doc.ents if ent.label_ == "PERSON"})


def detect_dobs(text):
    return extract_with_patterns(text, DOB_PATTERNS)


def detect_aadhaar(text):
    return extract_with_patterns(text, [AADHAAR_PATTERN])


def detect_phones(text):
    return extract_with_patterns(text, [PHONE_PATTERN])


def detect_pan(text):
    return extract_with_patterns(text, [PAN_PATTERN])


def detect_emails(text):
    return extract_with_patterns(text, [EMAIL_PATTERN])


def detect_addresses(text):
    doc = nlp(text)
    return list({
        ent.text.strip()
        for ent in doc.ents
        if ent.label_ in ("GPE", "LOC", "ADDRESS")
    })


def detect_ip_addresses(text):
    return extract_with_patterns(text, [IP_PATTERN])


def detect_bank_details(text):
    return extract_with_patterns(text, BANK_PATTERNS)


def extract_with_patterns(text, patterns):
    matches = set()
    for pattern in patterns:
        matches.update(re.findall(pattern, text))
    return list(matches)
