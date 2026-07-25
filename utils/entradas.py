def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            'Debe ser un numero'
            
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print('no debe estar vacio')