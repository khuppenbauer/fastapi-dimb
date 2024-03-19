# app/routes/postcodes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db

router = APIRouter()

@router.get("/status")
def read_status():
  return {
    "status": "ok"
  }

@router.get("/{plz_code}")
def get_plz_data(plz_code: str, db: Session = Depends(get_db)):
  postcode = db.query(models.Postcodes).filter(models.Postcodes.plz_code == plz_code).scalar()

  if not postcode:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found")

  return postcode
