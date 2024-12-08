import streamlit as st
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

st.title('Curasense')

st.info('This is app predicts disease using a machine learning model!')

with st.expander('Data'):
  st.write('**Raw Data**')
  data = pd.read_csv('https://raw.githubusercontent.com/WillsanAJantho/dataset/refs/heads/main/Symptom2Disease.csv')
  data

