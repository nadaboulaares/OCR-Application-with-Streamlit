import os
import numpy as np
import easyocr
from PIL import Image
import streamlit as st

# Set the TESSDATA_PREFIX environment variable
os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata'

# Function to convert images to JPEG format
def convert_to_jpg(image_path):
    # Open the image using PIL (Python Imaging Library)
    image = Image.open(image_path)

    # Convert the image to JPEG format
    image_jpg_path = os.path.splitext(image_path)[0] + '.jpg'
    image.save(image_jpg_path, 'JPEG')

    return image_jpg_path

# Function to perform OCR on the scanned document images
def perform_ocr(image_path):
    # Convert image to JPEG format
    image_path = convert_to_jpg(image_path)

    # Open the image using PIL (Python Imaging Library)
    image = Image.open(image_path)

    # Convert PIL image to numpy array
    image_np = np.array(image)

    # Perform OCR using EasyOCR
    reader = easyocr.Reader(['ar'])  # Specify Arabic as the language
    result = reader.readtext(image_np)

    # Extract text from the OCR result
    extracted_text = ' '.join([text[1] for text in result])

    return extracted_text

# Function to preprocess the extracted text
def preprocess_text(text):
    # Implement any necessary preprocessing steps here
    # For simplicity, we'll skip preprocessing in this example.
    return text

# Function to extract key features from the preprocessed text
def extract_features(text):
    # Implement feature extraction here
    # For simplicity, we'll skip feature extraction in this example.
    return {"Type de Document": "Contrat", "Dates": "12 février 2022", "Parties Impliquées": ["A", "B"],
            "Termes Clés": ["Contrat", "Allégations"], "Éléments d'Action": "Dates d'audience"}

# Function to process a single image
def process_image(image_path):
    # Perform OCR on the image
    extracted_text = perform_ocr(image_path)

    # Preprocess the extracted text
    preprocessed_text = preprocess_text(extracted_text)

    # Extract features from the preprocessed text
    extracted_features = extract_features(preprocessed_text)

    # Display the results
    st.write("## Extracted Text from", image_path)
    st.write(extracted_text)
    st.write("## Extracted Features from", image_path)
    st.write(extracted_features)

# Main function
def main():
    st.title("OCR App")

    # Upload image file
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "webp"])

    if uploaded_file is not None:
        # Perform OCR and display results
        process_image(uploaded_file)

if __name__ == "__main__":
    main()
