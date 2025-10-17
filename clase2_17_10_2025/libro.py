class Libro:
    __titulo = None
    __autor = None
    __anioPublicacion = None
    __copiasDisponibles = None

    def __init__(self,titulo,autor,anio,copias):
        self.__titulo = titulo
        self.__autor = autor
        self.setAnioPublicacion(anio)
        self.setCopiasDisponibles(copias)

    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getAnioPublicacion(self):
        return self.__anioPublicacion
    def getCopiasDisponibles(self):
        return self.__copiasDisponibles
    
    def setTitulo(self,titulo):
        self.__titulo = titulo
    def setAutor(self,autor):
        self.__autor = autor
    def setAnioPublicacion(self,anio):
        if anio>=1450:
            self.__anioPublicacion = anio
        else:
            raise ValueError("Error, el año de publicación debe ser a partir de 1450")

    def setCopiasDisponibles(self,copias):
        if copias>=0:
            self.__copiasDisponibles = copias
        else:
            raise ValueError("Error, las copias disponibles no pueden ser negativas")
    