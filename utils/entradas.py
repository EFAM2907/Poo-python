import re


def pedir_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print('Debe ser un número válido (ejemplo: 1000 o 1000.50)')
            
def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('Debe ser un numero')
            
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print('no debe estar vacio')
        

def pedir_email(mensaje='Correo electronico: '):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    while True:
        correo = input(mensaje).strip()
        if re.match(patron, correo):
            return correo
        print('Correo invalido, intenta de nuevo')

def pedir_datos_cuenta():
        id_cliente = pedir_numero('ID del cliente: ')
        numero_cuenta = pedir_numero('Numero de cuenta: ')
        saldo_inicial = pedir_float('Saldo inicial: ')
        
        return id_cliente, numero_cuenta, saldo_inicial