from os import error
from flask import Flask
from flask.templating import render_template
from flask_restful import Resource, Api
from funcoes import *

app = Flask(__name__)
api = Api(app)

class Coordenadas(Resource):

    def get(self, cidade):
        try:
            resul = buscar_cidade(cidade.upper())
            if resul:
                response = {
                    "lat":resul['lat'],
                    "lon":resul['lon']
                }
                return response
            else:
                response = {
                    "erro":"Cidade {} nao encontrada.".format(cidade)
                }
                return response
        except:
            response = {
                    "erro":"Erro ao tentar buscar cidade {}.".format(cidade)
                }
            return response

class Cidades(Resource):

    def get(self):
        try:
            resul = buscar_todas_cidades()
            return resul
        except:
            response = {
                    "erro":"Erro ao tentar listar as cidades."
                }
            return response

@app.route('/')
def inicial():
    return render_template('inicio.html')

api.add_resource(Coordenadas, '/valedoparaiba/coordenadas/<string:cidade>/')
api.add_resource(Cidades, '/valedoparaiba/')

if __name__ == '__main__':
    app.run()