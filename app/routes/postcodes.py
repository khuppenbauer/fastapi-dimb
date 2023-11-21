# app/routes/postcodes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db

router = APIRouter()

@router.get("/{plz_code}")
def get_ig(plz_code: str, db: Session = Depends(get_db)):
  postcode = db.query(models.OpendataPlz).filter(models.OpendataPlz.plz_code == plz_code).scalar()

  if not postcode:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found")

  return postcode.geo_point_2d
