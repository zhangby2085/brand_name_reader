import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_brand_name(image):
    # Convert the image to a numpy array
    image_array = np.array(image)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    
    # Apply thresholding to preprocess the image
    threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Perform text extraction
    text = pytesseract.image_to_string(threshold)
    
    # Split the text into words
    words = text.split()
    
    # Simple brand extraction (you might want to improve this part)
    # For this example, we'll assume the brand is the first word in all caps
    for word in words:
        if word.isupper() and len(word) > 1:
            return word
    
    return "No brand detected"

def add_brand_name_to_image(image, brand_name):
    # Convert the image to a numpy array
    image_array = np.array(image)
    
    # Convert the image to BGR color space (OpenCV uses BGR)
    image_bgr = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    
    # Get the image dimensions
    height, width, _ = image_bgr.shape
    
    # Define the font and text properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    color = (0, 0, 255)  # Red color in BGR format
    thickness = 2
    
    # Calculate the text size
    text_size, _ = cv2.getTextSize(brand_name, font, font_scale, thickness)
    
    # Calculate the position to center the text
    text_x = (width - text_size[0]) // 2
    text_y = (height + text_size[1]) // 2
    
    # Add the brand name text to the image
    cv2.putText(image_bgr, brand_name, (text_x, text_y), font, font_scale, color, thickness)
    
    # Convert the image back to RGB color space
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    
    return Image.fromarray(image_rgb)

def main():
    st.title("Brand Name Extractor")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
        if st.button('Extract Brand Name'):
            brand = extract_brand_name(image)
            st.write(f"Detected brand: {brand}")
            
            # Add the brand name to the image and display the new image
            new_image = add_brand_name_to_image(image, brand)
            st.image(new_image, caption='Image with Brand Name', use_column_width=True)

if __name__ == "__main__":
    main()