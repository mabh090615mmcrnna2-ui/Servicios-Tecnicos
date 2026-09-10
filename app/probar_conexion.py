import sys
import os

# Asegura que Python encuentre la carpeta app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from config.conexion import conectar

print("Iniciando prueba de conexión...")
conexion = conectar()

if conexion:
    print("==============================")
    print("CONEXIÓN EXITOSA")
    print("Base de datos: tecnico")
    print("==============================")
    conexion.close()
else:
    print("==============================")
    print("ERROR DE CONEXIÓN")
    print("==============================")