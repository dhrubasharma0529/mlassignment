import streamlit as st
st.title("BMI CALCULATOR")
def calculate_bmi(weight,height):
    height_in_meter=height * 0.3048
    bmi = weight / (height_in_meter**2)
    return bmi
def give_result(bmi):
    if bmi < 16:
        st.error("Exremely Underweight")
    elif 16 <= bmi < 18.5:
        st.warning("Underweight")
    elif 18.5 <= bmi < 25:
        st.success("Healthy")
    elif 25 <= bmi <30:
        st.info("Overweight")
    else:
        st.error("Extremely overweight")

weight = st.number_input("Enter the weight in kg")
height = st.number_input("Enter the height in feet")
clickedbutton = st.button("Calculate")
if clickedbutton:
    bmi = calculate_bmi(weight,height)
    st.write("your bmi is : ", bmi)
    give_result(bmi)
   