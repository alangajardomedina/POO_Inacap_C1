class Persona:
    #aquí dentro puedo crear atributos
    __run = None
    __nombre = None
    __genero = None
    __edad = None
    __especie = "Humano"

    #constructor: es el encargado de crear objetos:
    def __init__(self,run:str=None,nombre:str=None,genero:str=None,edad:int=None):
        self.__run = run
        self.__nombre = nombre
        self.__genero = genero
        self.__edad = edad
    
    #accesador(get): nos entrega el valor de un atributo:
    def getRun(self):
        return self.__run
    def getNombre(self):
        return self.__nombre
    def getGenero(self):
        return self.__genero
    def getEdad(self):
        return self.__edad
    def getEspecie(self):
        return self.__especie
    
    #mutador(set): nos permite modificar el valor de un atributo:
    def setRun(self,run:str):
        self.__run = run
    def setNombre(self,nombre:str):
        if len(nombre.strip())>=3 and nombre.isalpha():
            self.__nombre = nombre
        else:
            raise ValueError("Nombre de la persona incorrecto")

    def setGenero(self,genero:str):
        if genero.lower() in("masculino","femenino","otro"):
            self.__genero = genero
        else:
            raise ValueError("El género debe ser masculino, femenino, otro")

    def setEdad(self,edad:int):
        if edad>=0 and edad<=130:
            self.__edad = edad
        else:
            raise ValueError("La edad debe estar entre 0 y 130")

    def setEspecie(self,especie:str):
        self.__especie = especie
    
    #métodos(N): acciones que ejecuta la clase.
    def saludar(self)->str:
        return f"Hola me llamo {self.__nombre} y tengo {self.__edad} años"
    
    #métodos nativos:
    def __str__(self)->str:
        return f"""Run: {self.__run}
Nombre: {self.__nombre}
Género: {self.__genero}
Edad: {self.__edad}
Especie: {self.__especie}"""


#Vamos a crear objetos a partir de la clase Persona:
#Creamos objetos:
persona1 = Persona("16666666-6","Lalo","Masculino",20)
persona2 = Persona("19999999-9","Elvis","Masculino",25)

persona2.setNombre("Elsa")

print( persona1.saludar() )
print( persona2.saludar() )

print( persona1 )

#No se puede utilizar un atributo privado:
# print( persona1.__nombre )
print(persona1.getNombre() )

persona3 = Persona()
persona3.setRun("15555555-5")
persona3.setNombre("Juanito")
print(persona3)

persona4 = Persona("12456789-9","","",-5)
print(persona4)