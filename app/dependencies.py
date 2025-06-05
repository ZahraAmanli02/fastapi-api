from fastapi import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .auth import oauth2_scheme, verify_token

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return verify_token(token, db)

