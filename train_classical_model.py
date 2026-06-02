import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, f1_score

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

df = pd.read_csv("data/complaints.csv")

# ---------------------------------------------------
# Features and Target
# ---------------------------------------------------

X = df["complaint_text"]
y = df["risk_label"]

# ---------------------------------------------------
# Train/Test Split
# ---------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ---------------------------------------------------
# Build Pipeline
# ---------------------------------------------------

model = Pipeline([
    ("tfidf", TfidfVectorizer(max_features=5000)),
    ("clf", LogisticRegression(max_iter=1000))
])

# ---------------------------------------------------
# Train Model
# ---------------------------------------------------

model.fit(X_train, y_train)

# ---------------------------------------------------
# Predictions
# ---------------------------------------------------

y_pred = model.predict(X_test)

# ---------------------------------------------------
# Evaluation
# ---------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)


print("\nAccuracy:", accuracy)  # Out of all predictions, how many were correct?
print("F1 Score:", f1)          # How good is the model at finding the right class without too many mistakes?

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ---------------------------------------------------
# Save Model
# ---------------------------------------------------

joblib.dump(model, "classical_model.pkl")

print("\nModel saved as classical_model.pkl")