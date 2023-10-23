
import streamlit as st

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Create a Streamlit web app
st.title("Basic Calculator")

# User input for choice
choice = st.selectbox("Select an operation", ["Add", "Subtract", "Multiply", "Divide"])

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

# Calculate based on user choice
if choice == "Add":
    result = add(num1, num2)
elif choice == "Subtract":
    result = subtract(num1, num2)
elif choice == "Multiply":
    result = multiply(num1, num2)
else:
    result = divide(num1, num2)

st.write(f"Result: {result}")
