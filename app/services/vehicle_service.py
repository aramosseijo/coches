from fastapi import HTTPException

class VehicleService:

    def __init__(self, repository):
        self.repository = repository

    def get_filtered_vehicles(self, marca: str, modelo: str, year: int, filtro: str):
    # Verificar el filtro primero
        if filtro not in ["posterior", "anterior", "igual"]:
            raise HTTPException(status_code=400, detail="Filtro no válido. Usa 'posterior', 'anterior' o 'igual'.")

        marca_codigo = self._find_marca_codigo(marca)
        modelo_codigo = self._find_modelo_codigo(marca_codigo, modelo)
        anos = self.repository.get_anos(marca_codigo, modelo_codigo)
        return self._filter_anos(anos, year, filtro)


    def _find_marca_codigo(self, marca: str):
        marcas = self.repository.get_marcas()
        marca_encontrada = next((m for m in marcas if m['nome'].lower() == marca.lower()), None)
        if not marca_encontrada:
            raise HTTPException(status_code=404, detail=f"Marca '{marca}' no encontrada")
        return marca_encontrada['codigo']

    def _find_modelo_codigo(self, marca_codigo: str, modelo: str):
        modelos = self.repository.get_modelos(marca_codigo)
        modelo_encontrado = next((m for m in modelos if modelo.lower() in m['nome'].lower()), None)
        if not modelo_encontrado:
            raise HTTPException(status_code=404, detail=f"Modelo '{modelo}' no encontrado para la marca")
        return modelo_encontrado['codigo']

    def _filter_anos(self, anos: list, year: int, filtro: str):
        if filtro == "posterior":
            vehiculos_filtrados = [ano for ano in anos if int(ano['nome'][:4]) > year]
        elif filtro == "anterior":
            vehiculos_filtrados = [ano for ano in anos if int(ano['nome'][:4]) < year]
        elif filtro == "igual":
            vehiculos_filtrados = [ano for ano in anos if int(ano['nome'][:4]) == year]
        else:
            # Asegúrate de que esta excepción se esté lanzando correctamente
            raise HTTPException(status_code=400, detail="Filtro no válido. Usa 'posterior', 'anterior' o 'igual'.")
        
        return vehiculos_filtrados
