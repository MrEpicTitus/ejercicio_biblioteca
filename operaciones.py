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
