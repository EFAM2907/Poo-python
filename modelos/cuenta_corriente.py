from cuenta_bancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_de_cuenta, cliente, saldo):
        super().__init__(numero_de_cuenta, cliente, saldo)
        self.tipo_de_cuenta = 'Corriente'
        self.limite_sobre_giro = 1000
        
        
    def retirar(self, monto):
        if not isinstance(monto, (int, float)):
            return 'Deben ser numeros'
        if self.saldo - monto < -self.sobre_giro:
            return 'Retiro rechazado, Excede el limite del sobre giro'
        self.saldo -= monto
        return f'Retiro Exitoso, tu nuevo saldo es {self._saldo}'
    
    
    



