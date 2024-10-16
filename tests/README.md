# tests

Este directorio contiene las pruebas unitarias e integradas para el proyecto.

## Estructura de las pruebas

- **`test_vehicle_service.py`**: Pruebas unitarias para la lógica de filtrado de vehículos en el servicio.
- **`test_vehicle_repository.py`**: Pruebas unitarias para el repositorio de vehículos, incluyendo simulación de errores.
- **`test_integration.py`**: Pruebas de integración que verifican el correcto funcionamiento de los endpoints y servicios de la API.

## Cómo ejecutar las pruebas

Para ejecutar todas las pruebas, utiliza:

```bash
pytest

Para generar un reporte de cobertura:
pytest --cov=app --cov-report term-missing

