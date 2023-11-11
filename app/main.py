# app/main.py
from fastapi import FastAPI
from app.routes import igs
from db.connection import engine

app = FastAPI()

app.include_router(igs.router)

@app.get("/")
def read_root():
  return {
    "message": "Welcome to the FastAPI project!"
  }
