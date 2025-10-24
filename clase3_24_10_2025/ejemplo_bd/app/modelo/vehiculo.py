class Vehiculo:
    _patente = None
    _marca = None
    _modelo = None

    def __init__(self,patente,marca,modelo):
        self._patente = patente
        self._marca = marca
        self._modelo = modelo
    
    def getPatente(self):
        return self._patente
    def getMarca(self):
        return self._marca
    def getModelo(self):
        return self._modelo
    
    def setPatente(self,patente):
        self._patente = patente
    def setMarca(self,marca):
        self._marca = marca
    def setModelo(self,modelo):
        self._modelo = modelo
    
    def __str__(self):
        return f"Patente: {self._patente} - Marca: {self._marca} - Modelo: {self._modelo}"