from .cuenta_bancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):

    def __init__(self, numero_de_cuenta, cliente, saldo):
        self.limite_sobre_giro = 1000
        super().__init__(numero_de_cuenta, cliente, saldo)
        self.tipo_de_cuenta = 'Corriente'

    def _validar_limite_saldo(self, nuevo_saldo):
        return nuevo_saldo >= -self.limite_sobre_giro
