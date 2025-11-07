from app.modelo.vehiculo import Vehiculo

class Moto(Vehiculo):
    __tiene_patita = True

    def __init__(self, patente, marca, modelo,tiene_patita):
        super().__init__(patente, marca, modelo)
        self.__tiene_patita = tiene_patita
    
    def getTienePatita(self):
        return self.__tiene_patita
    
    def setTienePatita(self,tiene_patita):
        self.__tiene_patita = tiene_patita

    def __str__(self):
        return super().__str__() + f" - Tiene patita: {'Si' if self.__tiene_patita else 'No'}"
    