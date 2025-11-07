from app.modelo.moto import Moto
from app.modelo.auto import Auto
from app.controlador.vehiculoDAO import *

def addVehiculo():
    print("AGREGAR VEHÍCULO")
    patente = input("Ingrese patente: ")
    marca = input("Ingrese marca: ")
    modelo = input("Ingrese modelo: ")
    tipo_vehiculo = input("Ingrese tipo vehículo(moto,auto): ")
    if tipo_vehiculo=="moto":
        tiene_patita = input("Indique patita(si,no): ")
        vehiculo = Moto(patente,marca,modelo, True if tiene_patita=="si" else False )
    else:
        cant_puertas = int(input("Ingrese cantidad puertas: "))
        vehiculo = Auto(patente,marca,modelo,cant_puertas)
    if agregarVehiculo(vehiculo):
        print("Vehículo agregado")
    else:
        print("Vehículo no se agregó!")

def getVehiculo():
    v = verVehiculo()
    print(f"Patente: {v["patente"]} - ......")

def getVehiculos():
    for v in verVehiculos():
        print(f"Patente: {v["patente"]} - Marca: {v["marca"]} - ......")

def updateVehiculo():
    print("EDITAR VEHÍCULO")
    patente = input("Ingrese patente de un vehículo registrado: ")
    marca = input("Ingrese marca: ")
    modelo = input("Ingrese modelo: ")
    tipo_vehiculo = input("Ingrese tipo vehículo(moto,auto): ")
    if tipo_vehiculo=="moto":
        tiene_patita = input("Indique patita(si,no): ")
        vehiculo = Moto(patente,marca,modelo, True if tiene_patita=="si" else False )
    else:
        cant_puertas = int(input("Ingrese cantidad puertas: "))
        vehiculo = Auto(patente,marca,modelo,cant_puertas)
    if editarVehiculo(vehiculo):
        print("Vehículo editado")
    else:
        print("Vehículo no se editó!")

def deleteVehiculo():
    print("ELIMINAR VEHÍCULO")
    patente = input("Ingrese patente: ")
    if eliminarVehiculo(patente):
        print("Vehículo eliminado!")
    else:
        print("Vehículo no eliminado!")
