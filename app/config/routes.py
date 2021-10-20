#!/usr/bin/env python3

from fastapi import FastAPI

from domain.account import account_routes

def setup_routes(app: FastAPI):
    app.include_router(account_routes.router,
                       tags=['Account'],
                       prefix="/account")
