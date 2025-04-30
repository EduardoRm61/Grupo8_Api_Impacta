
from flask import Blueprint, request, jsonify
import professores.model_prof as modf
from flask_restx import Resource, Namespace, fields

bp_professor = Blueprint("professores", __name__)

ns = Namespace("professores", description="Gerenciamênto de dados dos professor da faculdade Impacta")

#____________________________________________DOC SWAGGER_______________________________________________________

model_prof = ns.model( "Professor", {
    "id" : fields.Integer(required=True, description="Identificação (id) do professor - pk"),
    "nome" : fields.String(required=True, description="Nome do professor - obrigatório"),
    "idade" : fields.Integer(required=True, description="Idade do professor "),
    "materia" : fields.String(required=True, description="Matéria aplicada pelo professor- obrigatória"),
    "obs" : fields.String(required=True, description="Observações, informações extras sobre o professor")
})

# ____________________________________________ GET GERAL _______________________________________________________


@bp_professor.route('/professores', methods=['GET'])
def listar_professores():
    try:
        return jsonify({"mensagem": "Ok", "professores": modf.professores["professor"]}) 
    except Exception as e:
        return jsonify({"mensagem": "error", "professor": f"Internal Server Error: {str(e)}"}), 500 
    

# ____________________________________________ GET ID ___________________________________________________________


@bp_professor.route("/professores/<int:id>", methods=["GET"])
def pesquisa_professor(id):
    try:
        professor = modf.procurarProfessorPorId(id)
        return jsonify({"mensagem": "Ok", "professor": professor}), 200
    except modf.ProfessorNaoIdentificado as e:
        return jsonify({"mensagem": "error", "professor": f"Not Found: {str(e)}"}), 404 # trocar por 400 Bad Request
    
    
# ____________________________________________ POST ______________________________________________________________


@bp_professor.route('/professores', methods=['POST'])
def cadastrar_professores():
    novo_professor = request.json
    if not novo_professor or "nome" not in novo_professor or "materia" not in novo_professor:
        return jsonify({"mensagem": "error", "professor": f"Bad Request: {str(e)}"}), 400    #talvez seja melhor 
    try:
        if modf.ProfessorExistente(novo_professor["id"]):  # Correção: Verifica se o professor já existe
            raise modf.ProfessorExiste("Professor já existe")
        modf.criarNovoProfessor(novo_professor)
        return jsonify({"mensagem": "Created", "professor": novo_professor}), 201
        #return jsonify({"mensagem": "Turma criada com sucesso!", "turma": nv_dict}), 201
    except modf.ProfessorExiste as e:
        return jsonify({"mensagem": "error", "professor": f"Bad Request: {str(e)}"}), 400
    
    
# ____________________________________________ PUT _______________________________________________________________


@bp_professor.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    atualizado = request.json
    try:
        professor = modf.procurarProfessorPorId(id) # Correção: Usar a função de procurarProfessorPorId correta
        if "nome" in atualizado:
            professor['nome'] = atualizado['nome']
        if "idade" in atualizado:
            professor['idade'] = atualizado['idade']
        if "materia" in atualizado:
            professor['materia'] = atualizado['materia']
        if "obs" in atualizado:
            professor['obs'] = atualizado['obs']
        return jsonify({"mensagem": "Atualizado", "professor": professor}), 200
    except modf.ProfessorNaoIdentificado as e:
        return jsonify({"mensagem": "error", "professor": f"Not Found: {str(e)}"}), 404
    except Exception as e:
        return jsonify({"mensagem": "erro", "professor": f"Internal Server Error: {str(e)}"}) # Correção: Mensagem de erro mais clara


# ____________________________________________ DELETE ID __________________________________________________________


@bp_professor.route("/professores/deletar/<int:id_professor>", methods=["DELETE"])
def delete_professor(id_professor):
    try:
        resultado = modf.deletarProfessorPorId(id_professor)
        return jsonify({"mensagem": "Ok", "professor": {resultado}}), 200
    except modf.ProfessorNaoIdentificado as e:
        return jsonify({"mensagem": "error", "professor": f"Not Found: {str(e)}"}), 404


# ____________________________________________ DELETE ______________________________________________________________


@bp_professor.route('/professores/resetar', methods=['DELETE'])
def resetar_professor():
    modf.resetar_professores()  # Função que reseta o dicionário de professores
    return jsonify({"mensagem": "Ok", "professor": "Resetado"}), 200



# ++++++++++++++++++++++++++++++++++++++ ok ++++++++++++++++++++++++++++++++++++++++++++++++++++++++