import sqlite3

def crear_conexion():
    return sqlite3.connect("biblos.db")
