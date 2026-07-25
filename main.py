from modelos.banco import Banco
from menu.operaciones import crear_cliente
from menu.menu import menu_principal
from utils.entradas import pedir_numero

def menu_de_opciones():
    while True:
        menu_principal()
        banco = Banco('Bancolombia')
        opcion = pedir_numero('Elige una opcion')
        if opcion == 1:
            print('crear cliente')
        elif opcion == 2:
            print('Crear cuenta de ahorros') 
        elif opcion == 3:
            print('Crear cuenta corriente')
        elif opcion == 4:
            print('Depositar')
        elif opcion == 5:
            print('Retirar')
        elif opcion == 6:
            print('Transferir')
        elif opcion == 7:
            print('Depositar') 
        elif opcion == 8:
            print('Lista clientes')
        elif opcion == 9:
            break

menu_de_opciones()

# bancolombia = Banco('Bancolombia')
# cliente1 = Cliente(1, 'Edwin', 3023037807, 'efam@gmail.com')
# cliente2 = Cliente(2, 'fernando', 3083037807, 'fer@gmail.com')
# cliente3 = Cliente(3, 'arias', 3083037807, 'ari@gmail.com')


# bancolombia.agregar_cliente(cliente1)
# bancolombia.agregar_cliente(cliente2)
# bancolombia.agregar_cliente(cliente3)

# bancolombia.crear_cuenta_ahorros(1, 65108457869, 20_000)
# bancolombia.crear_cuenta_ahorros(2, 35108457869, 40_000)
# bancolombia.crear_cuenta_corriente(3, 45651657840,10_000)

#print(bancolombia.transferir(5000, 35108457869, 65108457869))



