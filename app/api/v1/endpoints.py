from fastapi import APIRouter, HTTPException
from app.services.vehicle_service import VehicleService
from app.repositories.vehicle_repository import VehicleRepository

router = APIRouter()

# Inyectar dependencias
vehicle_repository = VehicleRepository()
vehicle_service = VehicleService(vehicle_repository)

# Endpoint para obtener vehículos filtrados
@router.get("/vehiculos/")
def get_vehiculos(marca: str, modelo: str, year: int, filtro: str):
    try:
        vehiculos = vehicle_service.get_filtered_vehicles(marca, modelo, year, filtro)
        return {"vehiculos_filtrados": vehiculos}
    except HTTPException as e:
        raise e  # Permitir que HTTPException se propague sin modificarla
    except Exception as e:
        # Cualquier otra excepción que no sea HTTPException genera un error 500
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")
