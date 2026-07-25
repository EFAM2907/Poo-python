from datetime import datetime


class CuentaBancaria:

    def __init__(
        self,
        numero_de_cuenta,
        cliente,
        saldo
    ):
        self.numero_de_cuenta= numero_de_cuenta
        self.cliente = cliente
        self._saldo = saldo
        self.fecha_creacion = datetime.now()
        
        
    def __repr__(self):
        return (f"{self.__class__.__name__}(cuenta={self.numero_de_cuenta}, "
                f"cliente={self.cliente.nombre}, saldo={self.saldo})")
        
        
    def depositar(self, monto):
        if not isinstance(monto, (int, float)):
            return False

        if monto <= 0:
            return False

        self._saldo += monto
        return True
        
    @property
    def saldo(self):    
        return self._saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
     if nuevo_saldo < 0:
        print("El saldo no puede ser negativo.")
        return

     self._saldo = nuevo_saldo
    def mostrar_informacion(self):
            return f"""
                Tu número de cuenta es: {self.numero_de_cuenta}
                Titular: {self.cliente.nombre}
                Saldo: {self._saldo}
                Fecha de creación: {self.fecha_creacion}
                """
    
    def retirar(self, monto):
        if not isinstance(monto, (int, float)):
            return False

        if monto <= 0:
            return False

        if monto > self._saldo:
            return False

        self._saldo -= monto
        return True


# edwin_cuenta = CuentaBancaria(1007504456, 'Edwin Arias', 100, 'Ahorros')

# #edwin_cuenta.retirar(-100)
# edwin_cuenta.saldo = 2
# print(edwin_cuenta.mostrar_informacion()) 

