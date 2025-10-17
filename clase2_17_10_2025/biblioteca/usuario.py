class Usuario:
    __nombre = None
    __edad = None
    __numeroUsuario = None

    def __init__(self,nombre:str,edad:int,numero:int):
        self.__nombre = nombre
        self.setEdad(edad)
        self.__numeroUsuario = numero

    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getNumeroUsuario(self):
        return self.__numeroUsuario
    
    def setNombre(self,nombre):
        self.__nombre = nombre
    def setEdad(self,edad):
        if edad>=12:
            self.__edad = edad
        else:
            raise ValueError("Error, la edad mínima es 12 años")

    def setNumeroUsuario(self,numero):
        self.__numeroUsuario = numero
    
    def __str__(self):
        return f"Nombre: {self.__nombre} - Edad: {self.__edad} - Número usuario: {self.__numeroUsuario}"
