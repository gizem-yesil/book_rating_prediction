from fastapi import APIRouter, HTTPException
import pickle
import numpy as np
import tensorflow as tf
from pydantic import BaseModel, Field

router = APIRouter()

with open("notebooks/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

model = tf.keras.models.load_model("notebooks/best_lstm_model.keras") 

class InputData(BaseModel):
        text: str = Field(..., min_length=5, max_length=150, description="The review text to be analyzed")

class PredictionOutput(BaseModel):
        predicted_rating: int




@router.get("/")
def read_root():
    return {"message": "API is working!"}

@router.post("/predict",response_model=PredictionOutput)
def predict_rating(data: InputData):
    try:
        if not data.text.strip():
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        text = data.text
        sequence = tokenizer.texts_to_sequences([text])
        padded_sequence = tf.keras.preprocessing.sequence.pad_sequences(sequence, maxlen=150)
        prediction = model.predict(padded_sequence)
        predicted_rating = np.argmax(prediction) + 1

        print(f"Input text: {data.text}")
        print(f"Predicted rating: {predicted_rating}")
    
        return {"predicted_rating": int(predicted_rating)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
