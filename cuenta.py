from datetime import datetime


class CuentaBancaria:

    def __init__(
        self,
        numero_cuenta,
        titular,
        saldo,   
        tipo_cuenta
    ):
        self.numero_cuenta= numero_cuenta
        self.titular = titular
        self.__saldo = saldo
        self.tipo_cuenta = tipo_cuenta
        self.fecha_creacion = datetime.now()
    def depositar(self, monto):
        
        if not isinstance(monto, (int, float)):
            return 'Deben ser numeros'
        
        if monto <= 0:
            return 'El valor no puede ser menor a 0'
        
        monto_max = 10000000
        if monto > monto_max:
            return 'el monto no puede ser mayor a 10.000.000'
        
        self._saldo += monto
        
        
    @property
    def saldo(self):    
        return self.__saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
     if nuevo_saldo < 0:
        print("El saldo no puede ser negativo.")
        return

     self._saldo = nuevo_saldo
    def mostrar_informacion(self):
            return f"""
                Tu número de cuenta es: {self.numero_cuenta}
                Titular: {self.titular}
                Saldo: {self._saldo}
                Tipo de cuenta: {self.tipo_cuenta}
                Fecha de creación: {self.fecha_creacion}
                """
    
    def retirar(self, monto):
        if not isinstance(monto, (int, float)):
            return 'Deben ser números'
    
        if monto <= 0:
            return 'El monto debe ser mayor a cero'
    
        if monto > self._saldo:
             return 'Saldo insuficiente'
    
        self._saldo -= monto
        return f'Retiro exitoso. Saldo actual: {self._saldo}'


edwin_cuenta = CuentaBancaria(1007504456, 'Edwin Arias', 100, 'Ahorros')

#edwin_cuenta.retirar(-100)
edwin_cuenta.saldo = 2
print(edwin_cuenta.mostrar_informacion()) 

