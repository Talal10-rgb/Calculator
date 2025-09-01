import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon="🧮")

st.title("🧮 Simple Calculator")

# User input fields
num1 = st.number_input("Enter first number", format="%.2f")
num2 = st.number_input("Enter second number", format="%.2f")

operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation."

    st.success(f"Result: {result}")
