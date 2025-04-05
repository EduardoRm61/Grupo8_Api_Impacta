# rotas apenas
# lembrar que agora não tem app e sim blueprint

from flask import Blueprint, request, jsonify
from model_prof import professores, ProfessorNaoIdentificado, ProfessorExiste, CadastroDeProfessorFalhado, apaga_tudo, ProfessorExistente, procurarProfessorPorId, criarNovoProfessor, deletarProfessorPorId, resetar_professores
# se não importar separadamnete dá reportUndefineVariable - variável não definida | melhor não por import model_prof


bluep_professor = Blueprint("professores", __name__)

# blueprint = estrutura flask que organiza rotas, templates e conf em partes separadas
# a variável bluep_professor receberá o blueprint do flask, terá nome de professor/ usado no url e totas
# name indicará o módulo atual (neste caso arquivo  route_prof.py), assim o flask poderá localizar templates, arquivos estáticos e blueprint - seu valor é automático


# ____________________________________________ GET GERAL _______________________________________________________


@bluep_professor.route('/professores', methods=['GET'])
def listar_professores():
    try:
        return jsonify({"mensagem": "Ok", "professores": professores["professor"]}) 
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500 
    

# ____________________________________________ GET ID ___________________________________________________________


@bluep_professor.route("/professores/<int:id>", methods=["GET"])
def pesquisa_professor(id):
    try:
        professor = procurarProfessorPorId(id)
        return jsonify({"mensagem": "Ok", "professor": professor}), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404
    
    
# ____________________________________________ POST ______________________________________________________________


@bluep_professor.route('/professores', methods=['POST'])
def cadastrar_professores():
    novo_professor = request.json
    if not novo_professor or "nome" not in novo_professor or "materia" not in novo_professor:
        return jsonify({"erro": "Nome e matéria são obrigatórios"}), 400
    try:
        if ProfessorExistente(novo_professor["id"]):  # Correção: Verifica se o professor já existe
            raise ProfessorExiste("Professor já existe")
        criarNovoProfessor(novo_professor)
        return jsonify({"mensagem": "Created", "professor": novo_professor}), 201
        #return jsonify({"mensagem": "Turma criada com sucesso!", "turma": nv_dict}), 201
    except ProfessorExiste as e:
        return jsonify({"erro": str(e)}), 400
    
    
# ____________________________________________ PUT _______________________________________________________________


@bluep_professor.route('/professores/<int:id>', methods=['PUT'])
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


# ____________________________________________ DELETE ID __________________________________________________________


@bluep_professor.route("/professores/deletar/<int:id_professor>", methods=["DELETE"])
def delete_professor(id_professor):
    try:
        resultado = deletarProfessorPorId(id_professor)
        return jsonify(resultado), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404


# ____________________________________________ DELETE ______________________________________________________________


@bluep_professor.route('/professores/resetar', methods=['DELETE'])
def resetar_professor():
    resetar_professores()  # Função que reseta o dicionário de professores
    return jsonify({"mensagem": "Resetado"}), 200