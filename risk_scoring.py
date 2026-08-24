import pandas as pd

print("=" * 60)
print("AI-Assisted Threat Detection Dashboard")
print("Risk Prioritization & Security Intelligence")
print("=" * 60)
# Load prediction results
df = pd.read_csv("dataset/predicted_security_logs.csv")

# Load Threat Intelligence Feed
threat_feed = pd.read_csv("dataset/threat_feed.csv")

print("\n✅ Prediction dataset loaded successfully!")
print("✅ Threat Intelligence Feed loaded successfully!")
# -----------------------------
# Risk Scoring Algorithm
# -----------------------------
def calculate_risk(row):

    score = 0

    # 1. AI Prediction (30 Marks)
    if row["Prediction"] == "Anomaly":
        score += 30

    # 2. Confidence Score (20 Marks)
    confidence = row["Confidence_Score"]

    if confidence < 40:
        score += 20
    elif confidence < 70:
        score += 10

    # 3. Severity (20 Marks)
    severity = str(row["Severity"]).lower()

    if severity == "high":
        score += 20
    elif severity == "medium":
        score += 10

    # 4. Anomaly Score (20 Marks)
    anomaly = row["Anomaly_Score"]

    if anomaly >= 80:
        score += 20
    elif anomaly >= 50:
        score += 10

    # 5. Threat Type (10 Marks)
    threat = str(row["Threat_Type"]).lower()

    high_threats = [
        "malware",
        "ransomware",
        "phishing",
        "brute force"
    ]

    if threat in high_threats:
        score += 10

    return score

df["Risk_Score"] = df.apply(calculate_risk, axis=1)

print("✅ Risk scores generated.")
# -----------------------------
# Threat Priority Classification
# -----------------------------
def priority(score):

    if score >= 80:
        return "Critical"

    elif score >= 60:
        return "High"

    elif score >= 40:
        return "Medium"

    else:
        return "Low"

df["Threat_Priority"] = df["Risk_Score"].apply(priority)

print("✅ Threat prioritization completed.")
# -----------------------------
# Response Recommendation
# -----------------------------
def recommendation(priority):

    if priority == "Critical":
        return "Immediately isolate the affected system and notify the SOC team."

    elif priority == "High":
        return "Investigate immediately and block suspicious activity."

    elif priority == "Medium":
        return "Monitor the activity and perform a detailed security review."

    else:
        return "Continue monitoring. No immediate action required."

df["Recommendation"] = df["Threat_Priority"].apply(recommendation)

print("✅ Response recommendations generated.")
# -----------------------------
# Event Correlation
# -----------------------------
df["Correlated_Event"] = (
    df["Threat_Type"].astype(str) + " | " +
    df["Attack_Signature"].astype(str) + " | " +
    df["Alert"].astype(str)
)

print("✅ Threat event correlation completed.")
# -----------------------------
# Validation Summary
# -----------------------------
print("\nValidation Summary")

print("Normal Events :", (df["Prediction"] == "Normal").sum())
print("Anomaly Events:", (df["Prediction"] == "Anomaly").sum())

print("\nThreat Priority Distribution")
print(df["Threat_Priority"].value_counts())
# -----------------------------
# Merge Threat Intelligence Feed
# -----------------------------
df = df.merge(
    threat_feed,
    on="Threat_Type",
    how="left"
)

print("✅ Threat Intelligence integrated successfully!")
# -----------------------------
# Save Final Dataset
# -----------------------------
df.to_csv("dataset/final_security_logs.csv", index=False)

print("\n✅ Final security intelligence dataset saved successfully!")
print("✅ File: dataset/final_security_logs.csv")

print("\nFinal Dataset Shape:", df.shape)