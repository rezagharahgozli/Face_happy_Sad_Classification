# **Happy vs Sad Image Classifier**

A web application built with Streamlit and TensorFlow/Keras that predicts whether a person in an image is happy or not.

### Overview

This project allows users to upload an image and receive a prediction based on a trained deep learning model. The model analyzes the image and outputs a score indicating the likelihood of a happy expression.

### Model
Framework: TensorFlow / Keras
Model file: models/HappySadModel.h5
Output:
Score >= 0.5 → Happy
Score < 0.5 → Sad

### Installation

Install the required dependencies:

pip install streamlit tensorflow pillow numpy
### Running the Application
streamlit run app.py
### How It Works
The user uploads an image
The image is resized to 256×256
Pixel values are normalized to the range [0, 1]
The processed image is passed to the model
The model outputs a prediction score
### Example Output
Prediction score: 0.82
Result: Happy
### Important Notes
The input image size must match the model input (256×256)
If your model was trained with a different size, update the preprocessing step accordingly
The model expects RGB images
### Future Improvements
Add probability visualization
Support multiple face detection
Improve model accuracy with a larger dataset
Deploy the application online
### Author

Mohammadreza Gharahgozlee
Python Developer | Data Analyst | Machine Learning
GitHub: https://github.com/rezagharahgozli