import pandas as pd
import random

low_texts = [
    "Delivery was slightly delayed",
    "Need invoice copy",
    "Package arrived late"
]

medium_texts = [
    "Product quality is disappointing",
    "Support response is slow",
    "Wrong color item received"
]

high_texts = [
    "Product arrived broken",
    "Nobody replied to my complaints",
    "Worst experience ever",
    "I want immediate refund"
]

data = []

for i in range(50):
    data.append([
        i+100,
        random.choice(low_texts),
        random.randint(12, 48),
        random.randint(0, 1),
        random.randint(500, 3000),
        "normal",
        "low",
        False
    ])

for i in range(50):
    data.append([
        i+150,
        random.choice(medium_texts),
        random.randint(6, 24),
        random.randint(1, 3),
        random.randint(2000, 8000),
        "normal",
        "medium",
        True
    ])

for i in range(50):
    data.append([
        i+200,
        random.choice(high_texts),
        random.randint(1, 12),
        random.randint(3, 7),
        random.randint(5000, 20000),
        "damaged",
        "high",
        True
    ])

df = pd.DataFrame(data, columns=[
    "complaint_id",
    "complaint_text",
    "customer_tenure_months",
    "previous_complaints",
    "order_value",
    "image_category",
    "risk_label",
    "human_review_required"
])

df.to_csv("complaints.csv", index=False)

print(df.head())