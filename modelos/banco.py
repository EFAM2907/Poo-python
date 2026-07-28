from modelos.cliente import Cliente
from modelos.cuenta_ahorros import CuentaAhorros
from modelos.cuenta_corriente import CuentaCorriente


class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []
        self.cuentas = []
        
    def generador_id(self, lista):
        if not lista:
            return 1
    
        return max(lista, key= lambda elemento : elemento.id_cliente).id_cliente + 1

        
    def crear_cliente(self, nombre, telefono, correo):
        for cliente in self.clientes:
          if cliente.telefono == telefono:
             raise ValueError('Telefono ya existente')
          if cliente.correo == correo:
             raise ValueError('El correo ya esta registrado')
        nuevo_id = self.generador_id(self.clientes)
        nuevo_cliente = Cliente(nuevo_id, nombre, telefono, correo)
        self.clientes.append(nuevo_cliente)
        return nuevo_cliente
        
    
    def buscar_cliente(self, id_cliente):
        if not isinstance(id_cliente, int):
            raise ValueError('Debe ser un numero Entero')
        for usuario in self.clientes:
            if usuario.id_cliente == id_cliente:
                return usuario
            
        return  None
    
    def buscar_cuenta(self, numero_de_cuenta):
        if not isinstance(numero_de_cuenta, int):
          raise ValueError('Debe ser un numero Entero')
        for cuenta in self.cuentas:
            if cuenta.numero_de_cuenta == numero_de_cuenta:
                return cuenta
        return None
    
    
    def crear_cuenta(self, tipo_de_cuenta, id_cliente, numero_de_cuenta, saldo_inicial):
        cliente = self.buscar_cliente(id_cliente)
        if cliente is None:
            raise ValueError('Error, cliente no encontrado')
        if self.buscar_cuenta(numero_de_cuenta) is not None:
            raise ValueError('cuenta ya existente')
        cuenta = tipo_de_cuenta(numero_de_cuenta, cliente, saldo_inicial)
        cliente.agregar_cuenta(cuenta)
        self.cuentas.append(cuenta)
        return cuenta
    
    def crear_cuenta_ahorros(self, id_cliente, numero_de_cuenta, saldo_inicial):
        return self.crear_cuenta(CuentaAhorros,id_cliente, numero_de_cuenta, saldo_inicial )
    
    def crear_cuenta_corriente(self, id_cliente, numero_de_cuenta, saldo_inicial):
        return self.crear_cuenta(CuentaCorriente,id_cliente, numero_de_cuenta, saldo_inicial )
    
    

    def transferir(self, monto, numero_cuenta_origen, numero_cuenta_destino):
        origen = self.buscar_cuenta(numero_cuenta_origen)
        destino = self.buscar_cuenta(numero_cuenta_destino)

        if origen is None:
            raise ValueError('Cuenta origen no encontrada')
        if destino is None:
            raise ValueError('Cuenta destino no encontrada')
        if origen == destino:
            raise ValueError('No puedes transferir a la misma cuenta')
     
        origen.retirar(monto)
        destino.depositar(monto)
        
        return True
    


