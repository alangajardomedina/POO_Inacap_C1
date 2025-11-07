import time
from app.vista.vehiculo_view import *

menu="""MENÚ OPCIONES
1. Agregar vehículo
2. Ver vehículos
3. Ver vehículo
4. Editar vehículo
5. Eliminar vehículo
6. Salir"""

while True:
    print(menu)
    opcion=input("Ingrese número de la opción: ")
    if opcion=="1":
        addVehiculo()
    elif opcion=="2":
        getVehiculos()
    elif opcion=="3":
        getVehiculo()
    elif opcion=="4":
        updateVehiculo()
    elif opcion=="5":
        deleteVehiculo()
    elif opcion=="6":
        print("Gracias, adios!")
        break
    else:
        print("Opción incorrecta!")
    time.sleep(3)