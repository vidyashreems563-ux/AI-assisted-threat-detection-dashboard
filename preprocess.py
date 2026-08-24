import pandas as pd

print("=" * 60)
print("AI-Assisted Threat Detection Dashboard")
print("Security Data Preprocessing")
print("=" * 60)

# Load Dataset
df = pd.read_csv("dataset/security_logs.csv")

print("\n✅ Dataset Loaded Successfully!")

# Dataset Information
print("\nDataset Shape:", df.shape)

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df = df.fillna("Unknown")

# Convert Timestamp to datetime
if "Timestamp" in df.columns:
    df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()
# Normalize text columns
text_columns = [
    "Protocol",
    "Traffic_Type",
    "Threat_Type",
    "Severity",
    "Action_Taken",
    "Attack_Signature",
    "Malware_Indicator",
    "Alert",
    "Device_OS"
]

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.title()

print("✅ Text normalization completed.")
# -----------------------------
# Threat Intelligence Mapping (MITRE ATT&CK)
# -----------------------------
mitre_mapping = {
    "Brute Force": "T1110",
    "Phishing": "T1566",
    "Malware": "T1204",
    "Ransomware": "T1486",
    "Suspicious Login": "T1078"
}

if "Threat_Type" in df.columns:
    df["MITRE_ATT&CK"] = df["Threat_Type"].map(mitre_mapping)
    df["MITRE_ATT&CK"] = df["MITRE_ATT&CK"].fillna("Unknown")

print("✅ MITRE ATT&CK mapping completed.")
df.to_csv("dataset/cleaned_security_logs.csv", index=False)

# Save cleaned dataset
df.to_csv("dataset/cleaned_security_logs.csv", index=False)

print("\n✅ Data preprocessing completed successfully!")
print("✅ Cleaned dataset saved as dataset/cleaned_security_logs.csv")

print("\nFinal Dataset Shape:", df.shape)