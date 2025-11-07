from app.bd.conexion import getConexion
from app.modelo.vehiculo import Vehiculo
from app.modelo.moto import Moto
from app.modelo.auto import Auto
import mysql.connector

#DAO: data access object

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
    try:
        sql = "SELECT * FROM vehiculo"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql)
        filas = cursor.fetchall()
        cursor.close()
        cone.close()
        return filas
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")

def verVehiculo(patente:str):
    try:
        sql = "SELECT * FROM vehiculo WHERE patente = %s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql, (patente,))
        fila = cursor.fetchone()
        cursor.close()
        cone.close()
        return fila
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")

def editarVehiculo(vehiculo:Vehiculo):
    try:
        sql = "UPDATE vehiculo SET marca=%s, modelo=%s, tiene_patita=%s, cant_puertas=%s, tipo_vehiculo=%s WHERE patente=%s"
        cone = getConexion()
        cursor = cone.cursor()
        
        tiene_patita=None
        cant_puertas=None
        tipo_vehiculo=None
        if isinstance(vehiculo,Moto):
            tiene_patita,tipo_vehiculo = vehiculo.getTienePatita(),"moto"
        elif isinstance(vehiculo,Auto):
            cant_puertas,tipo_vehiculo = vehiculo.getCantidadPuertas(),"auto"

        cursor.execute(sql, (vehiculo.getMarca(),
                             vehiculo.getModelo(),
                             tiene_patita,
                             cant_puertas,
                             tipo_vehiculo,
                             vehiculo.getPatente()))
        #siempre se debe confirmar el insertar, actualizar y eliminar... SIEMPRE!
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")

def eliminarVehiculo(patente:str):
    try:
        sql = "DELETE FROM vehiculo WHERE patente=%s"
        cone = getConexion()
        cursor = cone.cursor()
        cursor.execute(sql,(patente,))
        cone.commit()
        cursor.close()
        cone.close()
        return True
    except mysql.connector.Error as ex:
        print(f"Error: {ex}")
