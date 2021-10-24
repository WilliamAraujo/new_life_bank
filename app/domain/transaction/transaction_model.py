from config.database import Base
from sqlalchemy.types import Date
from sqlalchemy import Column, Integer, String, Float


class Transaction(Base):
    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, index=True)
    transaction_type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)

    def __repr__(self) -> str:
        return f"{self.transaction_type}, {self.amount}"
