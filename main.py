import uvicorn
from fastapi import FastAPI
from datetime import datetime
from pydantic.main import BaseModel
from pydantic import BaseModel, Field
from typing import Dict, List, Optional


class Account(BaseModel):
    id: int
    name: str=Field(..., example="João")
    document: str
    bornDate: str
    email: str
    phoneNumber: Optional[str]


accounts = [
    Account(id=1, name="Ana"     , document="12301", bornDate="01/04/1983", email="ana@gmail.com"      , phoneNumber="19982013301"),
    Account(id=2, name="Rodrigo" , document="12302", bornDate="02/08/1996", email="rodrigo@hotmail.com", phoneNumber="41982013302"),
    Account(id=3, name="Bianca"  , document="12303", bornDate="03/02/1982", email="bianca@gmail.com"   , phoneNumber="61982013303"),
    Account(id=4, name="Fernanda", document="12304", bornDate="04/11/1999", email="fernanda@yahoo.com" , phoneNumber="19982013304"),
    Account(id=5, name="Murilo"  , document="12305", bornDate="05/09/1989", email="murilo@hotmail.com" , phoneNumber="24982013305"),
    Account(id=6, name="Renato"  , document="12306", bornDate="06/03/1994", email="renato@gmail.com"   , phoneNumber="55982013306"),
    Account(id=7, name="Maria"   , document="12307", bornDate="07/08/1988", email="maria@yahoo.com"    , phoneNumber="32982013307"),
    Account(id=8, name="Bruna"   , document="12308", bornDate="08/09/1991", email="bruna@gmail.com")
]

app = FastAPI()

@app.get("/")
def root() -> str:
    return "Welcome to New Life Bank"

@app.get("/health/", tags=["health"])
def alive() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}

@app.get("/accounts/", response_model=List[Account], tags=["accounts"], summary="Return all accounts", description="Return all accounts")
def account() -> Account:
    return accounts

@app.get("/accounts/{id}", response_model=Optional[Account], tags=["accounts"])
def account_id(id: int) -> Account:
    for account in accounts:
        if (account.id == id):
            return account
    return None

@app.get("/accounts/{cpf}", response_model=Optional[Account], tags=["accounts"])
def account_id(cpf: str) -> Account:
    for account in accounts:
        if (account.document == cpf):
            return account
    return None

@app.post("/accounts/", response_model=bool, tags=["accounts"])
def account(account: Account) -> bool:
    try:
        accounts.append(account)
    except Exception as e:
        print(f"Error in load account: {e}")
        return False
    return True


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
