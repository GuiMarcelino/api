from flask import Flask, app, request
from flask_restful import Resource, Api



app = Flask(__name__)
api = Api(app)

exemplo_banco_de_dados = {'nome': 'Guilherme',
                          'sobrenome': 'Marcelino',
                          'idade': 30}


class BancoDeDados(Resource):
    def get(self):
        return exemplo_banco_de_dados

    def put(self):
        email = request.form['email']
        exemplo_banco_de_dados.update({'email' : email})
        return {'email' : email}

    def delete(self):
       resultado = exemplo_banco_de_dados.pop('idade')
       return resultado


api.add_resource(BancoDeDados, '/')

if __name__ == "__main__":
    app.run(debug=True)
