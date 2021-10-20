from sqlalchemy.orm.session import Session
from commons.base_repository import BaseRepository


class AccountRepository(BaseRepository):
    def read_account(id: int, db: Session, cls):
        #return db.query(cls).filter(==id)
        pass
