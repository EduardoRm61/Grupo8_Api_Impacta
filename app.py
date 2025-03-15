from flask import Flask, jsonify, request

app = Flask(__name__)

dadosProfessor = {"Professor":[
    {"Id": 12, "Nome": "Caio"},
    {"Id": 15, "Nome": "Furlan"}
]}

dadosTurma = {"Turma":[
    {"Id": 12, "Descrição": "Eng. Software","Ativa": True,"Professor Id": 12},
    {"Id": 14, "Descrição": "Análise e Desen. de Sistemas", "Ativa": False, "Professor Id": 15}     
]}

@app.route("/Turma",methods=["GET"])           #Conferindo lista de turmas
def listarTurma():
    return jsonify(dadosTurma)

if __name__ == "__main__":
    app.run(debug=True)