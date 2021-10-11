from pydantic import BaseModel
from pydantic.main import BaseModel


class Account(BaseModel):
    id: int
    name: str
    document: str
    bornDate: str
    email: str
    phoneNumber: str