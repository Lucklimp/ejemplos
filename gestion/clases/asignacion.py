
from GESTION.CLASES.departamento import Departamento
from GESTION.CLASES.empleados import Empleados
class Asignacion(Empleados):
    def _init_(self, id_asig=0, id_depto=0, id_rut=0, **kwargs):
        super().__init__(id_rut, **kwargs)
        self.id_asig = id_asig
        self.id_depto = id_depto

    def validar_asignacion(self, db):
        empleado = db.query(Empleados).get(self.id_rut)
        departamento = db.query(Departamento).get(self.id_depto)
        if not empleado or not departamento:
            raise ValueError("Empleado o departamento no encontrado.")
        
        existing_assignments = db.query(Asignacion).filter_by(id_rut=self.id_rut).filter(Asignacion.id_asig != self.id_asig).all()
        if existing_assignments:
            raise ValueError("El empleado ya está asignado a otro departamento.")

    def asignar(self, db):
        try:
            self.validar_asignacion(db)
            new_asignacion = Asignacion(id_asig=self.id_asig, id_depto=self.id_depto, id_rut=self.id_rut)
            db.session.add(new_asignacion)
            db.session.commit()
        except ValueError as ve:
            db.session.rollback()
            raise ve  # Re-raise the specific ValueError
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error al asignar empleado: {str(e)}")

    def reasignar(self, db, nuevo_depto_id):
        try:
            nuevo_depto = db.query(Departamento).get(nuevo_depto_id)
            if not nuevo_depto:
                raise ValueError("El nuevo departamento no existe.")

            # Verificar si el empleado ya está asignado a un departamento
            existing_assignment = db.query(Asignacion).filter_by(id_rut=self.id_rut).first()
            if not existing_assignment:
                raise ValueError("El empleado no está asignado a ningún departamento.")

            # Actualizar la asignación del departamento
            existing_assignment.id_depto = nuevo_depto_id
            db.session.commit()
            print(f"Empleado {self.id_rut} reasignado al departamento {nuevo_depto_id}")

        except ValueError as ve:
            db.session.rollback()
            raise ve  # Re-raise the specific ValueError
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error al reasignar empleado: {str(e)}")