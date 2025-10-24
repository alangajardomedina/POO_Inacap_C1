from app.bd.conexion import getConexion
from app.modelo.vehiculo import Vehiculo
from app.modelo.moto import Moto
from app.modelo.auto import Auto
import mysql.connector

def agregarVehiculo(vehiculo:Vehiculo):
    try:
        sql = "INSERT INTO vehiculo VALUES(%s,%s,%s,%s,%s,%s)"
        cone = getConexion()
        cursor = cone.cursor()
        
        tiene_patita = None
        cant_puertas = None
        if isinstance(vehiculo, Moto):
            tipo_vehiculo="moto"
            tiene_patita = vehiculo.getTienePatita()
        elif isinstance(vehiculo, Auto):
            tipo_vehiculo="auto"
            cant_puertas = vehiculo.getCantidadPuertas()

        cursor.execute(sql, (vehiculo.getPatente(),
                             vehiculo.getMarca(),
                             vehiculo.getModelo(),
                             tiene_patita,
                             cant_puertas,
                             tipo_vehiculo) )
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")


def verVehiculos():
    pass

def verVehiculo(patente:str):
    pass

def editarVehiculo(vehiculo:Vehiculo):
    pass

def eliminarVehiculo(patente:str):
    pass
