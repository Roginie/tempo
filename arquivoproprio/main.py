from flask import Flask, jsonify, make_response, request
from bd2 import Tempo

app = Flask ('tempo')

@app.route('/tempo', methods=['GET'])
def GET_tempo():
    return jsonify(Tempo) 

@app.route('/tempo/<int:id>', methods=['GET'])
def get_tempo_id(id):
    for tempo in Tempo:
        if tempo.get('id') == id:
            return jsonify(tempo)

@app.route('/tempo', methods=['POST'])
def cria_tempo():
    tempo = request.json
    Tempo.append(tempo)
    return make_response(
        jsonify(mensagem='Novo tempo atualizado com sucesso !!!', tempo=tempo)

    )

@app.route('/tempo/<int:id>', methods=['PUT'])
def editar_tempo_id(id):
    tempo_alterado = request.get_json()
    for indice, tempo in enumerate(Tempo):
        if tempo.get('id') == id:
            Tempo[indice].update(tempo_alterado)
            return jsonify(Tempo[indice])
        
        return jsonify({'mensagem:': 'tempo excluido com sucesso !!!'})
    
app.run(port=5000, host='localhost')