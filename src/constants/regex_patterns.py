"""
Regex patterns for various PII types.
"""

# Date of Birth formats: 01-01-1990 or 1990/01/01
DOB_PATTERNS = [
    r"\b\d{2}[/-]\d{2}[/-]\d{4}\b",
    r"\b\d{4}[/-]\d{2}[/-]\d{2}\b"
]

# Aadhaar Number: 1234 5678 9012
AADHAAR_PATTERN = r"\b\d{4}\s\d{4}\s\d{4}\b"

# Indian Mobile Phone Number
PHONE_PATTERN = r"\b[6-9]\d{9}\b"

# PAN Number: ABCDE1234F
PAN_PATTERN = r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"

# Email Address
EMAIL_PATTERN = r"\b[\w\.-]+@[\w\.-]+\.\w+\b"

# IPv4 Address
IP_PATTERN = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

# Bank Details: account, IFSC, MICR
BANK_PATTERNS = [
    r"\b\d{9,18}\b",                         # Generic account number
    r"IFSC[:\s]*[A-Z]{4}0[A-Z0-9]{6}",       # IFSC code
    r"MICR[:\s]*\d{9}"                       # MICR code
]
