# models.py
from geoalchemy2 import Geometry
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import JSON, UUID
from .database import Base

class OpendataPlz(Base):
  __tablename__ = 'opendatasoft_plz_germany'

  id = Column(UUID(as_uuid=True), primary_key=True, server_default='gen_random_uuid()')
  name = Column(String(255))

class Areas(OpendataPlz):
  geometry = Column(Geometry(geometry_type='POLYGON'))

class Postcodes(OpendataPlz):
  plz_code = Column(String(255))
  plz_name = Column(String(255))
  plz_name_long = Column(String(255))
  krs_code = Column(String(255))
  krs_name = Column(String(255))
  lan_code = Column(String(255))
  lan_name = Column(String(255))
  geo_point_2d = Column(JSON)