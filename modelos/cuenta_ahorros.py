from cuenta_bancaria import CuentaBancaria
from cliente import Cliente

class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_de_cuenta, cliente, saldo):
        super().__init__(numero_de_cuenta, cliente, saldo)
        self.tipo_de_cuenta = 'ahorros'


    def aplicar_intereses(self, porcentaje):
        interes = self._saldo * (porcentaje / 100)
        self._saldo += interes



# edwin = Cliente(1,'edwin', 3023037807, 'efam@gmail.com')

# cuenta1 = CuentaAhorros(123456, edwin, 2000, 'ahorros')

# edwin.agregar_cuenta(cuenta1)


