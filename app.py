from flask import Flask, jsonify, request


app = Flask(__name__)


dados = {
    "alunos": [
        {
            "Id": 20,
            "Nome": "Thaina",
            "Idade": 28,
            "Turma_Id": 12,
            "Data_nascimento": "10/08/2005",
            "Nota_Primeiro_Semestre": 8.0,
            "Nota_Segundo_semestre": 9.0,
            "Media_final": 8.5
        }
    ]
}


# Criando classes para minhas exceções:
class AlunoNaoIdentificado(Exception):
    def _init_(self, msg="Erro, Aluno não identificado ou inexistente!"):
        self.msg = msg
        super()._init_(self.msg)

class AlunoExistente(Exception):
    def _init_(self, msg="Erro, Aluno já existente!"):
        self.msg = msg
        super()._init_(self.msg)

class CadastroDeAlunoFalhado(Exception):
    def _init_(self, msg="Erro, Id do aluno ou Turma_Id incorretos!"):
        self.msg = msg
        super()._init_(self.msg)

class AtualizacaoAlunoFalhou(Exception):
    def _init_(self, msg="Erro, Não foi possível atualizar os dados do aluno! Reveja os campos e preencha corretamente"):
        self.msg = msg
        super()._init_(self.msg)




# Aqui estão as funções auxiliares para as rotas:
def procurar_aluno_por_id(id_aluno):
    for aluno in dados["alunos"]:
        if aluno["Id"] == id_aluno:
            return aluno
    raise AlunoNaoIdentificado()

def criar_novo_aluno(novo_aluno):
    dados["alunos"].append(novo_aluno)
    return

def listar_alunos():
    return dados["alunos"]

def deletar_aluno_por_id(id_aluno):
    alunos = dados["alunos"]
    for indice, aluno in enumerate(alunos):
        if aluno["Id"] == id_aluno:
            alunos.pop(indice)
            return {"Mensagem": "Aluno deletado com sucesso."}
    raise AlunoNaoIdentificado()

def aluno_ja_existe(id_aluno):
    for aluno in dados["alunos"]:
        if aluno["Id"] == id_aluno:
            return True
    return False

def alterar_informacoes_aluno(id_aluno, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final): #NÃO SEI SE VAI PRECISAR
    try:
        for aluno in dados["alunos"]:
            if aluno["Id"] == id_aluno:
                aluno["Nome"] = nome
                aluno["Idade"] = idade
                aluno["Turma_Id"] = turma_id
                aluno["Data_nascimento"] = data_nascimento
                aluno["Nota_Primeiro_Semestre"] = nota_primeiro_semestre
                aluno["Nota_Segundo_semestre"] = nota_segundo_semestre
                aluno["Media_final"] = media_final
                return {"Detalhes": "Aluno atualizado com sucesso!"}, 200
        raise AlunoNaoIdentificado()
    except Exception as e:
        return {"Erro": "Não foi possível atualizar o aluno", "Descrição": str(e)}, 500


# Aqui estão todas as rotas:
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
    except AlunoExistente as e:
        return jsonify({"Erro": str(e)}), 400
    except Exception as e:
        return jsonify({"Erro": "Falha ao cadastrar aluno", "Detalhes": str(e)}), 400

@app.route("/alunos/<int:id_aluno>", methods=["DELETE"])
def deletar_aluno_route(id_aluno):
    try:
        resultado = deletar_aluno_por_id(id_aluno)
        return jsonify(resultado), 200
    except AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404

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
            dados_aluno.get("media_final")
        )
        return jsonify(resultado), status_code
    except AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404
    except Exception as e:
        return jsonify({"Erro": "Falha ao atualizar aluno", "Detalhes": str(e)}), 500



if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug=True)





