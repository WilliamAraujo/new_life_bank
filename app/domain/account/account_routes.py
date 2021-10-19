from typing import List, Optional
from fastapi.routing import APIRouter
from fastapi import HTTPException, status

from account_schema import Account

router = APIRouter()

accounts = []


# @app.get("/accounts/", response_model=List[Account], tags=["accounts"], summary="Return all accounts", description="Return all accounts")
# def account() -> Account:
#     return accounts

# @app.get("/accounts/{id}", response_model=Optional[Account], tags=["accounts"])
# def account_id(id: int) -> Account:
#     for account in accounts:
#         if (account.id == id):
#             return account
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="ID Not found"
#     )

# @app.post("/accounts/", response_model=bool, tags=["accounts"])
# def account(account: Account) -> bool:
#     try:
#         accounts.append(account)
#     except Exception as e:
#         print(f"Error in load account: {e}")
#         return False
#     return True