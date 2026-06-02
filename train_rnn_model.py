import pandas as pd
import numpy as np

df = pd.read_csv("data/complaints.csv")

print(df.head())

#X = df["complaint_text"]
X = df["complaint_text"].astype(str).to_numpy()
y = df["risk_label"]

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

y = encoder.fit_transform(y)

print(encoder.classes_)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

y_train = np.array(y_train, dtype=np.int32)
y_test = np.array(y_test, dtype=np.int32)

print(type(X_train))
print(X_train.dtype)

print(type(y_train))
print(y_train.dtype)

import tensorflow as tf
from tensorflow.keras import layers

text_vectorizer = layers.TextVectorization(
    max_tokens=10000,
    output_sequence_length=50
)

text_vectorizer.adapt(X_train)

from tensorflow.keras import models

rnn_model = models.Sequential([

    text_vectorizer,

    layers.Embedding(
        input_dim=10000,
        output_dim=64
    ),

    layers.LSTM(64),

    layers.Dense(
        32,
        activation="relu"
    ),

    layers.Dense(
        3,
        activation="softmax"
    )
])

rnn_model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print(df["complaint_text"].head())

print(type(X_train))
print(X_train.dtype)

print(type(y_train))
print(y_train.dtype)

history = rnn_model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=10,
    batch_size=8
)

loss, accuracy = rnn_model.evaluate(
    X_test,
    y_test
)

print("Test Accuracy:", accuracy)


input_text = tf.constant(X_test) 
y_pred_probs = rnn_model.predict(
    input_text,
    verbose=0
)
y_pred = np.argmax(
    y_pred_probs,
    axis=1
)

from sklearn.metrics import accuracy_score, f1_score, classification_report
accuracy = accuracy_score(
    y_test,
    y_pred
)
f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)
print("\nAccuracy:", accuracy)  # Out of all predictions, how many were correct?
print("F1 Score:", f1)          # How good is the model at finding the right class without too many mistakes?
print(
    classification_report(
        y_test,
        y_pred,
        target_names=encoder.classes_
    )
)

rnn_model.save("rnn_model.keras")

print("Model saved successfully.")