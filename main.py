from flask import Flask, render_template
from flask_restful import Resource, Api
from funcoes import *

app = Flask(__name__)
api = Api(app)

#CLASSE PARA COORDENADAS
class Coordenadas(Resource):

    #Busca os dados de uma cidade especifica
    def get(self, cidade):
        try:
            resul = buscar_cidade(cidade.upper())
            if resul:
                resul.pop('cidade')
                return resul
            else:
                response = {
                    "erro":"Cidade {} nao encontrada.".format(cidade)
                }
                return response
        except:
            response = {
                    "erro":"Erro ao tentar consultar coordenada da cidade."
                }
            return response

#CLASSE PARA CIDADES
class Cidades(Resource):

    #Busca os dados de todas as cidades
    def get(self):
        try:
            resul = listar_todas_cidades()
            return resul
        except:
            response = {
                    "erro":"Erro ao tentar consultar coordenada da cidade."
                }
            return response

#Retorna os links para acesso a raiz da API
@app.route('/')
def pagina_inicial():
    return render_template('inicio.html')

#REGISTRO DAS ROTAS
api.add_resource(Coordenadas, '/valedoparaiba/coordenadas/<string:cidade>/')
api.add_resource(Cidades, '/valedoparaiba/')

if __name__ == '__main__':
    app.run()