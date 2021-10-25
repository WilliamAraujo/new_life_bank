import json
from sqlalchemy.orm.session import Session
from domain.account.account_model import Account
from domain.transaction.transaction_model import Transaction
from domain.transaction.transaction_repository import TransactionRepository
from domain.transaction.transaction_schema import TransactionSchema, TransactionSchemaCreate


def create(db: Session, body: TransactionSchemaCreate) -> TransactionSchema:
    account_id = int(body.account_id)
    account = TransactionRepository().filter_by_id(db, Account, account_id)[0]
    if (account is not None):
        _account = {"name": account.name, "document": account.document, "email": account.email}
        body.account_id = json.dumps(_account)
    transaction = Transaction(**body.dict())
    return TransactionRepository().transfer(db, transaction)


def get_transactions(db: Session) -> TransactionSchema:
    return TransactionRepository().all(db, Transaction)
