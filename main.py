from fastapi import FastAPI
from app.api.v1.endpoints import router as vehicle_router

app = FastAPI()

# Incluir el router de la API de vehículos
app.include_router(vehicle_router)
