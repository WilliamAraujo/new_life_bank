from typing import Optional
from pydantic import BaseModel, Field


class Account(BaseModel):
    id: int
    name: str=Field(..., example="João")
    document: str
    bornDate: str
    email: str
    phoneNumber: Optional[str]
