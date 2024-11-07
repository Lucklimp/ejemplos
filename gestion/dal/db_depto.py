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



def reasignar_departamento(): 
    """ Reasigna un empleado a un nuevo departamento, 
    asegurando que el empleado esté asociado a un solo departamento a la vez, 
    y confirmando si desea eliminar al empleado del departamento actual. """ 
    try: 
        conn = conexion() 
        if conn is not None: 
            with conn.cursor() as cursor: 
                id_empleado = input("Ingrese el ID del empleado: ") 
                id_depto = input("Ingrese el ID del nuevo departamento: ") # Verificar si el empleado ya está asignado a un departamento
                sql_verificar = "SELECT id_depto FROM asignacion WHERE id_rut = %s" 
                cursor.execute(sql_verificar, (id_empleado,)) 
                resultado = cursor.fetchone() 
                if resultado: # Si el empleado ya está asignado a un departamento, pedir confirmación para reasignar 
                    confirmar = input(f"El empleado {id_empleado} ya está asignado al departamento {resultado[0]}. ¿Desea reasignarlo? (s/n): ")
                    if confirmar == 's': # Eliminar la asignación existente del empleado 
                        sql_delete = "DELETE FROM asignacion WHERE id_rut = %s" 
                        cursor.execute(sql_delete, (id_empleado,)) # Asignar el empleado al nuevo departamento 
                        sql_insert = "INSERT INTO asignacion (id_depto, id_rut) VALUES (%s, %s)" 
                        valores = (id_depto, id_empleado) 
                        cursor.execute(sql_insert, valores) 
                        conn.commit() 
                        print("Empleado reasignado correctamente al nuevo departamento") 
                    else: 
                        print("Reasignación cancelada.") 
                else: # Si el empleado no está asignado a ningún departamento, proceder con la asignación 
                    sql_insert = "INSERT INTO asignacion (id_depto, id_empleado, fecha_asignacion) VALUES (%s, %s)"
                    valores = (id_depto, id_empleado) 
                    cursor.execute(sql_insert, valores) 
                    conn.commit() 
                    print("Empleado asignado correctamente al departamento") 
                    cursor.close() 
                    conn.close() 
    except Error as e: 
        print(f"Error al reasignar el departamento: {e}")