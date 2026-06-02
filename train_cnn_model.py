import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# ---------------------------------------------------
# Dataset Path
# ---------------------------------------------------

dataset_path = "data/images"

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=(64, 64),
    batch_size=8
)

validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed=42,
    image_size=(64, 64),
    batch_size=8
)

# ---------------------------------------------------
# Class Names
# ---------------------------------------------------

class_names = train_dataset.class_names

print("Classes:", class_names)

# ---------------------------------------------------
# Prefetch for Performance
# ---------------------------------------------------

AUTOTUNE = tf.data.AUTOTUNE

train_dataset = train_dataset.prefetch(buffer_size=AUTOTUNE)
validation_dataset = validation_dataset.prefetch(buffer_size=AUTOTUNE)

# ---------------------------------------------------
# Build CNN Model
# ---------------------------------------------------

cnn_model = models.Sequential([

    layers.Rescaling(1./255, input_shape=(64, 64, 3)),

    layers.Conv2D(16, (3, 3), activation="relu"),
    layers.MaxPooling2D(),

    layers.Conv2D(32, (3, 3), activation="relu"),
    layers.MaxPooling2D(),

    layers.Flatten(),

    layers.Dense(64, activation="relu"),

    layers.Dense(len(class_names), activation="softmax")
])

# ---------------------------------------------------
# Compile Model
# ---------------------------------------------------

cnn_model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# ---------------------------------------------------
# Train Model
# ---------------------------------------------------

history = cnn_model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=10
)

loss, accuracy = cnn_model.evaluate(
    validation_dataset
)

print("Validation Accuracy:", accuracy)

##################
import numpy as np

y_true = []
y_pred = []

for images, labels in validation_dataset:

    predictions = cnn_model.predict(
        images,
        verbose=0
    )

    predicted_labels = np.argmax(
        predictions,
        axis=1
    )

    y_true.extend(labels.numpy())
    y_pred.extend(predicted_labels)

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report

accuracy = accuracy_score(
    y_true,
    y_pred
)

f1 = f1_score(
    y_true,
    y_pred,
    average="weighted"
)

print("Accuracy:", accuracy)
print("F1 Score:", f1)

print(
    classification_report(
        y_true,
        y_pred,
        target_names=class_names
    )
)
##################


# ---------------------------------------------------
# Save Model
# ---------------------------------------------------

cnn_model.save("cnn_model.keras")

print("\nCNN model saved as cnn_model.keras")