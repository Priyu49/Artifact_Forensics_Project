import os
from PIL import Image, ImageChops, ImageEnhance

def perform_ela(image_path, quality=90):
    try:
        original = Image.open(image_path).convert('RGB')
        temp_filename = 'temp_compressed_ela.jpg'
        original.save(temp_filename, 'JPEG', quality=quality)
        compressed = Image.open(temp_filename)
        
        ela_image = ImageChops.difference(original, compressed)
        
        extrema = ela_image.getextrema()
        max_diff = max([ex[1] for ex in extrema])
        if max_diff == 0:
            max_diff = 1 
            
        scale = 255.0 / max_diff
        ela_image = ImageEnhance.Brightness(ela_image).enhance(scale)
        os.remove(temp_filename)
        return ela_image

    except Exception as e:
        print(f"Error processing image: {e}")
        return None