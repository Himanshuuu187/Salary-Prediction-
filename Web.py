from main import *
import streamlit as st 

st.title("   Salary Prediction ")

Exp = st.number_input("Enter your Years of Experience: ")

res = m*Exp + b

st.success(f"Your Expected Based on your Years of Experience is : {int(res[0][0])}")