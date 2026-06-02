import joblib
import tensorflow as tf

classical_model = joblib.load("classical_model.pkl")

cnn_model = tf.keras.models.load_model("cnn_model.keras")

rnn_model = tf.keras.models.load_model("rnn_model.keras")

RISK_SCORE_MAP = {
    "low": 0.2,
    "medium": 0.6,
    "high": 0.9
}

def map_risk(score):

    if score >= 0.75:
        return "high"

    elif score >= 0.45:
        return "medium"

    else:
        return "low"
    
#image_category
def get_cnn_score(image_category):

    if image_category == "damaged":        #For simplicity
        return 0.9

    return 0.2

def get_classical_score(text):

    prediction = classical_model.predict([text])[0]

    return RISK_SCORE_MAP[prediction]

LABEL_MAP = {
    0: "high",
    1: "low",
    2: "medium"
}

import numpy as np

def get_rnn_score(text):

    #probs = rnn_model.predict(np.array([text]), verbose=0)

    import tensorflow as tf

    input_text = tf.constant([text])

    #print(rnn_model.input_shape)
    #print(rnn_model.inputs)

    probs = rnn_model.predict(input_text, verbose=0)

    label_idx = probs.argmax(axis=1)[0]

    risk = LABEL_MAP[label_idx]

    return RISK_SCORE_MAP[risk]

def hybrid_predict(
        complaint_text,
        image_category):

    classical_score = get_classical_score(
        complaint_text
    )

    cnn_score = get_cnn_score(
        image_category
    )

    rnn_score = get_rnn_score(
        complaint_text
    )

    final_score = (
        0.4 * classical_score +
        0.3 * cnn_score +
        0.3 * rnn_score
    )

    risk_level = map_risk(final_score)

    return {
        "classical_score": round(classical_score, 2),
        "cnn_score": round(cnn_score, 2),
        "rnn_score": round(rnn_score, 2),
        "final_score": round(final_score, 2),
        "risk_level": risk_level
    }

# result = hybrid_predict(
#     complaint_text="Product arrived broken and nobody replied",
#     image_category="damaged"
# )

# print(result)

#########################################################################
from llm_explainer import explain_with_gemini

def predict_hybrid(input_data):

    complaint_text = input_data[
        "complaint_text"
    ]

    image_category = input_data[
        "image_category"
    ]

    model_outputs = hybrid_predict(
        complaint_text,
        image_category
    )

    payload = {
        **model_outputs,
        "complaint_text":
            complaint_text
    }

    try:

        llm_explanation = (
            explain_with_gemini(payload)
        )

    except Exception as e:

        llm_explanation = {

            "summary":
                "LLM explanation unavailable.",

            "recommended_action":
                "manual_review",

            "reason":
                f"LLM error: {str(e)}",

            "human_review_required":
                True,

            "risk_notes": [
                "LLM unavailable"
            ]
        }

    return {

        "model_outputs":
            model_outputs,

        "llm_explanation":
            llm_explanation
    }

input_data = {

    "complaint_text":
        #"The product arrived broken and support has not responded.",
        #"Delivery was slightly delayed",
        "Wrong color item received",
    "image_category":
        "normal",
        #"damaged",
}

result = predict_hybrid(
    input_data
)

import json

print(
    json.dumps(
        result,
        indent=2
    )
)