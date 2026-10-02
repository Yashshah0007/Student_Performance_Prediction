# Student Performance Prediction System

A machine learning project that predicts a student's Performance Index based on their study and academic-related information.

## Project Overview

The goal of this project is to build a regression model that predicts a student's numerical Performance Index using:

- Hours Studied
- Previous Scores
- Extracurricular Activities
- Sleep Hours
- Sample Question Papers Practiced

The project follows a complete basic machine learning workflow:

Data Collection → Data Cleaning → EDA → Feature Engineering → Train/Test Split → Model Training → Evaluation → Model Saving → Prediction → Streamlit App

## Dataset

The dataset contains information about student study habits and performance.

Original dataset:
- 10,000 rows
- 6 columns

After removing duplicate rows:
- 9,873 rows

The target variable is:

`Performance Index`

The `Extracurricular Activities` column was converted from:

- Yes → 1
- No → 0

## Machine Learning Models

Two regression models were trained and compared:

1. Linear Regression
2. Random Forest Regression

### Model Comparison

| Model | MAE | MSE | RMSE | R² |
|---|---:|---:|---:|---:|
| Linear Regression | 1.6470 | 4.3059 | 2.0751 | 0.9884 |
| Random Forest | 1.8988 | 5.6290 | 2.3726 | 0.9849 |

For this dataset and test split, Linear Regression produced the lower error values and higher R², so it was selected as the final saved model.

## Final Model

The trained Linear Regression model was saved using `joblib`:

`student_performance_model.pkl`

The model can then be loaded and used to make predictions for new students.

## Streamlit Application

A simple Streamlit web application was created to allow users to enter student information and receive a predicted Performance Index.

The application takes:

- Hours Studied
- Previous Scores
- Extracurricular Activities
- Sleep Hours
- Sample Question Papers Practiced

and displays the predicted Performance Index.

## Project Structure

```text
Student_Performance_Prediction/
│
├── data/
│   └── Student_Performance.csv
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── student_performance_model.pkl
├── predict.py
├── app.py
├── requirements.txt
└── README.md