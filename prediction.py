# prediction.py

import os
import joblib
import numpy as np


# ===============================
# Safe Model Loading (Absolute Path)
# ===============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "saved_models")

def load_model(model_name):
    model_path = os.path.join(MODEL_DIR, model_name)

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    return joblib.load(model_path)


# Load models safely
# Load models safely (correct filenames)

diabetes_model = load_model("diabetes_model.pkl")
heart_model = load_model("heart.pkl")
kidney_model = load_model("kidney.pkl")





# ===============================
# Feature Importance
# ===============================

def get_feature_importance(disease):

    if disease == "Diabetes":
        model = diabetes_model
        features = [
            "Pregnancies", "Glucose", "BloodPressure",
            "SkinThickness", "Insulin", "BMI",
            "DiabetesPedigreeFunction", "Age"
        ]

    elif disease == "Heart Disease":
        model = heart_model
        features = ["Systolic", "Cholesterol", "Diastolic", "MaxHeartRate"]

    else:
        model = kidney_model
        features = ["Creatinine", "Urea", "RandomGlucose", "BP_Systolic", "BP_Diastolic"]

    importances = model.feature_importances_

    return features, importances
# ===============================
# Prediction Logic
# ===============================

def run_prediction_logic(disease, vals):

    notes = {}

    if disease == "Diabetes":
        input_data = np.array([[
            vals["Pregnancies"],
            vals["Glucose"],
            vals["BloodPressure"],
            vals["SkinThickness"],
            vals["Insulin"],
            vals["BMI"],
            vals["DiabetesPedigreeFunction"],
            vals["Age"]
        ]])
        model = diabetes_model

    elif disease == "Heart Disease":
        input_data = np.array([[
            vals["systolic"],
            vals["chol"],
            vals["thalach"]
        ]])
        model = heart_model

    else:  # Kidney Disease
        input_data = np.array([[
        vals["creatinine"],
        vals["urea"],
        vals["bgr"],
        vals["bp_systolic"]
    ]])
        model = kidney_model

    # ------------------------------
    # Prediction
    # ------------------------------
    prediction = model.predict(input_data)

    # Some models may not support predict_proba
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_data)
        risk_score = round(probability[0][1] * 100, 2)
    else:
        # Fallback
        risk_score = 50.0

    # Risk Category
    if risk_score <= 30:
        risk_category = "Low Risk"
    elif risk_score <= 60:
        risk_category = "Moderate Risk"
    else:
        risk_category = "High Risk"

    result = "Positive" if prediction[0] == 1 else "Normal"

    return result, risk_score, risk_category, notes

 # agar tum joblib use kar rahe ho

import joblib
import numpy as np

def quick_predict_from_symptoms(disease, age):

    if disease == "Heart Disease":
        model = joblib.load("saved_models/heart.pkl")

        input_data = np.array([[
            age, 1, 0, 120, 200, 0, 1, 150, 0, 1.0, 1, 0, 2
        ]])

    elif disease == "Diabetes":
        model = joblib.load("saved_models/diabetes.pkl")

        input_data = np.array([[
            1, 120, 70, 20, 80, 25.0, 0.5, age
        ]])

    elif disease == "Kidney Disease":
        model = joblib.load("saved_models/kidney.pkl")

        input_data = np.array([[
            age, 1.0, 30, 100, 120
        ]])

    else:
        return "Unknown", 0, "Low Risk"

    prediction = model.predict(input_data)[0]

    try:
        prob = model.predict_proba(input_data)[0][1]
    except:
        prob = 0.5

    risk_score = int(prob * 100)

    if risk_score > 60:
        risk_category = "High Risk"
    elif risk_score > 30:
        risk_category = "Moderate Risk"
    else:
        risk_category = "Low Risk"

    result = "Disease Detected" if prediction == 1 else "No Disease Detected"

    return result, risk_score, risk_category