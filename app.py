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

class AlunoNaoIdentificado(Exception):
    def __init__(self, msg="Erro, Aluno não identificado ou inexistente!"):
        self.msg = msg
        super().__init__(self.msg)

class AlunoExistente(Exception):
    def __init__(self, msg="Erro, Aluno já existente!"):
        self.msg = msg
        super().__init__(self.msg)

