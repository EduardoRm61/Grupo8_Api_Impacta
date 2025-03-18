from flask import Flask, jsonify, request

app = Flask(__name__)


professores = {"professor": [
    {"id": 10, "nome": "Caio", "idade": 27, "materia": "Dev API E Micros", "obs": "Contato com aluno via Chat"},
    {"id": 11, "nome": "Odair", "idade": 30, "materia": "DevOps", "obs": None}
]}

#devido erro persistente de 11 != 12, criou-se um def para ver se para / já a 2 dias neste erro
def gerar_novo_id():
    '''Criação de id, obrigatório'''
    if not professores["professor"]: # Correção: A verificação deve ser na lista de professores
        return 1
    return max(professor["id"] for professor in professores["professor"]) + 1 # Correção: Iterar sobre a lista correta

class ProfessorNaoIdentificado(Exception):
    def __init__(self, msg="Not Found - Professor inexistente"):
        self.msg = msg
        super().__init__(self.msg)

class ProfessorExistente(Exception):
    def __init__(self, msg="Professor já existente"):
        self.msg = msg
        super().__init__(self.msg)

class CadastroDeProfessorFalhado(Exception): # Correção: Nome da classe estava incorreto na chamada do except
    def __init__(self, msg="ID, nome e matéria são obrigatórios"):
        self.msg = msg
        super().__init__(self.msg)


def procurarProfessorPorId(id_professor):   #def é minúscula
    for professor in professores["professor"]:
        if professor['id'] == id_professor:
            return professor
    raise ProfessorNaoIdentificado()

def criarNovoProfessor(nv_dict):
    professores["professor"].append(nv_dict)
    return

def deletarProfessorPorId(id_professor):
    for indice, professor in enumerate(professores["professor"]):
        if professor["id"] == id_professor:
            professores["professor"].pop(indice)
            return {"mensagem": "Professor deletado com sucesso"} # Correção: Retorno estava com ponto final extra
    raise ProfessorNaoIdentificado()

#tratamento de execeção foi atualizado para ficar mais próximo ao feito na turma
#lembrando que, a segui, try - funções que dão certo, except - retono de erro
#chamar função correspondente dentro da rota

@app.route('/professores', methods=['GET'])
def listar_professores():
    try:
        return jsonify({"mensagem": "Ok", "professores": professores["professor"]}) #correção do retorno
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500 # Correção: Mensagem de erro mais clara

@app.route("/professores/<int:id>", methods=["GET"])
def pesquisa_professor(id):
    try:
        professor = procurarProfessorPorId(id)
        return jsonify({"mensagem": "Ok", "professor": professor}), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404

@app.route('/professores', methods=['POST'])
def cadastrar_professores():
    novo_professor = request.json
    if not novo_professor or "nome" not in novo_professor or "materia" not in novo_professor:
        return jsonify({"erro": "Nome e matéria são obrigatórios"}), 400
    try:
        novo_professor["id"] = gerar_novo_id()
        criarNovoProfessor(novo_professor)
        return jsonify({"mensagem": "Created", "professor": novo_professor}), 201

    except CadastroDeProfessorFalhado as e: # Correção: Capturar a exceção correta
        return jsonify({"erro": str(e)}), 400

@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    atualizado = request.json
    try:
        professor = procurarProfessorPorId(id) # Correção: Usar a função de procurarProfessorPorId correta
        if "nome" in atualizado:
            professor['nome'] = atualizado['nome']
        if "idade" in atualizado:
            professor['idade'] = atualizado['idade']
        if "materia" in atualizado:
            professor['materia'] = atualizado['materia']
        if "obs" in atualizado:
            professor['obs'] = atualizado['obs']
        return jsonify({"mensagem": "Atualizado", "professor": professor}), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": f"Internal Server Error: {str(e)}"}) # Correção: Mensagem de erro mais clara

@app.route("/professores/<int:id>", methods=["DELETE"])
def delete_professor(id):
    try:
        resultado = deletarProfessorPorId(id)
        return jsonify(resultado), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)