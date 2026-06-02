import pandas as pd

from hybrid_inference import hybrid_predict

from sklearn.metrics import (
    accuracy_score,
    f1_score
)

df = pd.read_csv("data/complaints.csv")

actual = []
predicted = []

for _, row in df.iterrows():

    result = hybrid_predict(
        row["complaint_text"],
        row["image_category"]
    )

    predicted.append(
        result["risk_level"]
    )

    actual.append(
        row["risk_label"]
    )

accuracy = accuracy_score(
    actual,
    predicted
)

f1 = f1_score(
    actual,
    predicted,
    average="weighted"
)

print("Hybrid Accuracy:", accuracy)
print("Hybrid F1:", f1)