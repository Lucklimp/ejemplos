from gestion.clases.emplea import Empleados
from gestion.clases.proyecto import Proyecto

class ProyectoEmp(Empleados, Proyecto):
    def __init__(self, id_proyemp, id_proyecto, id_rut):
        self.id_proyemp = id_proyemp
        self.id_proyecto = id_proyecto
        self.id_rut = id_rut