

def buscar_id(lista, id):
    for item in lista:
        if item['id_cliente'] == id:
            return item
    return None