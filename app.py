from flask import Flask, jsonify, request

# Dados iniciais dos professores
professores = {
    "professor": [
        {"id": 10, "nome": "Caio", "idade": 27, "materia": "Dev API E Micros", "obs": "Contato com aluno via Chat"},
        {"id": 11, "nome": "Odair", "idade": 30, "materia": "DevOps", "obs": None}
    ]
}

app = Flask(__name__)

# Rota para listar todos os professores
@app.route('/professores', methods=['GET'])
def listar_professores():
    
    return jsonify({"mensagem": "Ok", "professor": professores["professor"]}), 200

# Rota para buscar um professor por ID
@app.route("/professores/<int:id>", methods=["GET"])
def pesquisa_professor(id):
    for professor in professores["professor"]:
        if professor["id"] == id:
            return jsonify({"mensagem": "Ok", "professor": professor}), 200
    return jsonify({"error": "Not Found - Professor inexistente"}), 404

# Rota para cadastrar um novo professor
@app.route('/professores', methods=['POST'])
def cadastrar_professores():
    novo_professor = request.json

    # Verifica se os campos obrigatórios estão presentes
    if not novo_professor or "nome" not in novo_professor or "materia" not in novo_professor:
        return jsonify({"error": "Nome e matéria são obrigatórios"}), 400

    # Gera um novo ID para o professor
    if professores["professor"]:
        ultimo_professor = professores["professor"][-1]
        novo_id_prof = ultimo_professor["id"] + 1                                       
    else:
        novo_id_prof = 1

    
    professores["professor"].append(novo_professor)

    return jsonify({"mensagem": "Created", "professor": novo_professor}), 201
 

# Rota para atualizar um professor existente
@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    atualizado = request.json
    for professor in professores["professor"]:
        if professor['id'] == id:
            professor['nome'] = atualizado.get('nome', professor['nome'])
            professor['idade'] = atualizado.get('idade', professor['idade'])
            professor['materia'] = atualizado.get('materia', professor['materia'])
            professor['obs'] = atualizado.get('obs', professor['obs'])
            return jsonify({"mensagem": "Atualizado", "professor": professor}), 200
    return jsonify({"error": "Not Found - Professor inexistente"}), 404

# Rota para deletar um professor
@app.route("/professores/<int:id>", methods=["DELETE"])
def delete_professor(id):
    for professor in professores["professor"]:
        if professor["id"] == id:
            professores["professor"].remove(professor)
            return jsonify({"mensagem": "Deletado", "professor": professor}), 200
    return jsonify({"error": "Not Found - Professor inexistente"}), 404

if __name__ == '__main__':
    app.run(debug=True) 