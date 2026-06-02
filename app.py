from fastapi import FastAPI
from pydantic import BaseModel

from hybrid_inference import predict_hybrid

app = FastAPI(title="Hybrid AI Decision API")

class ComplaintInput (BaseModel):
    customer_id: str

    complaint_text: str

    customer_tenure: float

    previous_complaints: int

    image_category: str

@app.get("/")
def health_check():

    return {
        "status": "ok"
    }

@app.post("/predict")
def predict(payload: ComplaintInput):

    input_data = {

        "complaint_text":
            payload.complaint_text,

        "image_category":
            payload.image_category
    }

    return predict_hybrid(
        input_data
    )