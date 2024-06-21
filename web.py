import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('my web app')


# a = st.text_input('name')

df = pd.read_csv('a.csv')
# st.dataframe(df)
fig = plt.figure()
plt.plot(df)
st.pypot(fig)