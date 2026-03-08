import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1️⃣ Load Dataset
data = pd.read_excel("data/Interview.xlsx")

print("Dataset Loaded Successfully")

# 2️⃣ Handle Missing Values
data = data.fillna(0)

# 3️⃣ Features
feature_columns = [
    "Year",
    "Education Score",
    "Technical Score",
    "Job score",
    "Communication Score",
    "Internship Experience",
    "Soft skill Score",
    "Problem solving Score",
    "Interview Score",
    "Certifications"
]

X = data[feature_columns]

# 4️⃣ Target
y = data["Hired not Unhired"]

if y.dtype == "object":
    y = y.map({"Hired": 1, "Unhired": 0})

# 5️⃣ Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6️⃣ Train Model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# 7️⃣ Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# 8️⃣ Save Model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")