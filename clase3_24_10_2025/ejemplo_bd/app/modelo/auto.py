from app.modelo.vehiculo import Vehiculo

class Auto(Vehiculo):
    __cant_puertas = 3

    def __init__(self, patente, marca, modelo, cant_puertas):
        super().__init__(patente, marca, modelo)
        self.__cant_puertas = cant_puertas
    
    def getCantidadPuertas(self):
        return self.__cant_puertas
    
    def setCantidadPuertas(self,cant_puertas):
        self.__cant_puertas = cant_puertas
    
    def __str__(self):
        return super().__str__() + f" - Cant. puertas: {self.__cant_puertas}"
    