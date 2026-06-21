# Metadata Module
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(image_path):
    """
    Scans the image's internal EXIF data for known AI signatures 
    or signs of metadata stripping.
    """
    try:
        img = Image.open(image_path)
        exif_data = img.getexif()
        
        # This dictionary will hold our final report
        report = {
            "Status": "Clean",
            "Suspicious_Tags": [],
            "Total_Tags_Found": 0
        }
        
        # Social media and some AI generators strip metadata entirely
        if not exif_data:
            report["Status"] = "WARNING: No EXIF Data Found (Possible strip/sanitization)"
            return report

        # A list of common fingerprints left by generative models
        ai_signatures = ["midjourney", "dall-e", "stable diffusion", "adobe firefly", "ai generated"]

        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            value_str = str(value).lower()
            report["Total_Tags_Found"] += 1
            
            # Cross-reference the data with our known AI signatures
            for sig in ai_signatures:
                if sig in value_str:
                    report["Status"] = "CRITICAL: AI Signature Detected!"
                    report["Suspicious_Tags"].append(f"{tag_name}: {value}")
                    
        return report

    except Exception as e:
        return {"Error": f"Could not read metadata: {e}"}