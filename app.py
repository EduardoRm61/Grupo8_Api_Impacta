from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados iniciais
dados = {
    "alunos": [
        {"nome": "lucas", "id": 15},
        {"nome": "cicero", "id": 29},
    ],
    "professores": []
}


# Classes de exceções para possíveis erros no código

class AlunoNaoIdentificado(Exception):
    def __init__(self, msg="Erro, Aluno não identificado ou inexistente!"):
        self.msg = msg
        super().__init__(self.msg)

class AlunoExistente(Exception):
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

def DeletarTodosAlunos():
    dados["alunos"] = []
    return

# Aqui estão todas as rotas:

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    alunos = ListarAlunos()
    return jsonify(alunos), 200