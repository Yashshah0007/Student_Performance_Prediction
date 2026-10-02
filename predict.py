import joblib
import pandas as pd

model = joblib.load("student_performance_model.pkl")


def predict_performance(hours, previous_scores, extracurricular,
                        sleep_hours, question_papers):

    new_student = pd.DataFrame([{
        "Hours Studied": hours,
        "Previous Scores": previous_scores,
        "Extracurricular Activities": extracurricular,
        "Sleep Hours": sleep_hours,
        "Sample Question Papers Practiced": question_papers
    }])

    return model.predict(new_student)[0]