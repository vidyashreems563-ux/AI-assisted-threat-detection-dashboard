import pandas as pd
import numpy as np

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

print("=" * 60)
print("AI-Assisted Threat Detection Dashboard")
print("AI-Based Threat Detection Engine")
print("=" * 60)

# Load cleaned dataset
df = pd.read_csv("dataset/cleaned_security_logs.csv")

print("\n✅ Cleaned dataset loaded successfully!")

# Select features
features = [
    "Protocol",
    "Traffic_Type",
    "Malware_Indicator",
    "Alert",
    "Threat_Type",
    "Attack_Signature",
    "Severity",
    "Anomaly_Score"
]

data = df[features].copy()

# Encode categorical columns
label_encoder = LabelEncoder()

for col in data.columns:
    if data[col].dtype == "object":
        data[col] = label_encoder.fit_transform(data[col].astype(str))

print("✅ Feature encoding completed.")
# Train Isolation Forest Model
model = IsolationForest(
    n_estimators=100,
    contamination=0.1,
    random_state=42
)

model.fit(data)

print("✅ Isolation Forest model trained successfully!")
predictions = model.predict(data)

df["Prediction"] = predictions

df["Prediction"] = df["Prediction"].replace({
    -1: "Anomaly",
     1: "Normal"
})

print("✅ Anomaly detection completed!")
# -----------------------------
# Generate Confidence Score
# -----------------------------
scores = model.decision_function(data)

# Convert scores to percentage
confidence = (scores - scores.min()) / (scores.max() - scores.min()) * 100

df["Confidence_Score"] = confidence.round(2)

print("✅ Confidence scores generated!")
# -----------------------------
# Incident Severity Classification
# -----------------------------
def classify(confidence):
    if confidence >= 75:
        return "Low"
    elif confidence >= 40:
        return "Medium"
    else:
        return "High"

df["Incident_Severity"] = df["Confidence_Score"].apply(classify)

print("✅ Incident severity classification completed!")
# -----------------------------
# Save Prediction Results
# -----------------------------
df.to_csv("dataset/predicted_security_logs.csv", index=False)

print("\n✅ Prediction results saved successfully!")
print("✅ File saved: dataset/predicted_security_logs.csv")

print("\nFinal Dataset Shape:", df.shape)