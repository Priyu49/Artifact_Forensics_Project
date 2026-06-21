# Noise Module
import cv2
import numpy as np
from PIL import Image

def analyze_noise(image_path):
    """
    Isolates the high-frequency noise/texture of an image using a median filter.
    Highlights flat, AI-smoothed patches in dark colors and real texture in bright colors.
    """
    try:
        # 1. Load the image using OpenCV
        img = cv2.imread(image_path)
        
        # 2. Convert to Grayscale (we only care about texture, not color)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 3. Apply a mathematical blur to smooth out the image
        # This acts as a "Low-Pass Filter"
        blurred = cv2.medianBlur(gray, 5)

        # 4. Subtract the blurred image from the original
        # This strips away the building/shapes and leaves ONLY the microscopic noise
        noise = cv2.absdiff(gray, blurred)

        # 5. Enhance the noise so the human eye can see the pattern
        noise_normalized = cv2.normalize(noise, None, 0, 255, cv2.NORM_MINMAX)

        # 6. Apply an "Inferno" heatmap so flat areas look dark, and noisy areas look bright
        noise_colored = cv2.applyColorMap(noise_normalized, cv2.COLORMAP_INFERNO)

        # 7. Convert back to a standard format to save
        noise_rgb = cv2.cvtColor(noise_colored, cv2.COLOR_BGR2RGB)
        final_image = Image.fromarray(noise_rgb)

        return final_image
        
    except Exception as e:
        print(f"Error in Noise Analysis: {e}")
        return None