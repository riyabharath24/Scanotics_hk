import streamlit as st
import cv
from PIL import Image
import numpy as numpy
from tensorflow.keras.preprocessing.img import img_to_array, load_img
from tensorflow.keras.models import load_model
import tensorflow
from tensorflow import keras
import os


def img_pred(img, weights_file):

    model = tf.keras.load_model(weights_file)

    opencvImage = cv.cvtColor(np.array(img), cv.COLOR_RGB2BGR)
    img = cv.resize(opencvImage, (244, 244))
    img = img.reshape(1, 244, 244, 3)
    p = model.predict(img)
    p = np.argmax(p, axis=1)[0]

    return p


st.title("Tumor Detection-MRI Scans")
st.header("Upload your image to scan here: ")


uploaded_img = st.file_uploader("Upload your image here...")

if uploaded_img is not None():
    img = Image.open(uploaded_img)
    st.image(img, caption="Uploaded scan image", use_column_width=True)

    st.write("Diagnosing...")

    st.write("")
    label = img_pred(img, 'mri_classifier_model.h5')
    if label == 0:
        print('\tTumor Detected- Consult a doctor immediately')
    else:
        print('\tNo tumor detected- You are healthy!')


for name, file_info in uploader.value.items():
    img3 = Image.open(io.BytesIO(file_info['content']))
    img3.show(title=None, command=None)
    plt.imshow(img3)


button = widgets.Button(description='Predict')
out = widgets.Output()


def on_button_clicked(_):
    img_pred(uploader)


button.on_click(on_button_clicked)
widgets.VBox([button, out])
