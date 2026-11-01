import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


# ==========================================
# TRAINING DATA
# ==========================================

data = {

    "symptoms": [

        # -------------------------
        # FEVER
        # -------------------------

        "fever",
        "high fever",
        "mild fever",
        "body temperature high",
        "fever and chills",
        "feeling feverish",
        "temperature is high",
        "hot body fever",
        "fever for two days",
        "fever with weakness",
        "fever without cough",
        "fever without cold",

        # -------------------------
        # RESPIRATORY INFECTION
        # -------------------------

        "fever cough",
        "fever and cough",
        "high fever cough",
        "cough cold",
        "cough and cold",
        "runny nose cough",
        "dry cough",
        "wet cough",
        "cough with mucus",
        "sore throat cough",
        "cold cough sore throat",
        "cough chest congestion",
        "breathing problem cough",
        "cough fever sore throat",

        # -------------------------
        # MIGRAINE
        # -------------------------

        "headache",
        "severe headache",
        "migraine",
        "severe migraine",
        "throbbing headache",
        "head pain",
        "headache with nausea",
        "headache and nausea",
        "headache sensitivity to light",
        "head pain sensitivity to light",
        "severe head pain",
        "headache with vomiting",

        # -------------------------
        # GASTRIC PROBLEM
        # -------------------------

        "stomach pain",
        "stomach ache",
        "gastric problem",
        "acidity",
        "stomach acidity",
        "abdominal pain",
        "stomach burning",
        "burning stomach",
        "gas problem",
        "stomach gas",
        "indigestion",
        "indigestion stomach pain",
        "acid reflux",
        "abdominal discomfort",

        # -------------------------
        # SKIN CONDITION
        # -------------------------

        "skin rash",
        "rash",
        "itchy skin",
        "skin itching",
        "red skin",
        "skin redness",
        "skin irritation",
        "red rash",
        "itching and rash",
        "red itchy skin",
        "skin allergy",
        "skin allergy rash",
        "rash and itching",
        "skin spots",

        # -------------------------
        # CHEST PAIN
        # -------------------------

        "chest pain",
        "chest discomfort",
        "chest pressure",
        "pressure in chest",
        "chest tightness",
        "pain in chest",
        "chest pain and pressure",
        "chest pain breathing difficulty",
        "chest pain while breathing",
        "chest heaviness",
        "pain near chest",
        "chest pain with breathing",

        # -------------------------
        # JOINT PROBLEM
        # -------------------------

        "joint pain",
        "joint swelling",
        "joint stiffness",
        "knee pain",
        "knee swelling",
        "pain in joints",
        "body joint pain",
        "joint pain and swelling",
        "knee joint pain",
        "shoulder joint pain",
        "ankle joint pain",
        "joint discomfort",
        "joint pain while walking",
        "swollen joints"
    ],


    "disease": [

        # FEVER
        "Fever",
        "Fever",
        "Fever",
        "Fever",
        "Fever",
        "Fever",
        "Fever",
        "Fever",
        "Fever",
        "Fever",
        "Fever",
        "Fever",

        # RESPIRATORY INFECTION
        "Respiratory Infection",
        "Respiratory Infection",
        "Respiratory Infection",
        "Respiratory Infection",
        "Respiratory Infection",
        "Respiratory Infection",
        "Respiratory Infection",
        "Respiratory Infection",
        "Respiratory Infection",
        "Respiratory Infection",
        "Respiratory Infection",
        "Respiratory Infection",
        "Respiratory Infection",
        "Respiratory Infection",

        # MIGRAINE
        "Migraine",
        "Migraine",
        "Migraine",
        "Migraine",
        "Migraine",
        "Migraine",
        "Migraine",
        "Migraine",
        "Migraine",
        "Migraine",
        "Migraine",
        "Migraine",

        # GASTRIC
        "Gastric Problem",
        "Gastric Problem",
        "Gastric Problem",
        "Gastric Problem",
        "Gastric Problem",
        "Gastric Problem",
        "Gastric Problem",
        "Gastric Problem",
        "Gastric Problem",
        "Gastric Problem",
        "Gastric Problem",
        "Gastric Problem",
        "Gastric Problem",
        "Gastric Problem",

        # SKIN
        "Skin Condition",
        "Skin Condition",
        "Skin Condition",
        "Skin Condition",
        "Skin Condition",
        "Skin Condition",
        "Skin Condition",
        "Skin Condition",
        "Skin Condition",
        "Skin Condition",
        "Skin Condition",
        "Skin Condition",
        "Skin Condition",
        "Skin Condition",

        # CHEST PAIN
        "Chest Pain",
        "Chest Pain",
        "Chest Pain",
        "Chest Pain",
        "Chest Pain",
        "Chest Pain",
        "Chest Pain",
        "Chest Pain",
        "Chest Pain",
        "Chest Pain",
        "Chest Pain",
        "Chest Pain",

        # JOINT
        "Joint Problem",
        "Joint Problem",
        "Joint Problem",
        "Joint Problem",
        "Joint Problem",
        "Joint Problem",
        "Joint Problem",
        "Joint Problem",
        "Joint Problem",
        "Joint Problem",
        "Joint Problem",
        "Joint Problem",
        "Joint Problem",
        "Joint Problem"
    ]
}


# ==========================================
# CREATE DATAFRAME
# ==========================================

df = pd.DataFrame(data)

X = df["symptoms"]
y = df["disease"]


print("Total training samples:", len(df))
print("Disease classes:", y.nunique())


# ==========================================
# TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.25,

    random_state=42,

    stratify=y
)


# ==========================================
# MACHINE LEARNING PIPELINE
# ==========================================

model = Pipeline([

    (
        "tfidf",

        TfidfVectorizer(

            lowercase=True,

            ngram_range=(1, 2),

            sublinear_tf=True
        )
    ),

    (
        "classifier",

        LogisticRegression(

            max_iter=3000,

            C=2.0
        )
    )
])


# ==========================================
# TRAIN MODEL
# ==========================================

print("\nTraining model...")

model.fit(
    X_train,
    y_train
)


# ==========================================
# MODEL TESTING
# ==========================================

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)


print(
    "\nModel Accuracy:",
    round(accuracy * 100, 2),
    "%"
)


# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(
    model,
    "disease_model.pkl"
)


print("\nModel saved successfully!")
print("File: disease_model.pkl")