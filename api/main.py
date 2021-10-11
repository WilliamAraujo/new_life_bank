import uvicorn
from typing import Dict
from datetime import datetime
from fastapi import FastAPI, HTTPException, status

from accounts import Account, accounts

app = FastAPI()

@app.get("/")
def root() -> str:
    return "Welcome to New Life Bank"

@app.get("/health/")
def alive() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}

@app.get("/accounts/")
def account() -> Account:
    return accounts

@app.get("/accounts/{id}")
def account_id(id: int) -> Account:
    for account in accounts:
        if (account.id == id):
            return account
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="ID Not found"
    )

@app.get("/accounts/{cpf}")
def account_id(cpf: str) -> Account:
    for account in accounts:
        if (account.document == cpf):
            return account
    return None

@app.post("/accounts/")
def account(account: Account) -> bool:
    try:
        accounts.append(account)
    except Exception as e:
        print(f"Error in load account: {e}")
        return False
    return True


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
