from .cuenta_bancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):

    def __init__(self, numero_de_cuenta, cliente, saldo):
        super().__init__(numero_de_cuenta, cliente, saldo)
        self.tipo_de_cuenta = 'Corriente'
        self.limite_sobre_giro = 1000

    def _validar_limite_saldo(self, nuevo_saldo):
        return nuevo_saldo >= -self.limite_sobre_giro

    def retirar(self, monto):
        if not isinstance(monto, (int, float)):
            raise ValueError('Deben ser numeros')

        if monto <= 0:
            raise ValueError('el monto no debe ser negativo o cero')

        nuevo_saldo = self._saldo - monto
        if not self._validar_limite_saldo(nuevo_saldo):
            raise ValueError('Retiro rechazado, Excede el limite del sobre giro')

        self._saldo = nuevo_saldo
        return True
