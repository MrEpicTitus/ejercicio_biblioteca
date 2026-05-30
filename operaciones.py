# Tabla libros
def crear_tabla_libros(connection):
    query = """CREATE TABLE IF NOT EXISTS libros (
                    id INTEGER PRIMARY KEY,
                    titulo TEXT NOT NULL UNIQUE,
                    autor TEXT NOT NULL
                )
            """
    connection.execute(query)
    print("Tabla libros creada exitosamente!")

# Tabla préstamos
def crear_tabla_prestamos(connection):
    query = """CREATE TABLE IF NOT EXISTS prestamos (
                    id_prestamos INTEGER PRIMARY KEY,
                    nombre_usuario TEXT NOT NULL,
                    id_libro INTEGER,
                    FOREIGN KEY(id_libro) REFERENCES libros(id) 
                )
            """
    connection.execute(query)
    print("Tabla préstamos creada exitosamente!")

################# SUBMENÚ LIBROS
# 1 - Agregar libro
def agregar_libro(connection, titulo, autor):
    query = """INSERT INTO libros (titulo, autor) VALUES (?, ?)"""
    cursor = connection.cursor()
    cursor.execute(query, (titulo, autor))
    connection.commit()
    return cursor.lastrowid

# 2 - Mostrar todos los libros
def mostrar_libros(connection):
    query = "SELECT * FROM libros"
    return connection.execute(query).fetchall()

# 3 - Eliminar libro
def eliminar_libro(connection, id_libro):
    query = "DELETE FROM libros WHERE id = ?"
    cursor = connection.cursor()
    cursor.execute(query, (id_libro,))
    connection.commit()

################# SUBMENÚ PRÉSTAMOS
# 1 - Registrar un préstamo
def registrar_prestamo(connection, id_libro, nombre_usuario):
    query1 = "SELECT id FROM libros WHERE id = ?"
    cursor = connection.cursor()
    try:
        resultado = cursor.execute(query1, (id_libro,)).fetchone()
        if resultado is None:
            print(f"El libro con el ID: {id_libro} no existe.")
            return
        
        print(f"El libro con el ID {id_libro} existe.")
        query2 = """INSERT INTO prestamos (nombre_usuario, id_libro)
                        VALUES (?, ?)
                        """
        cursor.execute(query2, (nombre_usuario, id_libro))
        connection.commit()
        return cursor.lastrowid
    
    except Exception as e:
        print("Error al registrar el préstamo: ", e)

# Mostrar préstamos
def mostrar_prestamos(connection):
    query = "SELECT * FROM prestamos"
    return connection.execute(query).fetchall()
