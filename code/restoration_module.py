import cv2
import numpy as np
from PIL import Image

def restore_epigraphy(image_path):
    """
    Phase 2: High-Accuracy Epigraphy Extraction using CLAHE and Adaptive Thresholding.
    """
    try:
        # 1. Load image and convert to Grayscale
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 2. CLAHE (Contrast Limited Adaptive Histogram Equalization)
        # This is the secret weapon. It boosts the contrast of the shallow, faded 
        # carvings by analyzing local micro-grids rather than the whole image lighting.
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        enhanced_contrast = clahe.apply(gray)

        # 3. Gentle Bilateral Filter
        # Smooths the flat rock grit but strictly preserves the newly enhanced edges.
        # Lowered the 'd' value to 9 so it isn't destructive to shallow carvings.
        bilateral = cv2.bilateralFilter(enhanced_contrast, d=9, sigmaColor=75, sigmaSpace=75)

        # 4. Adaptive Gaussian Thresholding (Replacing Canny)
        # Instead of just tracing thin edges, this isolates the darker "valleys"
        # (the carved lines) from the lighter stone surface, adapting to shadows.
        thresh = cv2.adaptiveThreshold(
            bilateral, 255, 
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY_INV, 
            blockSize=35, # Looks at a 35x35 pixel neighborhood
            C=5 # Subtracts 5 to filter out shallow surface scratches
        )

        # 5. Morphological Cleanup (Denoising)
        # Removes tiny microscopic speckles (salt and pepper noise) left on the stone
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        clean_text = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        # 6. Invert for Document Style (Black text on White background)
        final_output = cv2.bitwise_not(clean_text)

        return Image.fromarray(final_output)

    except Exception as e:
        print(f"Error in Restoration Analysis: {e}")
        return None
import cv2
import numpy as np
from PIL import Image

def restore_epigraphy(image_path):
    """
    Phase 2: Filters out geological stone weathering while isolating 
    and extracting faded human-carved inscriptions.
    """
    try:
        # 1. Load image and convert to Grayscale
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 2. The Bilateral Filter (The Magic Step)
        # Smooths the rock surface (sigmaSpace) but preserves the deep grooves (sigmaColor)
        bilateral = cv2.bilateralFilter(gray, d=15, sigmaColor=80, sigmaSpace=80)

        # 3. Gaussian Blur
        # A lightweight pass to remove any remaining microscopic grit before edge detection
        gaussian = cv2.GaussianBlur(bilateral, (5, 5), 0)

        # 4. Dynamic Canny Edge Detection
        # Calculates the median pixel intensity to automatically set the perfect thresholds 
        # for tracing the carved letters, regardless of lighting conditions.
        v = np.median(gaussian)
        lower = int(max(0, (1.0 - 0.33) * v))
        upper = int(min(255, (1.0 + 0.33) * v))
        edges = cv2.Canny(gaussian, lower, upper)

        # 5. Morphological Closing
        # Connects tiny breaks in the traced lines so the letters look solid
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

        # 6. Invert the image (Black text on a white background, like a printed document)
        inverted_result = cv2.bitwise_not(closed_edges)

        # Convert back to PIL format so the web server can display it
        final_image = Image.fromarray(inverted_result)
        return final_image

    except Exception as e:
        print(f"Error in Restoration Analysis: {e}")
        return None