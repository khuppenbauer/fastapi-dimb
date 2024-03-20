# schemas.py
from pydantic import BaseModel
from pydantic_geojson import FeatureModel
from typing import List

class Input(BaseModel):
  postcodes: List = []

class GeoJSONFeatureCollection(BaseModel):
  type: str
  features: List[FeatureModel]
