import streamlit as st
from datetime import datetime
import ast

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state["history"] = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Navigation menu
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Calculator", "History", "Text Input Calculator"])

if page == "Calculator":
    # Calculator page
    st.title("Simple Calculator - Made by AI")

    operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

    num1 = st.number_input("Enter first number:", format="%.2f")
    num2 = st.number_input("Enter second number:", format="%.2f")

    if st.button("Calculate"):
        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)

        # Save to history
        st.session_state["history"].append({
            "operation": operation,
            "num1": num1,
            "num2": num2,
            "result": result,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        st.write(f"The result is: {result}")

elif page == "History":
    # History page
    st.title("Calculation History")

    if st.session_state["history"]:
        for entry in reversed(st.session_state["history"]):
            if entry["operation"] == "Text Input":
                st.write(f"[{entry['timestamp']}] {entry['expression']} = {entry['result']}")
            else:
                st.write(f"[{entry['timestamp']}] {entry['num1']} {entry['operation']} {entry['num2']} = {entry['result']}")
    else:
        st.write("No history available.")

elif page == "Text Input Calculator":
    # Text Input Calculator page
    st.title("Text Input Calculator")

    expression = st.text_input("Enter a mathematical expression (e.g., 2 + 2 * 3):")

    if st.button("Evaluate"):
        try:
            # Safely evaluate the expression
            result = eval(expression, {"__builtins__": None}, {})

            # Save to history
            st.session_state["history"].append({
                "operation": "Text Input",
                "expression": expression,
                "result": result,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            st.write(f"The result is: {result}")
        except Exception as e:
            st.write(f"Error: {e}")