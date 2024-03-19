# app/routes/areas.py
import json
from fastapi import APIRouter, Depends, Query
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import utils, models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/status")
def read_status():
  return {
    "status": "ok"
  }

@router.post("/")
def generate_area(item: schemas.Input, simplified: str = Query("0.005"), db: Session = Depends(get_db)):
  geometry = db.query(func.ST_AsGeoJSON(func.ST_Simplify(func.ST_UNION(models.Areas.geometry), simplified))).filter(models.Areas.name.in_(item.postcodes)).scalar()
  geometry = utils.parseGeometry(json.loads(geometry))
  return geometry
