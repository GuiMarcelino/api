from flask import Flask, app, request, jsonify
from flask_restful import Resource, Api, reqparse



app = Flask(__name__)
api = Api(app)

exemplo_banco_de_dados = {'nome': 'Guilherme',
                          'sobrenome': 'Marcelino',
                          'idade': 30}

novo_registro = None

parser = reqparse.RequestParser()
parser.add_argument('usuario', type=str)
parser.add_argument('senha', type=str)

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

    def post(self):
        args = parser.parse_args()
        novo_registro = {'usuario': args['usuario'],
                         'senha': args['senha']}
        return jsonify(novo_registro)

api.add_resource(BancoDeDados, '/')

if __name__ == "__main__":
    app.run(debug=True)
