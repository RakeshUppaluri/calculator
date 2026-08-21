import streamlit as st

st.title("Calculator Application")

number1 = st.number_input("Insert a number",placeholder="Enter your first number")
number2 = st.number_input("Insert a number",placeholder="Enter your second number")

operation = st.selectbox("Select the operation",("Addition","Subtraction"))

ret=st.button("Calculate")
if ret:
    if operation=="Addition":
        st.write(number1+number2)
    elif operation=="Subtraction":
        st.write(number1-number2)
