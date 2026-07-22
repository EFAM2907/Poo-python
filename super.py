class CuentaBancaria():
    def __init__(self, numero_de_cuenta,titular,saldo):
        self.numero_de_cuenta = numero_de_cuenta
        self.titular = titular
        self._saldo = saldo
        
        
    def consultar_saldo(self):
        return self._saldo
    
    def mostrar_info(self):
        print(f"""
        Cuenta: {self.numero_de_cuenta}
        Titular: {self.titular}
        Saldo: {self._saldo}
        """)
    
class CuentaAhorros(CuentaBancaria):
    pass
        
        
cuenta = CuentaAhorros(
    12345,
    "Edwin",
    5000,
    
)

print(cuenta.consultar_saldo())