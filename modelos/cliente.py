from .cuenta_bancaria import CuentaBancaria
from datetime import datetime


class Cliente:
    def __init__(self,id_cliente,nombre,telefono,correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.fecha_registro = datetime.now() 
        self.cuentas =[]
        
        
    def __repr__(self):
     return f"Cliente({self.id_cliente}, '{self.nombre}', {self.telefono}, '{self.correo}')"

    def agregar_cuenta(self,new_cuenta):
        if not isinstance(new_cuenta, CuentaBancaria):
            return 'New_cuenta debe ser un instace de CuentaBancaria'
        
        for cuenta in self.cuentas:
            if cuenta == new_cuenta:
                return 'Cuenta ya existente'
        self.cuentas.append(new_cuenta)
        return "Cuenta agregada correctamente"
            
    def mostrar_cuentas(self):
        for cuenta in self.cuentas:
            print(f"""
                  {cuenta.numero_de_cuenta}
                  {cuenta.cliente.nombre}
                  {cuenta.saldo}
                  """)