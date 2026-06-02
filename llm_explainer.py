from dotenv import load_dotenv
import os

load_dotenv()

#print(os.getenv("GEMINI_API_KEY"))
print("API KEY =", os.getenv("GEMINI_API_KEY"))


input_payload = {
    "classical_score": 0.68,
    "cnn_score": 0.72,
    "rnn_score": 0.81,
    "final_score": 0.74,
    "risk_level": "medium",
    "complaint_text":
        "Product arrived broken and support never responded."
}

import os
import json

from google import genai

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

# client = genai.Client(
#     api_key="AQ.xxx"
# )

###########################################
def explain_with_gemini(input_payload):

    prompt = f"""
You are a business AI decision assistant.

You are NOT allowed to modify:
- classical_score
- cnn_score
- rnn_score
- final_score
- risk_level

Rules:

1. Return valid JSON only.
2. Do not modify any model score.
3. Do not change risk_level.
4. Do not invent facts.
5. If risk_level is high:
   human_review_required = true

Allowed recommended_action values:
- auto_reply
- manual_review
- escalate_immediately

You must choose exactly one.

You are NOT allowed to:
- approve refunds
- reject claims
- offer compensation
- make final customer service decisions

Input:
{json.dumps(input_payload, indent=2)}


Return ONLY these fields:
summary,
recommended_action,
reason,
human_review_required,
risk_notes  (Here, risk_notes must be a JSON array of strings.)

Do not repeat model inputs.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    return json.loads(response.text)


###########################################

payload = {
    "classical_score": 0.68,
    "cnn_score": 0.72,
    "rnn_score": 0.81,
    "final_score": 0.74,
    "risk_level": "medium",
    "complaint_text":
        "The product arrived broken and support has not responded."
}

# result = explain_with_gemini(payload)

# print(
#     json.dumps(
#         result,
#         indent=2
#     )
# )

