import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from PIL import Image
import io

# Load the model (ensure the path is correct)
model = tf.keras.models.load_model('fingerprint_model.h5')

# Set image size (should match your model's input size)
img_size = 32

def preprocess_image(image):
    # Convert to grayscale
    img_array = np.array(image)
    # Resize
    img_resize = cv2.resize(img_array, (img_size, img_size))
    # Normalize
    img_normalized = img_resize / 255.0
    return img_normalized.reshape(-1, img_size, img_size, 1)

st.title('Fingerprint Authenticity Checker')

st.write("""
Upload a fingerprint image to check if it's real or altered.
""")

uploaded_file = st.file_uploader("Choose a fingerprint image...")
if uploaded_file is not None:
    try:
        file_contents = uploaded_file.read()
        st.write(f"Successfully read {len(file_contents)} bytes")
    except Exception as e:
        st.write(f"Error reading file: {e}")
        
if uploaded_file is not None:
    st.write(f"File received: {uploaded_file.name}")
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Fingerprint.', width=200)
    st.write("")
    st.write("Classifying...")

    # Preprocess the image
    processed_image = preprocess_image(image)

    # Make prediction
    prediction = model.predict(processed_image)

    # Interpret the prediction
    class_names = ['Altered', 'Real']
    predicted_class = class_names[np.argmax(prediction[0])]
    confidence = np.max(prediction)

    st.write(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence:.2f}")

    # Display a bar chart of the prediction
    st.bar_chart(prediction[0],width=300)

st.write("""
Note: This app uses a deep learning model to classify fingerprints. 
While it strives for accuracy, it may not be 100% reliable and should not be used as the sole method for fingerprint verification in critical applications.
""")