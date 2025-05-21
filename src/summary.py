"""
summary.py
----------
Generates aggregated summary statistics from page-wise PII results.
"""

from collections import Counter


def generate_summary(pii_result):
    """
    Generate summary from detailed PII detection result.

    Parameters:
        pii_result (dict): Output from detect_all_pii()

    Returns:
        dict: Summary of total PII leaks, type-wise count, page count.
    """
    total_pii_found = 0
    pii_type_counter = Counter()

    for page in pii_result.get("pages", []):
        for pii_type, values in page.get("pii", {}).items():
            count = len(values)
            pii_type_counter[pii_type] += count
            total_pii_found += count

    summary = {
        "total_pages": len(pii_result.get("pages", [])),
        "total_pii_found": total_pii_found,
        "pii_type_counts": dict(pii_type_counter)
    }

    return summary
