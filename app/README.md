# app

Este directorio contiene el código principal de la API FastAPI.

## Estructura

- `api/`: Contiene las rutas y controladores de la API.
- `repositories/`: Define las interacciones con las API externas, como la obtención de marcas y modelos de coches.
- `services/`: Contiene la lógica de negocio para filtrar y procesar los datos de vehículos.

## Detalles

- **api/v1/endpoints.py**: Define los endpoints principales, incluyendo el filtrado de vehículos y la obtención de marcas y modelos.
- **repositories/vehicle_repository.py**: Gestiona las llamadas a la API externa para obtener los datos de los vehículos.
- **services/vehicle_service.py**: Procesa los datos recibidos del repositorio y aplica la lógica de filtrado.
