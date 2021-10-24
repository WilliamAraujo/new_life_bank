from config.database import Base
from sqlalchemy.types import Date
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from domain.transaction.transaction_model import Transaction


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    born_date = Column(Date)
    document = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    transaction = relationship(Transaction, backref="accounts")

    def __repr__(self) -> str:
        return f"{self.name}, {self.born_date}, {self.document}, {self.email}, {self.phone_number}"
