import streamlit as st
import pandas as pd


st.sidebar.title("Esta es una prueba")
st.sidebar.header("Hola esto es una barra lateral")
st.sidebar.write("Barra lateral ")

st.sidebar.image("madrir.png")

if st.sidebar.button("Clik en la barra lateral "):
    st.sidebar.write("Hice un boton lateral ")
user_input = st.sidebar.text_input("escribe algo en la barra ") # esto hace que el usuario ingrese palabra y aparezcan en la barra lateral 
st.sidebar.write("Escribiste en la barra:  ", user_input)
st.title("Esta es mi primera pagina")
st.header("MI primera página")
st.image("madrir.png")
