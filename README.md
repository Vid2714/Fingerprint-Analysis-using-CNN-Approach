# Fingerprint Authentication System

This project implements a deep learning model to classify fingerprints as real or altered, along with a user-friendly web interface for easy interaction.

## Project Overview

The system uses a Convolutional Neural Network (CNN) to analyze fingerprint images and determine their authenticity. It can distinguish between real fingerprints and altered ones with various levels of difficulty.

### Key Features

- Deep learning model for fingerprint classification
- Streamlit web application for easy interaction
- Ability to upload and analyze fingerprint images in real-time

## Repository Structure

- `fingerprint_liveness.ipynb`: Script for training the fingerprint classification model
- `app.py`: Streamlit application for deploying the model on a website
- `fingerprint_model.h5`: Saved trained model (not tracked by Git, needs to be generated)

## Usage

### Training the Model

1. Ensure you have the fingerprint dataset in the correct directory.
2. Run the model:
3. The trained model will be saved as `fingerprint_model.h5`.

### Running the Streamlit App

1. Make sure the trained model (`fingerprint_model.h5`) is in the same directory as `app.py`.
2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
3. Open the provided URL in your web browser.
4. Upload a fingerprint image to classify it as real or altered.

## Model Details

- Architecture: Convolutional Neural Network (CNN)
- Input: Grayscale fingerprint images (32x32 pixels)
- Output: Binary classification (Real/Altered)
- Performance metrics available in the training script output

## Future Improvements

- Expand the dataset with more diverse fingerprint samples
- Implement additional preprocessing techniques
- Explore advanced model architectures for improved accuracy
- Ability to identify the different fingers
