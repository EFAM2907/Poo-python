from utils.entradas import pedir_texto,pedir_numero,pedir_email,pedir_float, pedir_datos_cuenta

def crear_cliente(banco):
    while True:
        try:
           nombre = pedir_texto('Nombre del cliente: ')
           telefono = pedir_numero('Numero de telefono: ')
           correo = pedir_email()
           banco.crear_cliente(nombre, telefono, correo)
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


def gestionar_transaccion(banco, tipo_transaccion):
    numero_de_cuenta = pedir_numero('Cual es el numero de cuenta: ')
    cuenta = banco.buscar_cuenta(numero_de_cuenta)
    
    if not cuenta:
        print('No se encontro la cuenta')
        return False
        
    try:
        monto = pedir_float(f'Valor a {tipo_transaccion}: ')
        operacion = getattr(cuenta, tipo_transaccion)
        operacion(monto)
        return True
    except ValueError as error:
        print(error)
        return False

def depositar(banco):
    return gestionar_transaccion(banco, 'depositar')

def retirar(banco):
    return gestionar_transaccion(banco, 'retirar')

def transferir(banco):
    try:
        origen = pedir_numero('Numero de cuenta origen: ')
        destino = pedir_numero('Numero de cuenta destino: ')
        monto = pedir_float('Valor a transferir: ')
        
        banco.transferir(monto, origen, destino)
        return True
    except ValueError as error:
        print(f"Error en los datos de entrada: {error}")
        return False


#consultas
   
def consultar_saldo(banco):
    numero_de_cuenta = pedir_numero('Numero de cuenta: ')
    cuenta = banco.buscar_cuenta(numero_de_cuenta)

    if cuenta is None:
        print('No se encontro la cuenta')
        return False

    print(f'Saldo de la cuenta {cuenta.numero_de_cuenta}: {cuenta.saldo}')
    return True


def listar_clientes(banco):
    if not banco.clientes:
        print('No hay clientes registrados')
        return False

    print('\nClientes registrados:')
    for cliente in banco.clientes:
        print(f'ID: {cliente.id_cliente} | Nombre: {cliente.nombre} | '
              f'Telefono: {cliente.telefono} | Correo: {cliente.correo}')
    return True
