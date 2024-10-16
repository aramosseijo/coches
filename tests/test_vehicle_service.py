import pytest
from unittest.mock import MagicMock
from app.services.vehicle_service import VehicleService
from app.repositories.vehicle_repository import VehicleRepository
from fastapi import HTTPException
import requests

# Datos simulados para pruebas
fake_anos = [
    {"codigo": "2011-1", "nome": "2011 Gasolina"},
    {"codigo": "2012-1", "nome": "2012 Gasolina"},
    {"codigo": "2013-1", "nome": "2013 Gasolina"},
    {"codigo": "2015-1", "nome": "2015 Gasolina"}
]

# Configuración del repositorio simulado
@pytest.fixture
def vehicle_repository_mock():
    # Creamos un mock de VehicleRepository
    repo = MagicMock(spec=VehicleRepository)
    repo.get_marcas.return_value = [{"codigo": "6", "nome": "Audi"}]
    repo.get_modelos.return_value = [{"codigo": "1", "nome": "A1"}]
    repo.get_anos.return_value = fake_anos
    return repo

# Pruebas unitarias para VehicleService
def test_get_filtered_vehicles_posterior(vehicle_repository_mock):
    # Creamos una instancia de VehicleService con el repositorio simulado
    service = VehicleService(vehicle_repository_mock)

    # Llamamos a la función que filtra los vehículos con el filtro "posterior"
    result = service.get_filtered_vehicles(marca="Audi", modelo="A1", year=2012, filtro="posterior")

    # Verificamos que los resultados sean correctos
    assert len(result) == 2
    assert result[0]['nome'] == "2013 Gasolina"
    assert result[1]['nome'] == "2015 Gasolina"

def test_get_filtered_vehicles_anterior(vehicle_repository_mock):
    # Creamos una instancia de VehicleService con el repositorio simulado
    service = VehicleService(vehicle_repository_mock)

    # Llamamos a la función que filtra los vehículos con el filtro "anterior"
    result = service.get_filtered_vehicles(marca="Audi", modelo="A1", year=2013, filtro="anterior")

    # Verificamos que los resultados sean correctos
    assert len(result) == 2
    assert result[0]['nome'] == "2011 Gasolina"
    assert result[1]['nome'] == "2012 Gasolina"

def test_get_filtered_vehicles_igual(vehicle_repository_mock):
    # Creamos una instancia de VehicleService con el repositorio simulado
    service = VehicleService(vehicle_repository_mock)

    # Llamamos a la función que filtra los vehículos con el filtro "igual"
    result = service.get_filtered_vehicles(marca="Audi", modelo="A1", year=2013, filtro="igual")

    # Verificamos que los resultados sean correctos
    assert len(result) == 1
    assert result[0]['nome'] == "2013 Gasolina"

def test_get_filtered_vehicles_invalid_filtro(vehicle_repository_mock):
    # Creamos una instancia de VehicleService con el repositorio simulado
    service = VehicleService(vehicle_repository_mock)

    # Verificamos que se lanza una excepción con un filtro inválido
    with pytest.raises(HTTPException) as excinfo:
        service.get_filtered_vehicles(marca="Audi", modelo="A1", year=2013, filtro="invalido")
    
    # Verificamos el código de error y el mensaje
    assert excinfo.value.status_code == 400
    assert "Filtro no válido" in excinfo.value.detail

def test_get_marcas_api_error(monkeypatch):
    def mock_get(*args, **kwargs):
        raise Exception("API error")
    
    monkeypatch.setattr(requests, "get", mock_get)
    
    repository = VehicleRepository()
    with pytest.raises(HTTPException) as excinfo:
        repository.get_marcas()
    assert excinfo.value.status_code == 500
    assert "Error al obtener las marcas" in excinfo.value.detail

def test_get_filtered_vehicles_filtro_invalido():
    # Simula un filtro inválido en el servicio
    repository = MagicMock()
    service = VehicleService(repository)

    with pytest.raises(HTTPException) as excinfo:
        service.get_filtered_vehicles(marca="Audi", modelo="A1", year=2010, filtro="desconocido")
    
    assert excinfo.value.status_code == 400
    assert "Filtro no válido" in excinfo.value.detail
