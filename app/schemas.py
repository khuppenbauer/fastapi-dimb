# schemas.py
from pydantic import BaseModel
from typing import List

class Input(BaseModel):
  postcodes: List = []
