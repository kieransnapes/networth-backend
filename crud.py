from sqlalchemy.orm import Session

import models, schemas


def get_balance(db: Session, balance_id: int):
    return db.query(models.Balance).filter(models.Balance.id == balance_id).first()

def create_balance(db: Session, balance: schemas.BalanceCreate):#, user_id: int):
    db_balance = models.Balance(**balance.dict())
    db.add(db_balance)
    db.commit()
    db.refresh(db_balance)
    return db_balance

def get_balances(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Balance).offset(skip).limit(limit).all()
