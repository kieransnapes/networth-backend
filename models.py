from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     balances = relationship("Balance", back_populates="owner")


class Balance(Base):
    __tablename__ = "balances"

    id = Column(Integer, primary_key=True, index=True)
    token_id = Column(String, index=True)
    location = Column(String, index=True)
    symbol = Column(String, index=True)
    quantity = Column(String, index=True)
    # owner = relationship("User", back_populates="balances")