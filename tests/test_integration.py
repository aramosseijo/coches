from fastapi.testclient import TestClient
from main import app  # Importa la app de FastAPI desde el archivo principal

client = TestClient(app)

def test_get_vehiculos_posterior():
    # Enviar una solicitud GET a /vehiculos/?marca=Audi&modelo=A1&year=2010&filtro=posterior
    response = client.get("/vehiculos/?marca=Audi&modelo=A1&year=2010&filtro=posterior")
    
    # Verificar que la respuesta tenga el código de estado 200
    assert response.status_code == 200
    
    # Verificar que el contenido de la respuesta esté presente
    data = response.json()
    assert "vehiculos_filtrados" in data
    assert len(data["vehiculos_filtrados"]) > 0  # Debe haber vehículos posteriores a 2010

def test_get_vehiculos_anterior():
    # Enviar una solicitud GET a /vehiculos/?marca=Audi&modelo=A1&year=2015&filtro=anterior
    response = client.get("/vehiculos/?marca=Audi&modelo=A1&year=2015&filtro=anterior")
    
    # Verificar que la respuesta tenga el código de estado 200
    assert response.status_code == 200
    
    # Verificar que el contenido de la respuesta esté presente
    data = response.json()
    assert "vehiculos_filtrados" in data
    assert len(data["vehiculos_filtrados"]) > 0  # Debe haber vehículos anteriores a 2015

def test_get_vehiculos_filtro_invalido():
    # Enviar una solicitud GET con un filtro no válido
    response = client.get("/vehiculos/?marca=Audi&modelo=A1&year=2013&filtro=invalido")
    
    # Verificar que la respuesta tenga el código de estado 400 (Bad Request)
    assert response.status_code == 400
    
    # Verificar el mensaje de error
    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Filtro no válido. Usa 'posterior', 'anterior' o 'igual'."
