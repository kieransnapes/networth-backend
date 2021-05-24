from typing import List, Optional

from pydantic import BaseModel


class BalanceBase(BaseModel):
    token_id: str
    location: Optional[str] = None
    symbol: str
    quantity: str


class BalanceCreate(BalanceBase):
    pass


class Balance(BalanceBase):
    id: int
    # owner_id: int

    class Config:
        orm_mode = True


# class UserBase(BaseModel):
#     email: str


# class UserCreate(UserBase):
#     password: str


# class User(UserBase):
#     id: int
#     is_active: bool
#     balances: List[Balance] = []

#     class Config:
#         orm_mode = True