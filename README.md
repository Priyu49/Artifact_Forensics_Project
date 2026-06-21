# 🛡️ Project HeritageShield
**Digital Artifact Forensics & Epigraphy Restoration Pipeline**

## Overview
Project HeritageShield is a dual-core computer vision web application designed to safeguard regional historical artifacts. It provides a unified pipeline to detect hyper-realistic Generative AI forgeries (Midjourney, DALL-E) of architectural sites, while simultaneously offering digital restoration tools to extract and read heavily weathered, authentic stone inscriptions.

## Core Features
### Phase 1: Algorithmic Forgery Detection
* **EXIF Fingerprinting:** Scans hidden metadata for generative software signatures or intentional stripping.
* **Error Level Analysis (ELA):** Maps 8x8 JPEG macroblock compression to detect spliced anomalies.
* **Spatial Variance Telemetry:** Extracts high-frequency spatial noise to calculate physical entropy. Identifies the mathematical smoothing inherent in AI pixel prediction to output an Authenticity Confidence Score.

### Phase 2: Digital Epigraphy Restoration
* **CLAHE Enhancement:** Utilizes Contrast Limited Adaptive Histogram Equalization to boost micro-shadows in shallow carvings.
* **Bilateral Filtering:** Non-linear edge preservation smooths geological erosion without degrading carved groove depth.
* **Adaptive Gaussian Thresholding:** Isolates structural topology to render faded inscriptions as clean, readable documents.

## Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **Computer Vision Math:** OpenCV (`cv2`), NumPy
* **Image Processing:** Pillow (`PIL`)
* **Interface:** HTML/CSS (Jinja2 concepts via FastAPI responses)

## Installation & Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/HeritageShield.git
   cd HeritageShield
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install fastapi uvicorn opencv-python numpy pillow python-multipart
   ```

4. **Ignite the Local Server:**
   ```bash
   uvicorn app:app --reload
   ```

5. **Access the Dashboard:** 
   Open a web browser and navigate to `http://localhost:8000`.

## Generating Reports
Upload an image of a historical artifact or structural site. The system will automatically process the evidence through all forensic modules and generate a comprehensive, printable PDF report containing visual maps and statistical telemetry.
