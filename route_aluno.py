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
    
@bp_aluno.route("/alunos/<int:id_aluno>", methods=["PUT"])
def alterar_aluno_route(id_aluno):
    dados_aluno = request.json

    if not dados_aluno:
        return jsonify({
            "Erro": "Requisição inválida",
            "Descrição": "O corpo da requisição está vazio, preencha todos os campos"
        }), 400

    try:
        resultado, status_code = modAl.alterar_informacoes_aluno(
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
    except modAl.AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404
    except Exception as e:
        return jsonify({"Erro": "Falha ao atualizar aluno", "Detalhes": str(e)}), 500


