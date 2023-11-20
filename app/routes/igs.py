# app/routes/igs.py
import json
from fastapi import APIRouter, Depends, Query, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy import func
from sqlalchemy.orm import Session
from .. import utils, models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/")
def get_igs(simplified: str = Query("0.005"), db: Session = Depends(get_db)):
  igs = db.query(models.DimbIg).filter(models.DimbIg.simplified == simplified).all()
  geometries = []
  features = []
  for row in igs:
    geometries.append(row.geometry)
    feature = {
        "type": "Feature",
        "properties": row.meta,
        "geometry": row.geometry
    }
    features.append(feature)

  geometryCollection = {
    "type": "GeometryCollection",
    "geometries": geometries
  }

  properties = utils.properties(geometryCollection)

  return {
    "type": "FeatureCollection",
    "features": features,
    "properties": properties
  }

@router.get("/{name}")
def get_ig(name: str, simplified: str = Query("0.005"), db: Session = Depends(get_db)):
  ig = db.query(models.DimbIg).filter(models.DimbIg.name == name, models.DimbIg.simplified == simplified).scalar()

  if not ig:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found")

  return ig


@router.post("/")
def update_ig(item: schemas.DimbIgInput, simplified: str = Query("0.005"), db: Session = Depends(get_db)):
  ig = db.query(models.DimbIg).filter(models.DimbIg.name == item.name, models.DimbIg.simplified == simplified).scalar()

  geometry = db.query(func.ST_AsGeoJSON(func.ST_Simplify(func.ST_UNION(models.OpendataPlz.geometry), simplified))).filter(models.OpendataPlz.name.in_(item.postcodes)).scalar()
  geometry = utils.parseGeometry(json.loads(geometry))

  if not ig:
    ig = models.DimbIg(name=item.name, simplified=simplified, meta=jsonable_encoder(item))
    ig.geometry = jsonable_encoder(geometry)
    db.add(ig)
  else:
    setattr(ig, "meta", jsonable_encoder(item))
    setattr(ig, "geometry", jsonable_encoder(geometry))

  db.commit()
  db.refresh(ig)
  return ig


@router.put("/{name}")
def update_ig(name: str, item: schemas.DimbIgInput, simplified: str = Query("0.005"), db: Session = Depends(get_db)):
  ig = db.query(models.DimbIg).filter(models.DimbIg.name == name, models.DimbIg.simplified == simplified).scalar()

  if not ig:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found")

  geometry = db.query(func.ST_AsGeoJSON(func.ST_Simplify(func.ST_UNION(models.OpendataPlz.geometry), simplified))).filter(models.OpendataPlz.name.in_(item.postcodes)).scalar()
  geometry = utils.parseGeometry(json.loads(geometry))

  setattr(ig, "meta", jsonable_encoder(item))
  setattr(ig, "geometry", jsonable_encoder(geometry))

  db.commit()
  db.refresh(ig)
  return ig


@router.delete("/{name}")
def delete_ig(name: str, simplified: str = Query("0.005"), db: Session = Depends(get_db)):
  ig = db.query(models.DimbIg).filter(models.DimbIg.name == name, models.DimbIg.simplified == simplified).scalar()
  
  if not ig:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Not found")

  db.delete(ig)
  db.commit()
  return Response(status_code=status.HTTP_204_NO_CONTENT)
