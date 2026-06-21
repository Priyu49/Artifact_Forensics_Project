import os
from PIL import Image
from code.ela_module import perform_ela 
from code.metadata_module import extract_metadata

test_img_path = "test_photo.jpg" 

print(f"\n{'='*40}")
print(f"🕵️  FORENSIC ANALYSIS REPORT: {test_img_path}")
print(f"{'='*40}\n")

# --- PHASE 1: METADATA EXTRACTION ---
print("--- PHASE 1: Scanning Digital Fingerprint ---")
metadata_report = extract_metadata(test_img_path)

print(f"Status: {metadata_report.get('Status')}")
if metadata_report.get('Total_Tags_Found'):
    print(f"Tags Analyzed: {metadata_report.get('Total_Tags_Found')}")
if metadata_report.get('Suspicious_Tags'):
    print("Anomalies Found:")
    for tag in metadata_report.get('Suspicious_Tags'):
        print(f"  -> {tag}")
print("\n")


# --- PHASE 2: VISUAL ANOMALY DETECTION ---
print("--- PHASE 2: Running Error Level Analysis ---")
result_image = perform_ela(test_img_path)

if result_image:
    result_path = "real_ela_result.jpg"
    result_image.save(result_path)
    print(f"SUCCESS: Visual compression map saved as -> {result_path}")
else:
    print("ERROR: ELA Engine failed to process the image.")

print(f"\n{'='*40}")
print("ANALYSIS COMPLETE.")
print(f"{'='*40}\n")