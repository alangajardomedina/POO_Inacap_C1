from libro import Libro

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
    print(menu)
    opc = input("Ingrese opción: ")
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
            from usuario import Usuario
            usuario = Usuario(nombre,edad,numero)
            usuarios.append(usuario)
            print("Usuario agregado con éxito!")
        except ValueError as ex:
            print(ex)
    elif opc=="3":
        pass
    elif opc=="4":
        pass
    elif opc=="5":
        for li in libros:
            print(li)
    elif opc=="6":
        for usu in usuarios:
            print(usu)
    elif opc=="7":
        pass
    elif opc=="0":
        print("Gracias, adios!")
        break
    else:
        print("Error, opción incorrecta!")