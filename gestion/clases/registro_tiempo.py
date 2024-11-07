from GESTION.CLASES.proyecto_emp import ProyectoEmp
from datetime import datetime

class RegistroTiempo(ProyectoEmp):
    def _init_(self, id_reg_tiem: int = 0, id_proyemp: int = 0, fecha: str = '', 
                 cant_horas: float = 0, descripcion: str = '', hora_extra: bool = False, 
                 observacion: str = ''):
        super().__init__(id_proyemp)

        self.id_reg_tiem = id_reg_tiem
        self.fecha = self.validar_fecha(fecha) if fecha else None 
        self.cant_horas = cant_horas
        self.descripcion = descripcion
        self.hora_extra = hora_extra
        self.observacion = observacion

        self.validacion_cant_horas()

    def validar_fecha(self, fecha: str) -> datetime:
        try:
            return datetime.strptime(fecha, '%Y-%m-%d')
        except ValueError:
            raise ValueError("La fecha debe estar en el formato 'YYYY-MM-DD'.")

    def validacion_cant_horas(self):
        if self.cant_horas < 0:
            raise ValueError("Cantidad de horas no puede ser negativa.")
        print(f"Horas trabajadas: {self.cant_horas}")

    def _str_(self):
        return (f"ID Registro: {self.id_reg_tiem}, Proyecto ID: {self.id_proyemp}, "
                f"Fecha: {self.fecha.strftime('%Y-%m-%d') if self.fecha else 'No asignada'}, "
                f"Horas: {self.cant_horas}, Descripción: {self.descripcion}, "
                f"Hora Extra: {self.hora_extra}, Observación: {self.observacion}")