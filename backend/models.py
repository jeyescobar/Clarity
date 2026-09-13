from pydantic import BaseModel

class Transaction(BaseModel):
    amount : float
    description : str
    category : str
    type : str
