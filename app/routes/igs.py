# app/routes/igs.py
from fastapi import APIRouter, Query
from db.models import IG
from db.connection import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/igs/")
def get_geofeatures(simplified: str = Query("0.005")):
  db = SessionLocal()
  data = db.query(IG)
  data = data.filter(IG.simplified == simplified)
  data = data.all()
  db.close()
  features = []
  for row in data:
      feature = {
          "type": "Feature",
          "properties": row.meta,
          "geometry": row.geometry
      }
      features.append(feature)

  geofeature_collection = {
      "type": "FeatureCollection",
      "features": features
  }
  return geofeature_collection
