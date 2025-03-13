from flask import Flask, jsonify, request

app = Flask(__name__)

dadosTurma = {"Turma":[
    {"Id": 12, "Descrição": "Eng. Software","Ativa": True,"Professor Id": 14},
    {"Id": 14, "Descrição": "Análise e Desen. de Sistemas", "Ativa": False, "Professor Id": 13}
]}


# Aqui estão as rotas para as determinadas requisições Http

@app.route("/Turma", methods=["GET"])           #mesmo endpoint
def listarTurma():
    return jsonify (dadosTurma)

@app.route("/Turma", methods=["GET"])           #mesmo endpoint
def procurarTurma():


@app.route("/Turma.criar")