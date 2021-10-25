from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import (Column, Integer, String, Float, ForeignKey)


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    transaction_type = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    destination_account = Column(String, nullable=False)
    account_id = Column(String, ForeignKey("accounts.id"))
    account = relationship("Account")

    def __repr__(self) -> str:
        return f"{self.transaction_type}, {self.amount}"
