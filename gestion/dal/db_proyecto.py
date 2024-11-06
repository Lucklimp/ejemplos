from gestion.dal.db import conexion
from mysql.connector import Error
import pandas as pd
def crear_proyecto():
    """
    Crea un nuevo proyecto
    """
    try: 
        conn = conexion() 
        if conn is not None: 
            cursor = conn.cursor() 
            nombre = input("Ingrese el nombre del departamento: ") 
            descripcion = input("Ingrese una breve descripcion del proyecto: ") 
            fecha_ini = input("Ingrese la fecha de inicio del proyecto(YYYY-MM-DD): ") 
            plazo = input("Ingrese la fecha de plazzo maximo para entregar el proyecto(YYYY-MM-DD): ") 
            sql = "INSERT INTO proyecto (nombre, descripcion, fecha_inicio, fecha_plazo) VALUES (%s,%s,%s,%s)" 
            valores = (nombre, descripcion, fecha_ini, plazo) 
            cursor.execute(sql, valores) 
            conn.commit() 
            print("Proyecto agregado correctamente") 
            cursor.close() 
            conn.close() 
    except Error as e: 
        print(f"Error al agregar el departamento: {e}")

def actualizar_proyecto():
    """
    Actualiza los parametros del proyecto (editar)
    """
    try:
        conn = conexion()
        cursor = conn.cursor()
        mostrar_proyecto()
        proyec_id = input("Introduce el ID del proyecto que quieres actualizar: ") 
        nuevo_nombre = input("Introduce el nuevo nombre del proyecto: ")
        nueva_descripcion = input("actualice la nueva descripcion")
        fecha_plazo = input("Ingrese la nueva fecha de plazo (YYYY-MM-DD)")
        # Crear la consulta de actualización
        sql = "UPDATE proyecto SET nombre = %s, descripcion = %s, fecha_plazo = %s WHERE id_proyecto = %s"
        valores = (nuevo_nombre, nueva_descripcion, fecha_plazo, proyec_id )
        
        # Ejecutar la consulta de actualización
        cursor.execute(sql, valores)
        conn.commit()  # Confirmar la transacción

        # Verificar si se actualizó alguna fila
        if cursor.rowcount > 0:
            print("Proyecto actualizado actualizado exitosamente.")
        else:
            print("ID del departamento no encontrado.")

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

    except Error as err:
        print(f"Error: {err}")

def mostrar_proyecto():
    """
    Conectar a la base de datos, obtener y mostrar autores en un DataFrame
    """
    try:
        conex = conexion()
        if conex is not None:
            cur = conex.cursor()
            # Ejecutar la consulta
            cur.execute("SELECT * FROM proyecto")
            # Obtener los resultados y convertirlos en un DataFrame
            resultados = cur.fetchall()
            columnas = [col[0] for col in cur.description]  # Obtener los nombres de las columnas
            df = pd.DataFrame(resultados, columns=columnas)

        # Mostrar el DataFrame
            print(df)

        # Cerrar la conexión
            cur.close()
            conex.close()
    except Error as err:
        print(f"Error: {err}")

def eliminar_proyecto(nombre):
    """
    Eliminar proyectos
    """
    try:
        conn = conexion()
        cursor = conn.cursor()

        # Crear la consulta de eliminación
        sql = "DELETE FROM proyecto WHERE nombre = %s"
        valores = (nombre,)

        # Ejecutar la consulta de eliminación
        cursor.execute(sql, valores)
        conn.commit()  # Confirmar la transacción

        # Verificar si se eliminó alguna fila
        if cursor.rowcount > 0:
            print("Proyecto eliminado exitosamente.")
        else:
            print("Nombre del proyecto no encontrado.")

        # Cerrar el cursor y la conexión
        cursor.close()
        conn.close()

    except Error as err:
        print(f"Error: {err}")