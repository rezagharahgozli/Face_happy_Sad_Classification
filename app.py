import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# load model
model = load_model("models/HappySadModel.h5")

st.title("Happy or Not Happy Detection")
st.image('images/happysad.jpg', caption="Happy Sad Detection")
st.write("Upload an image and the model will predict whether the person is happy or not.")

# upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png","bmp"])

def preprocess_image(image, target_size=(256, 256)):
    image = image.resize(target_size)
    image = np.array(image)


    if len(image.shape) == 2:
        image = np.stack([image] * 3, axis=-1)

    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    processed_image = preprocess_image(image, target_size=(256, 256))

    prediction = model.predict(processed_image)[0][0]

    st.write(f"Prediction score: {prediction:.4f}")

    if prediction >= 0.5:
        st.success("Result: Happy")
    else:
        st.error("Result: Sad")