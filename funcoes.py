import coordenadas as cd

#Busca os dados de cidade especifica
def buscar_cidade(cidade):
    cidades = cd.coordenadas
    for i in cidades:
        if i['cidade'] == cidade:
            return i
    return False

#Busca todas as cidades
def buscar_todas_cidades():
    cidades = cd.coordenadas
    return cidades