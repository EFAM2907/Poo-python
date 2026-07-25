from cuenta_bancaria import CuentaBancaria
from cuenta_ahorros import CuentaAhorros
from cuenta_corriente import CuentaCorriente
from cliente import Cliente



edwin = Cliente(1, 'Edwin', 3023037807, 'efam@gmail.com')
#fernando = Cliente(2,'Fernando Montoya', 3245647895, 'fer@gmail.com')

cuenta_ahorros = CuentaAhorros(1007504456, edwin, 100, 'Ahorros')
cuenta_corriente = CuentaCorriente(5266456494, edwin, 500, 'Corriente', 200)


print(edwin.agregar_cuenta(cuenta_ahorros))
print(edwin.agregar_cuenta(cuenta_corriente))


print(edwin.mostrar_cuentas())