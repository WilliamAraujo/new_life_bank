from typing import Any

from sqlalchemy.orm.session import Session


class BaseRepository():
    def create(self, db: Session, model: Any) -> Any:
        db.add(model)
        db.commit()
        db.refresh(model)
        return model

    def all(self, db: Session, cls) -> Any:
        return db.query(cls).all()
