from flask import Blueprint, request, jsonify
import model_aluno as modal

bp_aluno = Blueprint("alunos", __name__)

@bp_aluno.route("/alunos", methods=["GET"])
def listar_alunos_route():
    alunos = modal.listar_alunos()
    return jsonify(alunos)

@bp_aluno.route("/alunos/<int:id_aluno>", methods=["GET"])
def procurar_aluno_route(id_aluno):
    try:
        aluno = modal.modprocurar_aluno_por_id(id_aluno)
        return jsonify(aluno)
    except modal.AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404