from fastapi import FastAPI
from pydantic import BaseModel

from model import predict

app = FastAPI()


class Greeting(BaseModel):
    message: str


class Prediction(BaseModel):
    value: float
    prediction: float


@app.get("/")
def hello() -> Greeting:
    return Greeting(message="hello world")


@app.get("/predict")
def predict_value(value: float) -> Prediction:
    return Prediction(value=value, prediction=predict(value))
