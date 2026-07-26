from datetime import datetime


class CuentaBancaria:

    def __init__(self, numero_de_cuenta, cliente, saldo):
        self.numero_de_cuenta = numero_de_cuenta
        self.cliente = cliente
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

    def depositar(self, monto):
        if not isinstance(monto, (int, float)):
            raise ValueError('Deben ser numeros')

        if monto <= 0:
            raise ValueError('El valor no puede ser negativo o cero')

        nuevo_saldo = self._saldo + monto
        if not self._validar_limite_saldo(nuevo_saldo):
            raise ValueError('El saldo resultante no cumple con los límites de la cuenta')

        self._saldo = nuevo_saldo
        return True

    def retirar(self, monto):
        if not isinstance(monto, (int, float)):
            raise ValueError('Deben ser numeros')

        if monto <= 0:
            raise ValueError('el monto no debe ser negativo o cero')

        nuevo_saldo = self._saldo - monto
        if not self._validar_limite_saldo(nuevo_saldo):
            raise ValueError('Fondos insuficientes')

        self._saldo = nuevo_saldo
        return True

    def mostrar_informacion(self):
        return f"""
        Tu número de cuenta es: {self.numero_de_cuenta}
        Titular: {self.cliente.nombre}
        Saldo: {self._saldo}
        Fecha de creación: {self.fecha_creacion}
        """
