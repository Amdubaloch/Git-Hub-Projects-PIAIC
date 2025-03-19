import streamlit as st


def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in meters."""
    return weight / (height**2)


def get_bmi_category(bmi):
    """Return the BMI category based on the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def bmi_calculator():
    st.title("BMI Calculator")

    # Add input fields
    weight = st.number_input(
        "Enter your weight (kg)", min_value=20.0, max_value=300.0, value=70.0
    )
    height = st.number_input(
        "Enter your height (m)", min_value=0.5, max_value=3.0, value=1.70
    )

    # Calculate BMI when button is pressed
    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)

        # Display results
        st.write(f"Your BMI is: {bmi:.2f}")
        st.write(f"Category: {category}")

        # Add a color-coded indicator
        if category == "Normal weight":
            st.success(f"Your BMI is in the {category} range")
        elif category == "Underweight":
            st.warning(f"Your BMI is in the {category} range")
        else:
            st.error(f"Your BMI is in the {category} range")
