from fastapi import FastAPI
from models import Transaction


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Clarity API is running"}


@app.post("/transactions")
def create_transaction(transaction : Transaction):
    return transaction