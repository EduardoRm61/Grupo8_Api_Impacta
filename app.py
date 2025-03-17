from flask import Flask, jsonfy

app = Flask(__name__)

dadosAluno = {"Aluno":[
    {"Id": 20, "Nome": "Thaina", "Idade": 28, "Turma_Id": 12, "Data de nascimento": 20/5/1996, "Nota do primeiro semestre": 8, "Nota do segundo semestre": 8, "Media Final": 8},
    {"Id": 20, "Nome": "Eduardo", "Idade": 20, "Turma_Id": 14, "Data de nascimento": 1/1/2005, "Nota do primeiro semestre": 10, "Nota do segundo semestre": 10, "Media Final": 10}
]}

dadosTurma = {"Turma":[
    {"Id": 1, "Descrição": "Banco de dados", "professor_id": 500, "Ativa": False},
    {"Id": 1, "Descrição": "Desenvolvimento Mobile", "professor_id": 555, "Ativa": True}
]}

