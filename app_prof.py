from flask import Flask, jsonify, request
import model_turma as modTur
app = Flask(__name__)
                
# Todas as rotas:

@app.route("/reseta", methods=["POST","DELETE"])
def reseta():
    apaga_tudo()
    return "resetado" 

# apenas professores - juntar- se correto à app.py

@app.route('/professores', methods=['GET'])
def listar_professores():
    
    '''Devolve list/dict de todos professores'''
    
    try:
        return jsonify({"mensagem": "Ok", "professores": professores["professor"]}) 
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500 
    #posso trocar para 404 not found? 500 é erro interno

@app.route("/professores/<int:id>", methods=["GET"])
def pesquisa_professor(id):
    
    '''Devolve dict com base no id (chave/pk)'''
    
    try:
        professor = procurarProfessorPorId(id)
        return jsonify({"mensagem": "Ok", "professor": professor}), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404
    
###########################################
@app.route('/professores', methods=['POST'])
def cadastrar_professores():
    
    '''Add novo professor a list/dict'''
    
    novo_professor = request.json
    if not novo_professor or "nome" not in novo_professor or "materia" not in novo_professor:
        return jsonify({"erro": "Nome e matéria são obrigatórios"}), 400
    #aqui deve ter nome, id e matéria obrigatório
    
    try:
        if modTur.ProfessorExistente(novo_professor["id"]):  # Correção: Verifica se o professor já existe
            raise ProfessorExiste("Professor já existe")
        criarNovoProfessor(novo_professor)
        return jsonify({"mensagem": "Created", "professor": novo_professor}), 201

    except ProfessorExiste as e:
        return jsonify({"erro": str(e)}), 400
    #pode ser erro 409 - conflict - conflito entre dados ou dados iguais?
    
###############################################################################################################

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

@app.route("/professores/deletar/<int:id_professor>", methods=["DELETE"])
def delete_professor(id_professor):
    try:
        resultado = deletarProfessorPorId(id_professor)
        return jsonify(resultado), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404

@app.route('/professores/resetar', methods=['DELETE'])
def resetar_professor():
    resetar_professores()  # Função que reseta o dicionário de professores
    return jsonify({"mensagem": "Resetado"}), 200


@app.route("/alunos", methods=["GET"])
def listar_alunos_route():
    alunos = listar_alunos()
    return jsonify(alunos)

@app.route("/alunos/<int:id_aluno>", methods=["GET"])
def procurar_aluno_route(id_aluno):
    try:
        aluno = procurar_aluno_por_id(id_aluno)
        return jsonify(aluno)
    except AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404

@app.route("/alunos", methods=["POST"])
def adicionar_aluno():
    novo_aluno = request.json
    novo_aluno["Id"] = int(novo_aluno["Id"])
    novo_aluno["Turma_Id"] = int(novo_aluno["Turma_Id"])

    try:
        if aluno_ja_existe(novo_aluno["Id"]):
            raise AlunoExistente()
        criar_novo_aluno(novo_aluno)
        return jsonify({"mensagem": "Aluno criado com sucesso!", "aluno": novo_aluno}), 201
    except AlunoExistente as es:
        return jsonify({"Erro": str(es)}), 400


@app.route("/alunos/deletar/<int:id_aluno>", methods=["DELETE"])
def deletar_aluno_route(id_aluno):
    try:
        resultado = deletar_aluno_por_id(id_aluno)
        return jsonify(resultado), 200
    except AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404
    
@app.route('/alunos/resetar', methods=['DELETE'])
def resetar_alunoId():
    deletar_alunos()
    return jsonify({"mensagem": "Resetado"}), 200


@app.route("/alunos/<int:id_aluno>", methods=["PUT"])
def alterar_aluno_route(id_aluno):
    dados_aluno = request.json

    if not dados_aluno:
        return jsonify({
            "Erro": "Requisição inválida",
            "Descrição": "O corpo da requisição está vazio, preencha todos os campos"
        }), 400

    try:
        resultado, status_code = alterar_informacoes_aluno(
            id_aluno,
            dados_aluno.get("Nome"),
            dados_aluno.get("Idade"),
            dados_aluno.get("Turma_Id"),
            dados_aluno.get("Data_nascimento"),
            dados_aluno.get("Nota_Primeiro_Semestre"),
            dados_aluno.get("Nota_Segundo_semestre"),
            dados_aluno.get("Media_final")
        )
        return jsonify(resultado), status_code
    except AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404
    except Exception as e:
        return jsonify({"Erro": "Falha ao atualizar aluno", "Detalhes": str(e)}), 500


if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)