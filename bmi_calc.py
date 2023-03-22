import streamlit as st

st.title("BMI Calculator")

mass = st.number_input("What is your mass(kg): ", step = 0.1)
height = st.number_input("What is your height(m): ", step = 0.01)

button = st.button("Calculate BMI")
if button:
  BMI = mass/height**2
  st.success(f"Your BMI is {BMI}%.2f")
