from datetime import datetime


class CuentaBancaria:

    def __init__(self, numero_de_cuenta, cliente, saldo):
        self.numero_de_cuenta = numero_de_cuenta
        self.cliente = cliente
        if not self._validar_limite_saldo(saldo):
            raise ValueError('El saldo inicial no cumple con los límites de la cuenta')
        self._saldo = saldo
        self.fecha_creacion = datetime.now()

    def __repr__(self):
        return (f"{self.__class__.__name__}(cuenta={self.numero_de_cuenta}, "
                f"cliente={self.cliente.nombre}, saldo={self.saldo})")

    @property
    def saldo(self):
        return self._saldo

    def _validar_limite_saldo(self, nuevo_saldo):
        return nuevo_saldo >= 0

    def _validar_monto(self, monto):
        if not isinstance(monto, (int, float)):
            raise ValueError('Deben ser numeros')
        if monto <= 0:
            raise ValueError('El monto debe ser mayor a cero')

    def validar_retiro(self, monto):
        self._validar_monto(monto)
        nuevo_saldo = self._saldo - monto
        if not self._validar_limite_saldo(nuevo_saldo):
            raise ValueError('Fondos insuficientes')
        return nuevo_saldo


    def validar_deposito(self, monto):
        self._validar_monto(monto)
        nuevo_saldo = self._saldo + monto
        if not self._validar_limite_saldo(nuevo_saldo):
            raise ValueError('El saldo resultante no cumple con los límites de la cuenta')
        return nuevo_saldo

 
    def depositar(self, monto):
        nuevo_saldo = self.validar_deposito(monto)
        self._saldo = nuevo_saldo
        return True    
       
    def retirar(self, monto):
         nuevo_saldo = self.validar_retiro(monto)
         self._saldo = nuevo_saldo
         return True

    def mostrar_informacion(self):
        return f"""
        Tu número de cuenta es: {self.numero_de_cuenta}
        Titular: {self.cliente.nombre}
        Saldo: {self._saldo}
        Fecha de creación: {self.fecha_creacion}
        """
