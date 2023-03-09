from scripts.txt2imgprocess import main
from pydantic import BaseModel

from fastapi import FastAPI
app = FastAPI()



@app.get("/")
def read_root():
    return "Stable diffusion works!"



class PredictRequest(BaseModel):
    prompt: str


@app.post("/predict")
def read_root(predict_request : PredictRequest):

    images = main(predict_request.prompt)

    return  images