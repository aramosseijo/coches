import requests
from fastapi import HTTPException

class VehicleRepository:
    BASE_URL = "https://parallelum.com.br/fipe/api/v1/carros"

    def get_marcas(self):
        try:
            response = requests.get(f"{self.BASE_URL}/marcas")
            response.raise_for_status()  # Lanza un error si el status code es diferente de 200
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail="Error al obtener las marcas")

    def get_modelos(self, marca_codigo: str):
        url = f"{self.BASE_URL}/marcas/{marca_codigo}/modelos"
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error al obtener los modelos")
        return response.json()['modelos']

    def get_anos(self, marca_codigo: str, modelo_codigo: str):
        url = f"{self.BASE_URL}/marcas/{marca_codigo}/modelos/{modelo_codigo}/anos"
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error al obtener los años")
        return response.json()
