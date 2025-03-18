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