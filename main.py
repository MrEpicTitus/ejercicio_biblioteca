from db import crear_conexion
from operaciones import (crear_tabla_libros,
                         crear_tabla_prestamos,
                         agregar_libro,
                         mostrar_libros,
                         eliminar_libro,
                         registrar_prestamo,
                         mostrar_prestamos)


def menu_principal():
    return input("""
=== MENÚ PRINCIPAL ===
1. Gestionar libros.
2. Gestionar préstamos.
3. Salir
                 
Seleccione una opción:
""")

MENU_LIBROS = """
=== Gestión de libros ===
1. Agregar libro.
2. Mostrar todos los libros.
3. Eliminar libro.
4. Volver al menú principal.

Usted escogió: 
"""
MENU_PRESTAMOS = """
=== Gestión de préstamos ===
1. Registrar préstamo.
2. Mostrar préstamos.
3. Mostrar libros prestados con usuario.
4. Volver al menú principal.

Usted escogió: 
"""

def main():
    # Estableciendo conexión con db
    connection = crear_conexion()

    # Creando tablas
    crear_tabla_libros(connection)
    crear_tabla_prestamos(connection)

    try:
        while True:
            # Creando submenú gestión de préstamos
            def menu_gestion_prestamos():
                while (opcion := input(MENU_PRESTAMOS)) != "4":
                    if opcion == "1":
                        id_libro = int(input("Ingresar ID del libro que solicita: "))
                        nombre_usuario = input("Ingrese su nombre de usuario: ")
                        prestamo_id = registrar_prestamo(connection, id_libro, nombre_usuario)
                        if prestamo_id:#
                            print(f"Préstamo registrado con ID: {prestamo_id}")

                    elif opcion == "2":
                        prestamos = mostrar_prestamos(connection)
                        for prestamo in prestamos:
                            print(prestamo)
                    elif opcion == "3":
                        pass
                    else:
                        print("Opción inválida, por favor intente de nuevo")

            # Creando submenú gestión de libros
            def menu_gestion_libros():
                while (opcion := input(MENU_LIBROS)) != "4":
                    if opcion == "1":
                        titulo = input("Ingresar el nombre del libro: ")
                        autor = input("Ingrensar el nombre del autor: ")
                        id_libro = agregar_libro(connection, titulo, autor)
                        print(f"\nLibro {id_libro} agregado con éxito!")

                    elif opcion == "2":
                        libros = mostrar_libros(connection)
                        for libro in libros:
                            print(libro)

                    elif opcion == "3":
                        id_libro = input("Ingrese el ID del libro que desea eliminar: ")
                        eliminar_libro(connection, id_libro)
                        print(f"Libro {id_libro} eliminado")

                    else:
                        print("Opción inválida, por favor intente de nuevo")

            # Desplegando menú principal
            opcion = menu_principal()
            if opcion == "1":
                menu_gestion_libros()

            elif opcion == "2":
                menu_gestion_prestamos()

            elif opcion == "3":
                print("Hasta pronto, tenga un buen día.")
                break

            else:
                print("Opción inválida")

    finally:
        connection.close()

if __name__ == "__main__":
    main()
