from typing import Any
from sqlalchemy.orm.session import Session
from commons.base_repository import BaseRepository


class TransactionRepository(BaseRepository):
    def transfer(self, db: Session, model: Any) -> Any:
        db.add(model)
        db.commit()
        db.refresh(model)
        return model
