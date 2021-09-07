import coordenadas as cd

def buscar_cidade(cidade):
    for i in cd.coordenadas:
        if i['cidade'] == cidade:
            return i
    return False    