import streamlit as st

st.title("Calculator Application")

number1 = st.number_input("Insert a number",placeholder="Enter your first number")
number2 = st.number_input("Insert a number",placeholder="Enter your second number")

operation = st.selectbox("Select the operation",("Addition","Subtraction","Multiplication","Division"))

ret=st.button("Calculate")
if ret:
    if operation=="Addition":
        st.write(number1+number2)
    elif operation=="Subtraction":
        st.write(number1-number2)
    elif operation=="Multiplication":
        st.write(number1*number2)
    elif operation=="Division":
        if number2!=0:
            st.write(number1/number2)
        else:
            st.write("division is not possible")
