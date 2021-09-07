import coordenadas as cd

#Busca os dados de cidade especifica
def buscar_cidade(cidade):
    for i in cd.coordenadas:
        if i['cidade'] == cidade:
            return i
    return False

#Busca os dados de todas as cidades
def listar_todas_cidades():
    cidades = cd.coordenadas
    return cidades