import mysql.connector
from mysql.connector import Error
def conexion():
    '''
    
    establece la conexion a la bd biblioteca
    '''

    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            database = "gestion_empleados_mg",
            user = "root",
            port = 3306
            #password="" 
        )
    except mysql.connector.Error as e:
        print(f"Hubo un error al conectar a la BD {e}")
    else:
        if conexion.is_connected():
            return conexion
        return None
    
