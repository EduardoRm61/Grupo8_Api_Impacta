from flask import Flask, jsonify, request

app = Flask(__name__)


professores = {"professor": [
    {"id": 10, "nome": "Caio", "idade": 27, "materia": "Dev API E Micros", "obs": "Contato com aluno via Chat"},
    {"id": 11, "nome": "Odair", "idade": 30, "materia": "DevOps", "obs": None}
]}


class ProfessorNaoIdentificado(Exception):
    def __init__(self, msg="Erro, Professor não identificado ou inexistente!"):
        self.msg = msg
        super().__init__(self.msg)

class ProfessorExistente(Exception):
    def __init__(self, msg="Erro, Professor já existente!"):
        self.msg = msg
        super().__init__(self.msg)

class CadastroDeProfessorFalhado(Exception):
    def __init__(self, msg="Erro, Nome e matéria são obrigatórios!"):
        self.msg = msg
        super().__init__(self.msg)


@app.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify({"mensagem": "Ok", "professor": professores["professor"]}), 200

@app.route("/professores/<int:id>", methods=["GET"])
def pesquisa_professor(id):
    try:
        professor = ProcurarProfessorPorId(id)
        return jsonify({"mensagem": "Ok", "professor": professor}), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404

@app.route('/professores', methods=['POST'])
def cadastrar_professores():
    novo_professor = request.json
    if not novo_professor or "nome" not in novo_professor or "materia" not in novo_professor:
        return jsonify({"erro": "Nome e matéria são obrigatórios"}), 400
    try:
        if professores["professor"]:
            ultimo_professor = professores["professor"][-1]
            novo_id_prof = ultimo_professor["id"] + 1
        else:
            novo_id_prof = 1
        novo_professor["id"] = novo_id_prof
        CriarNovoProfessor(novo_professor)
        return jsonify({"mensagem": "Created", "professor": novo_professor}), 201
    except CadastroDeProfessorFalhado as e:
        return jsonify({"erro": str(e)}), 400

@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    atualizado = request.json
    try:
        professor = ProcurarProfessorPorId(id)
        professor['nome'] = atualizado.get('nome', professor['nome'])
        professor['idade'] = atualizado.get('idade', professor['idade'])
        professor['materia'] = atualizado.get('materia', professor['materia'])
        professor['obs'] = atualizado.get('obs', professor['obs'])
        return jsonify({"mensagem": "Atualizado", "professor": professor}), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404

@app.route("/professores/<int:id>", methods=["DELETE"])
def delete_professor(id):
    try:
        resultado = DeletarProfessorPorId(id)
        return jsonify(resultado), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)