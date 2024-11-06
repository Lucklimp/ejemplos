class TipoEmpleados:
    def __init__(self, id_tipo, tipo):
        self.id_tipo = id_tipo
        self.tipo = tipo
    
    def __str__(self):
        return f"ID Tipo: {self.id_tipo}, Tipo de Empleado: {self.tipo}"
    
    #Método de ejemplo para modificar el tipo de empleado
    def cambiar_tipo(self, nuevo_tipo):
        self.tipo = nuevo_tipo
