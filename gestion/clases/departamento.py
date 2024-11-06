from gestion.clases.emplea import Empleados  # Importa la clase Empleados sin alias 

class Departamento:
    def __init__(self, id_depto, nombre):  # Corrige la sintaxis del constructor
        self.id_depto = id_depto
        self.nombre = nombre
