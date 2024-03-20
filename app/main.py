# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import areas, properties, postcodes, token

app = FastAPI()

app.include_router(areas.router, prefix='/api/areas')
app.include_router(properties.router, prefix='/api/properties')
app.include_router(postcodes.router, prefix='/api/postcodes')
app.include_router(token.router)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
def read_root():
  return {
    "message": "Welcome to the FastAPI project!"
  }
