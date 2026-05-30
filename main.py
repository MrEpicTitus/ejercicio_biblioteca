from db import crear_conexion
from operaciones import (crear_tabla_libros,
                         crear_tabla_prestamos,
                         agregar_libro,
                         mostrar_libros,
                         eliminar_libro)


def menu_principal():
    return input("""
=== MENÚ PRINCIPAL ===
1. Gestionar libros.
2. Gestionar préstamos.
3. Salir
                 
Seleccione una opción:
""")

MENU_LIBROS = """
=== Gestión de estudiantes ===
1. Agregar libro.
2. Mostrar todos los libros.
3. Eliminar libro.
4. Volver al menú principal.

Usted escogió: 
\n
"""
MENU_PRESTAMOS = """"""

def main():
    # Estableciendo conexión con db
    connection = crear_conexion()

    # Creando tablas
    crear_tabla_libros(connection)
    crear_tabla_prestamos(connection)

    try:
        while True:
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
                        id_libro = input("Ingrese el ID del libro que desea modificar: ")
                        eliminar_libro(connection, id_libro)
                        print(f"Libro {id_libro} eliminado")
                    else:
                        print("Opción inválida, por favor intente de nuevo")

            # Desplegando menú principal
            opcion = menu_principal()
            if opcion == "1":
                menu_gestion_libros()
            elif opcion == "2":
                pass
            elif opcion == "3":
                print("Hasta pronto, tenga un buen día.")
                break

            else:
                print("Opción inválida")

    finally:
        connection.close()

if __name__ == "__main__":
    main()
