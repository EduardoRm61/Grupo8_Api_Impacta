from flask import Blueprint, request, jsonify
import model_aluno as modAl

bp_aluno = Blueprint("alunos", __name__)

@bp_aluno.route("/alunos", methods=["GET"])
def listar_alunos_route():
    alunos = modAl.listar_alunos()
    return jsonify(alunos)

@bp_aluno.route("/alunos/<int:id_aluno>", methods=["GET"])
def procurar_aluno_route(id_aluno):
    try:
        aluno = modAl.modprocurar_aluno_por_id(id_aluno)
        return jsonify(aluno)
    except modAl.AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404
    

@bp_aluno.route("/alunos", methods=["POST"])
def adicionar_aluno():
    novo_aluno = request.json
    novo_aluno["Id"] = int(novo_aluno["Id"])
    novo_aluno["Turma_Id"] = int(novo_aluno["Turma_Id"])
    try:
        if modAl.aluno_ja_existe(novo_aluno["Id"]):
            raise modAl.AlunoExistente()
        modAl.criar_novo_aluno(novo_aluno)
        return jsonify({"mensagem": "Aluno criado com sucesso!", "aluno": novo_aluno}), 201
    except modAl.AlunoExistente as es:
        return jsonify({"Erro": str(es)}), 400

