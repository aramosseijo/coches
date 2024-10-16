# Coches API

Este proyecto es una API basada en **FastAPI** para consultar y filtrar información de vehículos a través de la API externa: https://deividfortuna.github.io/fipe/

## Funcionalidad

La API permite:
- Obtener una lista de marcas de coches.
- Filtrar modelos de vehículos según marca, modelo y año.
- Filtrar vehículos por criterios como `posterior`, `anterior` o `igual` a un año específico.

## Requisitos

- **Python 3.9+**
- **pip**
- **FastAPI** y **Uvicorn** para la ejecución de la API.

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/aramosseijo/coches.git
    cd coches
    ```

2. Crea un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Puesta en marcha

1. Para iniciar la API, ejecuta el siguiente comando:

    ```bash
    uvicorn main:app --reload
    ```

2. Accede a la documentación interactiva en:

    - Swagger UI: `http://127.0.0.1:8000/docs`
    - Redoc: `http://127.0.0.1:8000/redoc`

## Estructura del Proyecto

- `app/`: Contiene los módulos principales de la API.
- `tests/`: Contiene pruebas unitarias e integradas.
- `requirements.txt`: Lista de dependencias del proyecto.

## Pruebas

Para ejecutar las pruebas unitarias e integradas:

```bash
pytest
