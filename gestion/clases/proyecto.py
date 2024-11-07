class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion, fecha_inicio, fecha_plazo):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_plazo = fecha_plazo

    def validar_fecha(self):
        # Lógica para validar fechas
        if self.fecha_inicio > self.fecha_plazo:
            raise ValueError("La fecha de inicio no puede ser posterior a la fecha plazo.")