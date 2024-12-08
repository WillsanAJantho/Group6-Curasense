import streamlit as st

st.title('Curasense')

st.info('This is app predicts disease using a machine learning model!')

df = pd.read_csv('https://raw.githubusercontent.com/WillsanAJantho/dataset/refs/heads/main/Symptom2Disease.csv')
df
