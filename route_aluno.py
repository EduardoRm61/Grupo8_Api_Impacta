from flask import Blueprint, request, jsonify
import model_aluno as modal

bp_aluno = Blueprint("alunos", __name__)

@bp_aluno.route("/alunos", methods=["GET"])
def listar_alunos_route():
    alunos = modal.listar_alunos()
    return jsonify(alunos)
