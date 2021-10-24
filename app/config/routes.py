from fastapi import FastAPI

from domain.account import account_routes
from domain.transaction import transaction_routes


def setup_routes(app: FastAPI):
    app.include_router(account_routes.router,
                       tags=['Account'],
                       prefix="/account")

    app.include_router(transaction_routes.router,
                       tags=['Transaction'],
                       prefix="/transaction")
