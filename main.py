from modelos.banco import Banco
from menu.operaciones import crear_cliente, crear_cuenta_ahorros, crear_cuenta_corriente, depositar, retirar, transferir, consultar_saldo,listar_clientes
from menu.menu import menu_principal
from utils.entradas import pedir_numero




def menu_de_opciones():
    banco = Banco('Bancolombia')
    while True:
        menu_principal()
        opcion = pedir_numero('Elige una opcion: ')
        
        match opcion:
            case 1:
                if crear_cliente(banco):     
                    print('Cliente creado con exito')
                else:
                    print('No se pudo crear el usuario')
                 
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
                if depositar(banco):
                    print('Depósito realizado con éxito')
            case 5:
                if retirar(banco):
                    print('Retiro realizado con éxito')
            case 6:
                if transferir(banco):
                    print('Transferencia completada')
            case 7:
                consultar_saldo(banco)
            case 8:
                listar_clientes(banco)
            case 9:
                break
            case _:
                print('opcion no valida')
                
if __name__ == '__main__':
    menu_de_opciones()
        




