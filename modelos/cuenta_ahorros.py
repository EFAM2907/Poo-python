from .cuenta_bancaria import CuentaBancaria


class CuentaAhorros(CuentaBancaria):

    def __init__(self, numero_de_cuenta, cliente, saldo):
        super().__init__(numero_de_cuenta, cliente, saldo)
        self.tipo_de_cuenta = 'ahorros'

    def aplicar_intereses(self, porcentaje):
        interes = self._saldo * (porcentaje / 100)
        self._saldo += interes
