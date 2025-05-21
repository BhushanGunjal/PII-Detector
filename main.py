from src.reader import extract_text_from_pdf
from src.detectors import detect_all_pii
from src.summary import generate_summary
from src.utils import save_json, pretty_print_json

# File location
PDF_PATH = "files/sample.pdf"
OUTPUT_PATH = "output/sample_pii.json"

# Step 1: Extract text from PDF
text_pages = extract_text_from_pdf(PDF_PATH)

# Step 2: Detect PII
pii_results = detect_all_pii(text_pages)

# Step 3: Generate Summary
summary_data = generate_summary(pii_results)

# Step 4: Combine output
output_data = {
    "summary": summary_data,
    "pages": pii_results["pages"]
}

# Step 5: Save to JSON
save_json(output_data, OUTPUT_PATH)

# Optional: Pretty print to console
pretty_print_json(output_data)

print(f"\n✅ PII detection complete. Results saved to {OUTPUT_PATH}")
