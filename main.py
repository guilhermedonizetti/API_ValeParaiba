from flask import Flask
from flask_restful import Resource, Api
from funcoes import *

app = Flask(__name__)
api = Api(app)

class Coordenadas(Resource):

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

api.add_resource(Coordenadas, '/valedoparaiba/coordenadas/<string:cidade>')

if __name__ == '__main__':
    app.run()