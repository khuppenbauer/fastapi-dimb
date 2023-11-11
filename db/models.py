# db/models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from db.connection import Base

class IG(Base):
  __tablename__ = "dimb_ig"

  id = Column(String, primary_key=True, index=True)
  name = Column(String, index=True)
