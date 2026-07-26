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
        
def pedir_email():
    while True:
        email = pedir_texto("Correo electronico: ")

        if "@" not in email:
            print("El correo debe contener un '@'.")
            continue

        if "." not in email:
            print("El correo debe contener un punto.")
            continue

        if email.rindex(".") < email.index("@"):
            print("El punto debe estar después del '@'.")
            continue

        return email


def pedir_datos_cuenta():
        id_cliente = pedir_numero('ID del cliente: ')
        numero_cuenta = pedir_numero('Numero de cuenta: ')
        saldo_inicial = pedir_float('Saldo inicial: ')
        
        return id_cliente, numero_cuenta, saldo_inicial