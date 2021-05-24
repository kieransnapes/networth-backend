from typing import List
from typing import Optional
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/balance/", response_model=schemas.Balance)
def create_balance(balance: schemas.BalanceCreate, db: Session = Depends(get_db)):
    return crud.create_balance(db=db, balance=balance)

@app.get("/balance/", response_model=List[schemas.Balance])
def read_balances(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    balances = crud.get_balances(db, skip=skip, limit=limit)
    return balances

@app.get("/balance/{balance_id}", response_model=schemas.Balance)
def read_balance(balance_id: int, db: Session = Depends(get_db)):
    db_balance = crud.get_balance(db, balance_id=balance_id)
    if db_balance is None:
        raise HTTPException(status_code=404, detail="Balance not found")
    return db_balance


