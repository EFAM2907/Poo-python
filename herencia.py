class CuentaBancaria:

    def __init__(self, numero_cuenta, titular, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self._saldo = saldo

    def depositar(self, monto):
        self._saldo += monto
    
    @property
    def consultar_saldo(self):
        return self._saldo
    
    
class CuentaAhorros(CuentaBancaria):

    def aplicar_intereses(self, porcentaje):
        interes = self._saldo * (porcentaje / 100)
        self._saldo += interes



cuenta = CuentaAhorros("123", "Edwin", 1000)

print(cuenta.consultar_saldo)

cuenta.depositar(500)

print(cuenta.consultar_saldo)