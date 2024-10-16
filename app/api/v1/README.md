# app/api/v1

Este directorio contiene los endpoints para la versión 1 de la API.

## Rutas principales

- `/vehiculos/`: Permite obtener vehículos filtrados según la marca, el modelo y el año.
- Se pueden aplicar filtros como `posterior`, `anterior` o `igual` a un año específico.

Las rutas están implementadas en **`endpoints.py`**, utilizando **FastAPI** para definir las solicitudes HTTP y manejar los parámetros.
