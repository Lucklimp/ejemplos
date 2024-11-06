from cryptography.fernet import Fernet
import re
#from prettytable import prettytable
from gestion.clases.tipo_emp import TipoEmpleados  
from gestion.clases.role import Rol
#table = prettytable.PrettyTable()

class Empleados(TipoEmpleados, Rol) :
    clave = Fernet.generate_key()
    cipher_suite = Fernet(clave)

    def __init__(self, id_rut, nombre , fecha_nac , fecha_contrato , sueldo, correo , telefono , direccion , id_rol , id_tipo , nom_usuario , password ):
        super.__init__(id_tipo)  # Llamar directamente a los constructores
        super.__init__(id_rol )
        self.id_rut = id_rut
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.fecha_contrato = fecha_contrato
        self.sueldo = sueldo
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.nom_usuario = nom_usuario
        self.password = self.encriptar_clave(password)

    def encriptar_clave(self, password):
        if password:
            return self.cipher_suite.encrypt(password.encode())
        return ""
    
    def desencriptar_clave(self):
        if self.password:
            return self.cipher_suite.decrypt(self.password).decode()
        return ""

    def validar_datos(self):
        # Valida datos básicos sin solicitar entrada
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.correo):
            raise ValueError("Correo no válido.")
        if not re.match(r"\d{9,15}", self.telefono):
            raise ValueError("Teléfono no válido.")
        
    def __str__(self):
        return (f"ID RUT: {self.id_rut}, Nombre: {self.nombre}, Fecha Nac: {self.fecha_nac}, "
                f"Fecha Contrato: {self.fecha_contrato}, Sueldo: {self.sueldo}, Correo: {self.correo}, "
                f"Teléfono: {self.telefono}, Dirección: {self.direccion}, ID Rol: {self.id_rol}, "
                f"ID Tipo: {self.id_tipo}, Nombre de Usuario: {self.nom_usuario}")
    
   
