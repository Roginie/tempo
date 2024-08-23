#API -> e um lugar para disponibilizar recursos e ou fucinalidade  uma ponte
#endpoints








from flask import Flask, jsonify, make_response, request
from bd import Carros

#intancia o modulo Flask na nossa variavel app
app = Flask ('carros')

#primeiro metodo - visualizar os dados (GET)
#app.route -> define que essa funcao e uma rota para que o flask entender quele metodo precisa ser execultado
@app.route('/carros', methods=['GET'])
def GET_carros():
    return Carros

#app.run(port=5000, host='localhost')

#primeiro metodo parte 2 - Visualizad=r dados pr ID (GET / ID)
@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_id(id):
    for carros in Carros:
        if carros.get('id') == id:
            return jsonify(carros)

#app.run(port=5000, host='localhost')

#SEGUNDO METODO - CRIA NOVOS DADOS (POST)
@app.route('/carros', methods=['POST'])
def criar_carros():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(mensagem='Carro cadastrado com sucesso !!!', carro=carro)
                
    )
#app.run(port=5000, host='localhost')

#TERCEIRO METODO  - EDITAR DADOS (PUT)
@app.route('/carros', methods=['PUT'])
def editar_carro_id(id):
    carro_alterado = request.get_json()
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            Carro[indice].update(carro_alterado)
            return jsonify(Carros[indice])

#app.run(port=5000, host='localhost')
# QUARTO METODO DELETAR DADOS (DELETE)
@app.route('/carros/<int:id>', methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(Carros):
        if carro.get('id') == id:
            del Carros[indice]
            return jsonify({'mensagem:': 'carro excluido com sucesso !!!'})


app.run(port=5000, host='localhost')