import streamlit as st
import requests

st.set_page_config(page_title="MNIST Digit Images", page_icon=":pencil2:")


st.title('MNIST Digit Images')
img = st.file_uploader('Upload an image', type=['png', 'jpg'])

if img is not None:
    st.write('Uploaded Image:')
    st.image(img, width=300)
    files = {'file': img.getvalue()}
    # Paste the URL of your deployed model here
    resp = requests.post("paste-url-here", files=files)
    prediction = (resp.json().get('prediction'))
    st.header(f'Prediction: {prediction}')