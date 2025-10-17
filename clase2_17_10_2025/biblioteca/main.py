from libro import Libro
from prestamo import Prestamo
from usuario import Usuario

import os, time

libros = []
usuarios = []
prestamos = []

menu = """Menú opciones
1. Añadir libro
2. Añadir usuario
3. Prestar libro
4. Devolver libro
5. Listar libros
6. Listar usuarios
7. Listar prestamos
0. Salir"""

while True:
    time.sleep(3)
    os.system('cls')
    print(menu)
    opc = input("Ingrese opción: ")
    os.system('cls')
    if opc=="1":
        try:
            print("Añadir libro")
            titulo = input("Ingrese título: ")
            autor = input("Ingrese autor: ")
            anio = int(input("Ingrese año publicación: "))
            copias = int(input("Ingrese número copias: "))
            libro = Libro(titulo,autor,anio,copias)
            libros.append(libro)
            print("Libro agregado con éxito!")
        except ValueError as ex:
            print(ex)
    elif opc=="2":
        try:
            print("Añadir usuario")
            nombre = input("Ingrese nombre: ")
            edad = int(input("Ingrese edad: "))
            numero = int(input("Ingrese número usuario: "))
            usuario = Usuario(nombre,edad,numero)
            usuarios.append(usuario)
            print("Usuario agregado con éxito!")
        except ValueError as ex:
            print(ex)
    elif opc=="3":
        if not libros or not usuarios:
            print("Debes registrar libros o usuarios antes de prestamos")
            continue
        print("Prestar libro")
        #1. Necesito un libro (título)
        titulo = input("Ingrese nombre del libro a pedir: ")
        #2. Necesito un usuario (nombre)
        nombre_usu = input("Ingrese nombre usuario para el prestamo: ")
        #3. Validar si existe el libro
        libro = None
        for li in libros:
            if titulo==li.getTitulo() and li.getCopiasDisponibles()>=1:
                li.restarCantidad()
                libro = li
                break
        #4. Validar si existe el usuario
        usuario = None
        for usu in usuarios:
            if nombre_usu==usu.getNombre():
                usuario = usu
                break
        #5. Crear el prestamo
        if not libro or not usuario:
            print("No puedes realizar el prestamo, usuario o libro no encontrado")
            continue
        prestamo = Prestamo(libro,usuario)
        #5.1 Guardar el prestamo en la lista:
        prestamos.append(prestamo)
        #6. Mensaje de prestamo exitoso
        print("Prestamo creado con éxito!")
    elif opc=="4":
        if not prestamos:
            print("No existen prestamos que devolver!")
            continue
        for index,p in enumerate(prestamos):
            print(f"Número:{index+1} - {p}")
        numero = int(input("\nIndique número del prestamo a devolver: "))
        prestamo_devuelto = prestamos.pop(numero-1)
        for li in libros:
            if li.getTitulo()==prestamo_devuelto.getLibro().getTitulo:
                li.sumarCantidad()
        print("Libro devuelto con éxito")
    elif opc=="5":
        if not libros:
            print("No hay libros registrados")
            continue
        for li in libros:
            print(li)
    elif opc=="6":
        if not usuarios:
            print("No hay usuarios registrados")
            continue
        for usu in usuarios:
            print(usu)
    elif opc=="7":
        if not prestamos:
            print("No hay prestamos registrados")
            continue
        for p in prestamos:
            print(p)
    elif opc=="0":
        print("Gracias, adios!")
        break
    else:
        print("Error, opción incorrecta!")
