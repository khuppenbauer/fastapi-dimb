# schemas.py
from pydantic import BaseModel
from typing import List

class DimbIgInput(BaseModel):
  name: str
  postcodes: List = []
  logourl: str = None
  siteurl: str = None
  contact: str = None
  activities: List = []
  description: str = None
