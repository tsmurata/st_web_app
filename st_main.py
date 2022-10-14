import streamlit as st
from PIL import Image

st.title('muアプリ')
st.caption('これはmuアプリです')

# 画像
image = Image.open('./data/cat.jpg')
st.image(image, width=300)

