import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Deja comillas vacías si usas XAMPP por defecto
            database="tecnico"
        )
        return conexion
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None