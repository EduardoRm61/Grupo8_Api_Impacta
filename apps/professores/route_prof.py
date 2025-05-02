
from flask import Blueprint, request, jsonify

from . import model_prof as modf
from flask_restx import  Namespace, fields, Resource

bp_professor = Blueprint("professores", __name__, url_prefix='/professores')

ns = Namespace("professores", description="Gerenciamento de dados dos professores da faculdade Impacta")

#____________________________________________DOC SWAGGER_______________________________________________________

@bp_professor.route('/')
def list_professores():
    return "Rota de professores funcionando!"

# model_prof = ns.model("Professor", {
#     "id" : fields.Integer(required=True, description="Identificação (id) do professor - pk"),
#     "nome" : fields.String(required=True, description="Nome do professor - obrigatório"),
#     "idade" : fields.Integer(required=False, description="Idade do professor "),
#     "materia" : fields.String(required=True, description="Matéria aplicada pelo professor- obrigatória"),
#     "obs" : fields.String(required=False, description="Observações, informações extras sobre o professor")
# })

# ____________________________________________ GET GERAL _______________________________________________________


@bp_professor.route('/professores', methods=['GET'])
def listar_professores():
    try:
        professores = modf.Professor.query.all()
        lista_professores = [professor.direcionar() for professor in professores]        
        return jsonify({"mensagem": "Ok", "professores": lista_professores}), 200
    except Exception as e:
        return jsonify({"mensagem": "error", "professor": f"Internal Server Error: {str(e)}"}), 500 


# ____________________________________________ GET ID ___________________________________________________________


@bp_professor.route("/professores/<int:id>", methods=["GET"])
def pesquisa_professor(id):
    try:
        professor = modf.procurarProfessorPorId(id)
        return jsonify({"mensagem": "Ok", "professor": professor}), 200
    except modf.ProfessorNaoIdentificado as e:
        return jsonify({"mensagem": "error", "professor": f"Not Found: {str(e)}"}), 404 
    
    
# ____________________________________________ POST ______________________________________________________________


@bp_professor.route('/professores', methods=['POST'])
def cadastrar_professores():
    novo_professor = request.json
    if not novo_professor or "nome" not in novo_professor or "materia" not in novo_professor:
        return jsonify({"mensagem": "error", "professor": f"Bad Request: {str(e)}"}), 400 
    try:
        if modf.ProfessorExistente(novo_professor["id"]):  
            raise modf.ProfessorExiste("Professor já existe")
        modf.criarNovoProfessor(novo_professor)
        return jsonify({"mensagem": "Created", "professor": novo_professor}), 201
    
    except modf.ProfessorExiste as e:
        return jsonify({"mensagem": "error", "professor": f"Bad Request: {str(e)}"}), 400
    
    
# ____________________________________________ PUT _______________________________________________________________


@bp_professor.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    atualizado = request.json
    try:
        professor = modf.procurarProfessorPorId(id) 
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
        return jsonify({"mensagem": "erro", "professor": f"Internal Server Error: {str(e)}"}) 


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
    modf.resetar_professores()  
    return jsonify({"mensagem": "Ok", "professor": "Resetado"}), 200



