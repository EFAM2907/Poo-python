from modelos.cliente import Cliente
from modelos.cuenta_ahorros import CuentaAhorros
from modelos.cuenta_corriente import CuentaCorriente


class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []
        self.cuentas = []
        
    def generador_id(lista):
        if not lista:
            return 1
    
        return max(lista, key= lambda elemento : elemento['id'])['id']+1

        
    def crear_cliente(self, nombre,telefono,correo):
        for cliente in self.clientes:
          if cliente.telefono == telefono:
             raise ValueError('Telefono ya existente')
          if cliente.correo == correo:
             raise ValueError('El correo ya esta registrado')
        nuevo_id = self.generador_id(self.clientes)
        nuevo_cliente = Cliente(nuevo_id, nombre, telefono,correo)
        self.clientes.append(nuevo_cliente)
        return nuevo_cliente
        
    # def agregar_cliente(self, cliente):
    #     if not isinstance(cliente, Cliente):
    #         return 'Debe ser un cliente'
    #     for usuario in self.clientes:
    #         if usuario.id_cliente == cliente.id_cliente:
    #             return 'El usuario ya existe'
    #     self.clientes.append(cliente)
    #     return'Se agrego el cliente correctamente'
    
    def buscar_cliente(self, id_cliente):
        if not isinstance(id_cliente, int):
            return 'Debe ser un numero Entero'
        for usuario in self.clientes:
            if usuario.id_cliente == id_cliente:
                return usuario
            
        return  None
    
    def buscar_cuenta(self, numero_de_cuenta):
        if not isinstance(numero_de_cuenta, int):
          return 'Debe ser un numero entero'
        for cuenta in self.cuentas:
            if cuenta.numero_de_cuenta == numero_de_cuenta:
                return cuenta
        return None
    
    def eliminar_cliente(self, id_cliente):
        if not isinstance(id_cliente, int):
            return 'Debe ser un numero Entero'
        cliente = self.buscar_cliente(id_cliente)
        if cliente is None:
         return 'Cliente no encontrado'
          
        self.clientes.remove(cliente)
        return 'Cliente eliminado Correctamente'
    
    def crear_cuenta_ahorros(self, id_cliente, numero_de_cuenta, saldo_inicial):
        cliente = self.buscar_cliente(id_cliente)
        if cliente is None:
            return 'Error, cliente no encontrado'
        cuenta = CuentaAhorros(numero_de_cuenta, cliente,saldo_inicial)
        cliente.agregar_cuenta(cuenta)
        self.cuentas.append(cuenta)

        return cuenta
    
    def crear_cuenta_corriente(self, id_cliente, numero_de_cuenta, saldo_inicial):
        cliente = self.buscar_cliente(id_cliente)
        if cliente is None:
            return 'Error, cliente no encontrado'
        cuenta = CuentaCorriente(numero_de_cuenta, cliente,saldo_inicial)
        cliente.agregar_cuenta(cuenta)
        self.cuentas.append(cuenta)
        return cuenta
    
    

    def transferir(self, monto, cuenta_origen, cuenta_destino):
         if monto <= 0:
             raise ValueError('Error, el monto debe ser positivo')
         
         origen = self.buscar_cuenta(cuenta_origen)
         destino = self.buscar_cuenta(cuenta_destino)

         if origen is None:
             return 'Error, cuenta origen no encontrada'
         if destino is None:
             return 'Error, cuenta destino no encontrada'
         if origen == destino:
             return 'Error, no puedes transferir a la misma cuenta'

         
        #  if not origen.retirar(monto):
        #     return 'Error, no se pudo retirar (saldo insuficiente)'

         destino.depositar(monto)
         return 'Transferencia exitosa'
    
banco_cuenta = Banco('Bancolombia')
# cliente1 = Cliente(1, 'Edwin', 3023037807, 'efam@gmail.com')
# cliente2 = Cliente(2, 'fernando', 3083037807, 'fer@gmail.com')


# banco_cuenta.agregar_cliente(cliente1)
# banco_cuenta.agregar_cliente(cliente2)

# banco_cuenta.crear_cuenta_ahorros(1, 65108457869, 20_000)
# banco_cuenta.crear_cuenta_ahorros(2, 3510761852, 50_000)

# print(banco_cuenta.cuentas)
# print(banco_cuenta.transferir(5000, 65108457869, 3510761852))  # Edwin -> Fernando, debería ser exitosa
# print(banco_cuenta.transferir(5000, 999999999, 6510761852))    # origen falso, debería avisar
# print(banco_cuenta.transferir(5000, 65108457869, 999999999))   # destino falso, debería avisar

# print(banco_cuenta.cuentas)
