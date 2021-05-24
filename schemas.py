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
    id: str
    # owner_id: int

    class Config:
        orm_mode = True
