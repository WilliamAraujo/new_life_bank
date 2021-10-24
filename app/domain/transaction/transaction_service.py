from sqlalchemy.orm.session import Session
from domain.transaction.transaction_model import Transaction
from domain.transaction.transaction_repository import TransactionRepository
from domain.transaction.transaction_schema import TransactionSchema, TransactionSchemaCreate


def create(db: Session, body: TransactionSchemaCreate) -> TransactionSchema:
    transaction = Transaction(**body.dict())
    return TransactionRepository().create(db, transaction)


def get_transactions(db: Session) -> TransactionSchema:
    return TransactionRepository().all(db, Transaction)
