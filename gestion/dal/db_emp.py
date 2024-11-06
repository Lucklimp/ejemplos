import mysql.connector
from mysql.connector import Error

import pandas as pd
from gestion.dal.db import conexion
import os
def agregar_usuario():
        """
        insertar el autor en la BD
        """
        try:
            conn = conexion()
            if conn is not None:
                cursor = conn.cursor()
                nombre = input("Ingrese el nombre: ")
                fecha_nac = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
                fecha_contrato = input("Ingrese la fecha de contrato (YYYY-MM-DD): ")
                sueldo = float(input("Ingrese el sueldo: "))
                correo = input("Ingrese el correo: ")
                telefono = input("Ingrese el teléfono: ")
                direccion = input("Ingrese la dirección: ")


                id_rol = int(input("Ingrese el ID del rol: "))
                id_tipo = int(input("Ingrese el ID del tipo: "))
                nom_usuario = input("Ingrese el nombre de usuario: ")
                password = input("Ingrese la contraseña: ")
                
                      
                sql = "INSERT INTO empleados (nombre, fecha_nac, fecha_contrato, sueldo, correo, telefono, direccion, id_rol, id_tipo, nom_usuario, password) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                valores = (nombre,fecha_nac,fecha_contrato,sueldo, correo, telefono, direccion, id_rol, id_tipo, nom_usuario, password)

                cursor.execute(sql, valores)
                conn.commit()
                print("empleado agregada correctamente")
                cursor.close()
                conn.close()
        except Error as e:
            print(F"Error al agregar al empleado {e}")



def mostrar_empleados():
    """
    Conectar a la base de datos, obtener y mostrar autores en un DataFrame
    """
    os.system("cls")
    try:
        conex = conexion()
        if conex is not None:
            cur = conex.cursor()
            # Ejecutar la consulta
            cur.execute("SELECT * FROM empleados")
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


def eliminar_empleado():
    """
    ELIMINAR EMPLEADOS DE LA BD
    """ 
    try:
        conex = conexion()
        if conex is not None:
            cur = conex.cursor()
            mostrar_empleados()
            # Si la conexión es exitosa, pedir el ID del empleado al usuario
            id_rut = int(input("Ingrese el ID RUT del empleado a eliminar: "))

             # Crear la consulta de eliminación
            sql = "DELETE FROM empleados WHERE id_rut = %s"
            valores = (id_rut,)

            # Ejecutar la consulta de eliminación
            cur.execute(sql, valores)
            conex.commit()  # Confirmar la transacción

            # Verificar si se eliminó alguna fila
            if cur.rowcount > 0:
                print("Empleado eliminado exitosamente.")
            else:
                print("ID RUT no encontrado.")

            # Cerrar el cursor y la conexión
            cur.close()
            conex.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    