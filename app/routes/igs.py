# app/routes/igs.py
from fastapi import APIRouter
from db.models import IG
from db.connection import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/igs/")
def find_igs():
  db = SessionLocal()
  igs = db.query(IG).all()
  db.close()    
  return igs
