from flask import Flask, jsonify, request
import requests
#import unittest

app = Flask(__name__)


dados = {
    "alunos": [
    {"Id": 20, "Nome": "Thaina"},
    {"Id": 22, "Nome": "Eduardo"}
    ],
    
}


# Classes de exceções para possíveis erros no código

class AlunoNaoIdentificado(Exception):
    def __init__(self, msg="Erro, Aluno não identificado ou inexistente!"):
        self.msg = msg
        super().__init__(self.msg)

class AlunoJaExistente(Exception):
    def __init__(self, msg="Erro, Aluno já existente!"):
        self.msg = msg
        super().__init__(self.msg)

class CadastroDeAlunoFalhado(Exception):
    def __init__(self, msg="Erro, Falha ao cadastrar aluno. Verifique os dados!"):
        self.msg = msg
        super().__init__(self.msg)

class AtualizacaoAlunoFalhou(Exception):
    def __init__(self, msg="Erro, Não foi possível atualizar os dados do aluno. Verifique os campos!"):
        self.msg = msg
        super().__init__(self.msg)

# Aqui estão as funções auxiliares para as rotas:

def ListarAlunos():
    return dados["alunos"]

def CriarNovoAluno(nv_dict):
    dados["alunos"].append(nv_dict)
    return

def DeletarTodosAlunos():
    dados["alunos"] = []
    return

def DeletarAlunoPorId(id_aluno):
    alunos = dados["alunos"]
    for indice, alunos in enumerate(alunos):
        if alunos["Id"] == id_aluno:
            alunos.pop(indice)
            return {"Mensagem": "Aluno foi deletado."}
        raise AlunoNaoIdentificado()

def ProcurarAlunoPorId(id_aluno):
    for aluno in dados["alunos"]:
        if aluno['Id'] == id_aluno:
            return aluno
        raise AlunoNaoIdentificado()
    
def AlunoJaExiste(id_aluno):
    for aluno in dados["aluno"]:
        if aluno["Id"] == id_aluno:
            return True
        return False
    
def AlterarInformacoes(Id_aluno, Nome):
    novos_dados = dados["alunos"]
    try:
        for aluno in novos_dados:
            if aluno["Id"] == Id_aluno:
                if AlunoJaExistente(Id_aluno):
                    return({
                        "ERRO": "Aluno já cadastrado com esse Id"
                    }), 400
            aluno["Nome"] = Nome
            return {"Aluno atualizado com sucesso!"}, 200
        return({
            "ERRO": "Este Id já está associado a um aluno."
    }), 400 #400 ou 404?
    except Exception as e:
        return({
            "ERRO": "Não é possível fazer essa requisição",
            "Descrição": str(e)
        })
    

# Aqui estão todas as rotas:

@app.route("/") 
def hello():
        print("rodei mesmo") 
        return "Hello World!"


@app.route("/alunos", methods=["GET"])
def listar_alunos():
    alunos = ListarAlunos()
    return jsonify(alunos), 200

@app.route("/Auno/<int:id_aluno>", methods=["GET"])
def encontrar_aluno (id_aluno):
    try:
        aluno = ProcurarAlunoPorId(id_aluno)
        return jsonify(aluno)
    except AlunoNaoIdentificado as ani:
        return jsonify({"ERRO": str(ani)}), 404
    
@app.route("/aluno", methods=["POST"])
def criar_aluno():
    try:
        # Obtém os dados do corpo da requisição
        nv_dict = request.json

        # Verifica se o ID foi fornecido
        if "Id" not in nv_dict or "Nome" not in nv_dict:
            return jsonify({
                "ERRO": "Requisição inválida.",
                "Mensagem": "Os campos 'Id' e 'Nome' são obrigatórios."
            }), 400

        # Converte o ID para inteiro
        nv_dict["Id"] = int(nv_dict["Id"])

        # Verifica se o aluno já existe
        if AlunoJaExiste(nv_dict["Id"]):
            return jsonify({
                "ERRO": "Requisição inválida.",
                "Mensagem": "Este Id já está associado a um aluno."
            }), 400

        # Adiciona o novo aluno
        CriarNovoAluno(nv_dict)

        # Retorna a lista atualizada de alunos
        return jsonify({
            "Mensagem": "Aluno criado com sucesso!",
            "alunos": ListarAlunos()
        }), 201

    except Exception as e:
        return jsonify({
            "ERRO": "Falha ao cadastrar novo aluno.",
            "Detalhes": str(e)
        }), 500

@app.route("/alunos/<int:idAluno>", methods=['PUT'])
def atualizar_alunos(idAluno):
    try:
        novos_dados = request.json
        nome = novos_dados.get("Nome")
        resultado = AlterarInformacoes(idAluno, nome=nome)
        return jsonify(resultado), 200
    except AlunoNaoIdentificado as ani:
        return jsonify({"erro": str(ani)}), 404
    
@app.route("/aluno/resetar/<int:id_aluno>", methods=["DELETE"])
def resetar_aluno_Id(id_aluno):
    try:
        resetar_aluno_Id(id_aluno)
        return jsonify(dados["alunos"]), 200
    except AlunoNaoIdentificado as ani:
          return jsonify({"Erro:": str(ani)}), 404


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug=True)


#########TESTES#################


