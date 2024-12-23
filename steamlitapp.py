import streamlit as st

# Define the calculator function
def calculator(operation, a, b):
    if operation == "Add":
        return a + b
    elif operation == "Subtract":
        return a - b
    elif operation == "Multiply":
        return a * b
    elif operation == "Divide":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operation"

# Streamlit app setup
st.title("Demo Calculator")
st.write("Perform basic arithmetic operations.")

# User inputs
operation = st.radio("Select an operation:", ["Add", "Subtract", "Multiply", "Divide"])
a = st.number_input("Enter the first number (Input A):", value=0.0, step=1.0)
b = st.number_input("Enter the second number (Input B):", value=0.0, step=1.0)

# Perform calculation and display the result
if st.button("Calculate"):
    result = calculator(operation, a, b)
    st.success(f"Result: {result}")
