import mysql.connector
from mysql.connector import Error

import pandas as pd
from GESTION.DAL.db import conexion

def agregar_departamento():

    try: 
        conn = conexion() 
        if conn is not None: 
            cursor = conn.cursor() 
            nombre = input("Ingrese el nombre del departamento: ") 
            # No se usa ninguna clase aquí, solo el nombre del departamento 
            sql = "INSERT INTO departamento (nombre) VALUES (%s)" 
            valores = (nombre,) # Nota: Asegúrate de que valores es una tupla 
            cursor.execute(sql, valores) 
            conn.commit() 
            print("Departamento agregado correctamente") 
            cursor.close() 
            conn.close() 
    except mysql.connector.Error as e: 
        print(f"Error al agregar el departamento: {e}")

def mostrar_departamentos():
    """
    Conectar a la base de datos, obtener y mostrar autores en un DataFrame
    """
    try:
        conex = conexion()
        if conex is not None:
            cur = conex.cursor()
            # Ejecutar la consulta
            cur.execute("SELECT * FROM departamento")
            # Obtener los resultados y convertirlos en un DataFrame
            resultados = cur.fetchall()
            columnas = [col[0] for col in cur.description]  # Obtener los nombres de las columnas
            df = pd.DataFrame(resultados, columns=columnas)

        # Mostrar el DataFrame
            print(df)

        # Cerrar la conexión
            cur.close()
            conex.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")



def actualizar_departamento():
    """
    Actualizar el nombre de un departamento en la base de datos
    """
    try:
        conn = conexion()
        cursor = conn.cursor()

        dept_id = input("Introduce el ID del departamento que quieres actualizar: ") 
        nuevo_nombre = input("Introduce el nuevo nombre del departamento: ")
        # Crear la consulta de actualización
        sql = "UPDATE departamento SET nombre = %s WHERE id_depto = %s"
        valores = (nuevo_nombre, dept_id)
        
        # Ejecutar la consulta de actualización
        cursor.execute(sql, valores)
        conn.commit()  # Confirmar la transacción

        # Verificar si se actualizó alguna fila
        if cursor.rowcount > 0:
            print("Departamento actualizado exitosamente.")
        else:
            print("ID del departamento no encontrado.")

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def buscar_departamento(nombre):
    """
    Buscar departamentos en la BD
    """
    try:
        conn = conexion()
        cursor = conn.cursor()

        # Crear la consulta de búsqueda
        sql = "SELECT * FROM departamento WHERE nombre = %s"
        valores = (nombre,)

        # Ejecutar la consulta de búsqueda
        cursor.execute(sql, valores)
        resultado = cursor.fetchall()

        # Verificar si se encontró algún departamento
        if resultado:
            for departamento in resultado:
                print(departamento)
        else:
            print("Departamento no encontrado.")

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def eliminar_departamento(nombre):
    """
    
    """
    try:
        conn = conexion()
        cursor = conn.cursor()

        # Crear la consulta de eliminación
        sql = "DELETE FROM departamento WHERE nombre = %s"
        valores = (nombre,)

        # Ejecutar la consulta de eliminación
        cursor.execute(sql, valores)
        conn.commit()  # Confirmar la transacción

        # Verificar si se eliminó alguna fila
        if cursor.rowcount > 0:
            print("Departamento eliminado exitosamente.")
        else:
            print("Nombre del departamento no encontrado.")

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def asignar_departamento():
    """
    asigna un departamento
    """
    try: 
        conn = conexion() 
        if conn is not None: 
            cursor = conn.cursor() 
            nombre_id= input("Ingrese del empleado: ") 
            nombre_id_depto= input("Ingrese la id del departamento: ") 
            sql = "INSERT INTO asignacion (id_depto, id_rut) VALUES (%s,%s)" 
            valores = ( nombre_id_depto, nombre_id) 
            cursor.execute(sql, valores) 
            conn.commit() 
            print("departamneto asignado correctamente") 
            cursor.close() 
            conn.close() 
    except Error as e: 
        print(f"Error al asignarel departamento: {e}")