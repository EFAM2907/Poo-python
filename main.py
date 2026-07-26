from modelos.banco import Banco
from menu.operaciones import crear_cliente, crear_cuenta_ahorros,crear_cuenta_corriente
from menu.menu import menu_principal
from utils.entradas import pedir_numero

def menu_de_opciones():
    banco = Banco('Bancolombia')
    while True:
        menu_principal()
        opcion = pedir_numero('Elige una opcion: ')
        
        match opcion:
            case 1:
                cliente = crear_cliente(banco)     
                if cliente:
                    print('Cliente creado con exito')
                else:
                     print('no se pudo crear el usuario')
                 
            case 2:
                 if crear_cuenta_ahorros(banco):
                     print('Cuenta creada con éxito')
                 else:
                     print('No se pudo crear la cuenta')
            case 3:
                 if crear_cuenta_corriente(banco):
                     print('Cuenta creada con éxito')
                 else:
                     print('No se pudo crear la cuenta')
            case 4:
                print('crear cliente')
            case 5:
                print('crear cliente')
            case 6:
                print('crear cliente')
            case 7:
                print('crear cliente')
            case 8:
                print(banco.cuentas)
            case 9:
                break
            case _:
                print('opcion no valida')
                
menu_de_opciones()
        
        
        # if opcion == 1:
        #     print('crear cliente')
        # elif opcion == 2:
        #     print('Crear cuenta de ahorros') 
        # elif opcion == 3:
        #     print('Crear cuenta corriente')
        # elif opcion == 4:
        #     print('Depositar')
        # elif opcion == 5:
        #     print('Retirar')
        # elif opcion == 6:
        #     print('Transferir')
        # elif opcion == 7:
        #     print('Depositar') 
        # elif opcion == 8:
        #     print('Lista clientes')
        # elif opcion == 9:
        #     break



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



