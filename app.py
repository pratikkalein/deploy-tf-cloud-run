import streamlit as st
import requests

st.set_page_config(page_title="MNIST Digit Images", page_icon=":pencil2:")


st.title('MNIST Digit Images')
img = st.file_uploader('Upload an image', type=['png', 'jpg'])

if img is not None:
    st.write('Uploaded Image:')
    st.image(img, width=300)
    files = {'file': img.getvalue()}
    resp = requests.post("http://127.0.0.1:5000", files=files)
    prediction = (resp.json().get('prediction'))
    st.header(f'Prediction: {prediction}')