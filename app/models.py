# models.py
from geoalchemy2 import Geometry
from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.postgresql import JSON, JSONB, UUID
from .database import Base

class DimbIg(Base):
  __tablename__ = 'dimb_ig'

  id = Column(UUID(as_uuid=True), primary_key=True, server_default='gen_random_uuid()')
  name = Column(String(255), nullable=False)
  meta = Column(JSON)
  geometry = Column(JSONB)
  simplified = Column(Float)

class DimbPlz(Base):
  __tablename__ = 'dimb_ig_plz'

  id = Column(UUID(as_uuid=True), primary_key=True, server_default='gen_random_uuid()')
  bundesland = Column(String(255))
  plz = Column(String(255))
  dimb_ig = Column(String(255))
  landkreis_stadt = Column(String(255))

class OpendataPlz(Base):
  __tablename__ = 'dimb_opendatasoft_plz_germany'

  id = Column(UUID(as_uuid=True), primary_key=True, server_default='gen_random_uuid()')
  name = Column(String(255))
  plz_code = Column(String(255))
  plz_name = Column(String(255))
  plz_name_long = Column(String(255))
  geometry = Column(Geometry(geometry_type='POLYGON'))
  krs_code = Column(String(255))
  krs_name = Column(String(255))
  lan_code = Column(String(255))
  lan_name = Column(String(255))
  geo_point_2d = Column(JSON)
