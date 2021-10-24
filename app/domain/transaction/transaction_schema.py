from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, Field


class TransactionSchema(BaseModel):
    id: int
    transaction_type: str=Field(..., example="123456")
    amount: float
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class TransactionSchemaCreate(BaseModel):
    transaction_type: str
    amount: float

    class Config:
        orm_mode = True    
