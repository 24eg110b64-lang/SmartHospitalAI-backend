from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)

CORS(app)


# =========================
# LOAD ML MODEL
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "ml-model",
    "disease_model.pkl"
)

model = joblib.load(MODEL_PATH)


# =========================
# HOME
# =========================

@app.route("/")
def home():

    return "Smart Hospital AI ML Service is running!"


# =========================
# ML PREDICTION
# =========================

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    symptoms = data.get("symptoms", "").strip().lower()


    if not symptoms:

        return jsonify({
            "error": "Please enter symptoms."
        }), 400


    # ML prediction

    prediction = model.predict([symptoms])[0]


    # Prediction probability

    probabilities = model.predict_proba([symptoms])[0]

    confidence = max(probabilities) * 100


    # =========================
    # SPECIALIST
    # =========================

    specialists = {

        "Respiratory Infection":
            "Pulmonologist",

        "Migraine":
            "Neurologist",

        "Gastric Problem":
            "Gastroenterologist",

        "Skin Condition":
            "Dermatologist",

        "Chest Pain":
            "Cardiologist",

        "Joint Problem":
            "Orthopedic Specialist"

    }


    specialist = specialists.get(
        prediction,
        "General Physician"
    )


    return jsonify({

        "symptoms": symptoms,

        "prediction": prediction,

        "confidence": round(
            confidence,
            2
        ),

        "specialist": specialist

    })


# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":

    # Render / Railway inject PORT at runtime.
    # Fall back to 5000 for local development.
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False          # debug=False in production
    )
