# app/routes/areas.py
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from .. import utils, schemas

router = APIRouter()

@router.get("/status")
def read_status():
  return {
    "status": "ok"
  }

@router.post("/")
def get_properties(item: schemas.GeoJSONFeatureCollection):
  geometries = []
  for feature in item.features:
    geometries.append(jsonable_encoder(feature.geometry))
  geometryCollection = {
    "type": "GeometryCollection",
    "geometries": geometries
  }
  return utils.properties(geometryCollection)
