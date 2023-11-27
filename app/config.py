# config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  DATABASE_URL: str
  SECRET_KEY: str
  ALGORITHM: str
  USERNAME: str
  PASSWORD: str

  class Config:
    env_file = ".env"

settings = Settings()
