import pandas as pd;
import joblib

import streamlit as st;

model = joblib.load('mj')

st.title("house price pred.")

# def prediction(area):
#     predicition = model.predict([[area]])
#     return predicition

st.number_input("Enter the area")


def predicition(area):
    p =model.predict([[area]])
    return p


if(st.button("predict")):
    result = predicition(area)

st.success("Predicted price is {}".format(result))