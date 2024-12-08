import streamlit as st
import pandas as pd

st.title('Curasense')

st.info('This is app predicts disease using a machine learning model!')

with st.expander('Data'):
st.write('**Raw Data**')
df = pd.read_csv('https://raw.githubusercontent.com/WillsanAJantho/dataset/refs/heads/main/Symptom2Disease.csv')
df
