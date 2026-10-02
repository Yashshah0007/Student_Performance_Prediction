
import streamlit as st
from predict import predict_performance

st.title("Student Performance Prediction")
st.write("Enter student details to predict the Performance Index.")

st.subheader("Enter Student Details")

hours = st.number_input(
    "Hours Studied",
    min_value=1,
    max_value=9,
    value=5
)

previous_scores = st.number_input(
    "Previous Scores",
    min_value=40,
    max_value=99,
    value=70
)

extracurricular = st.selectbox(
    "Extracurricular Activities",
    ["No", "Yes"]
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=4,
    max_value=9,
    value=6
)

question_papers = st.number_input(
    "Sample Question Papers Practiced",
    min_value=0,
    max_value=9,
    value=4
)

if extracurricular == "Yes":
    extracurricular = 1
else:
    extracurricular = 0

if st.button("Predict Performance"):
    prediction = predict_performance(
        hours,
        previous_scores,
        extracurricular,
        sleep_hours,
        question_papers
    )

    st.success("Prediction completed!")
    st.metric("Predicted Performance Index", f"{prediction:.2f}")
    st.info(
    "The Performance Index is a predicted score based on the student details provided."
)

