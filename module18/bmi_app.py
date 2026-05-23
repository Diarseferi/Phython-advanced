# bmi_app.py

import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚖️",
    layout="centered"
)

st.title("⚖️ BMI Calculator")
st.write("Calculate your Body Mass Index (BMI)")

# User inputs
weight = st.number_input(
    "Enter your weight (kg)",
    min_value=1.0,
    max_value=500.0,
    value=70.0,
    step=0.1
)

height = st.number_input(
    "Enter your height (cm)",
    min_value=50.0,
    max_value=300.0,
    value=170.0,
    step=0.1
)

# BMI Calculation
if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.subheader(f"Your BMI is: {bmi:.2f}")

    # BMI Categories
    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        color = "green"
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "orange"
    else:
        category = "Obese"
        color = "red"

    st.markdown(
        f"<h3 style='color:{color};'>Category: {category}</h3>",
        unsafe_allow_html=True
    )

    # Progress bar visualization
    progress = min(int((bmi / 40) * 100), 100)
    st.progress(progress)

# BMI Info
st.markdown("---")
st.markdown("### BMI Categories")
st.write("""
- Underweight: BMI less than 18.5
- Normal weight: BMI 18.5 – 24.9
- Overweight: BMI 25 – 29.9
- Obese: BMI 30 or greater
""")