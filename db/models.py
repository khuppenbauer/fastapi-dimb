# db/models.py
from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION, UUID, JSON
from db.connection import Base

class IG(Base):
  __tablename__ = "dimb_ig"

  id = Column(UUID, primary_key=True)
  name = Column(String(255), nullable=False)
  meta = Column(JSON)
  geometry = Column(JSON)
  simplified = Column(Float)
