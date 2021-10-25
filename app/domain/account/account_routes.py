from typing import List
from fastapi import Depends
from fastapi.routing import APIRouter
from config.database import get_db
from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session

from domain.account import account_service
from domain.account.account_schema import AccountSchema, AccountSchemaCreate

router = APIRouter()


@router.get("/",
            summary="Operação responsável por retornar todas as conta cadastradas.",
            response_model=List[AccountSchema])
def get_accounts(db: Session = Depends(get_db)):
    return account_service.get_accounts(db)

@router.get("/{id}",
            summary="Operação responsável por retornar uma conta.",
            response_model=List[AccountSchema])
def get_account(id: int, db: Session = Depends(get_db)):
    return account_service.get_account(db, id)

@router.post("/",
             summary="Operação responsável por criar uma nova conta.",
             response_model=AccountSchema)
def create_account(body: AccountSchemaCreate, db: Session = Depends(get_db)):
    return account_service.create(db, body)
