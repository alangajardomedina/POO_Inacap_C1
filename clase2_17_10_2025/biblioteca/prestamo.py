from datetime import datetime
from libro import Libro
from usuario import Usuario

class Prestamo:
    __libro = None
    __usuario = None
    __fecha = None

    def __init__(self,libro:Libro,usuario:Usuario):
        self.__libro = libro
        self.__usuario = usuario
        self.__fecha = datetime.now()
    
    def getLibro(self):
        return self.__libro
    def getUsuario(self):
        return self.__usuario
    def getFecha(self):
        return self.__fecha
    
    def setLibro(self,libro):
        self.__libro = libro
    def setUsuario(self,usuario):
        self.__usuario = usuario

    def __str__(self):
        return f"Prestamo: {self.__libro} | {self.__usuario}"