# utils.py
from typing import List, Union, Dict
from shapely.geometry import shape, mapping, Polygon, MultiPolygon

GeoJsonFeatureType = Dict[str, Union[str, List[Union[str, List[Union[float, List[List[float]]]]]]]]

def parseGeometry(data: Dict[str, Union[str, List[Union[str, List[Union[float, List[List[float]]]]]]]]) -> GeoJsonFeatureType:
  featureType = data["type"]
  coordinates = data["coordinates"]

  items = []
  if featureType == "Polygon":
    if len(coordinates) > 1:
      items = [max(coordinates, key=len)]
    else:
      items = coordinates
  elif featureType == "MultiPolygon":
    items = [[max(polygon_coordinates, key=len)] for polygon_coordinates in coordinates]

  return {
    "type": featureType,
    "coordinates": items,
  }

def properties(data: Dict[str, Union[str, List[Union[str, List[Union[float, List[List[float]]]]]]]]) -> GeoJsonFeatureType:
  geometry = shape(data)

  bounds = geometry.bounds
  center = mapping(geometry.centroid)["coordinates"]

  return {
    "center" : center,
    "bbox": bounds 
  }
