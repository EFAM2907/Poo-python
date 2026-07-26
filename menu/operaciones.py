from modelos.cliente import Cliente
from utils.entradas import pedir_texto,pedir_numero,pedir_email,pedir_float, pedir_datos_cuenta

def crear_cliente(banco):
    while True:
        try:
           nombre = pedir_texto('Nombre del cliente: ')
           telefono = pedir_numero('Numero de telefono: ')
           correo = pedir_email()
           banco.crear_cliente(nombre, telefono,correo)
           return True
           
        except ValueError as error:
            print(error)
            
            
def crear_cuenta(metodo_de_creacion):
    try:
        id_cliente, numero_cuenta, saldo_inicial = pedir_datos_cuenta()
        metodo_de_creacion(id_cliente, numero_cuenta, saldo_inicial)
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False
    
    
def crear_cuenta_ahorros(banco):
    return crear_cuenta(banco.crear_cuenta_ahorros)
    
def crear_cuenta_corriente(banco):
    return crear_cuenta(banco.crear_cuenta_corriente)


    
