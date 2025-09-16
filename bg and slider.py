import streamlit as st
from datetime import time,datetime
import base64

# fungsi untuk convert gambar jadi base64
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ubah gambar lokal jadi base64
img_base64 = get_img_as_base64("bahlil.jpg")

# CSS buat set background dengan gambar
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

[data-testid="stSidebar"] {{
    background-color: rgba(0,0,0,0.6);
    color: white;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Belajar agar tidak jadi bahlil kontol memek jembod bahlil ")
st.header("st.slider")

hate_score = st.slider('Seberapa benci anda dengan Bahlil?', 0, 100, 50)
st.write('Aku benci Bahlil sebesar',hate_score,'persen')

st.subheader("Range Slider")

values = st.slider('Berapa persen keinginan anda untuk menendang wajah bahlil?',0.0,100.0,(25.0,75.0))
st.write("Aku ingin menendang wajah bahlil",values,'persen')

st.subheader('Range Time Slider')
appointment = st.slider(
    "Berapa lama anda ingin menendang muka bahlil?",
    value=(time(11,30),time(12,45)))
st.write("Saya ingin menendang wajah bahlil dari pukul:",appointment)

st.subheader('Datetime Slider')
start_time = st.slider(
    "Kapan kamu mau mulai menendang bahlil?",
    value=datetime(2020,1,1,9,30),
    format="MM/DD/YY - hh:mm")
st.write("Saya ingin menendang wajah bahlil pada:",start_time)
