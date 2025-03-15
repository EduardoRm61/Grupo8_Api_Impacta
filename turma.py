from flask import Flask, jsonify, request

app = Flask(__name__)

app = {"Professor":[
    {"Id": 12, "Nome": "Caio"},
    {"Id": 15, "Nome": "Furlan"}
]}

dadosTurma = {"Turma":[
    {"Id": 12, "Descrição": "Eng. Software","Ativa": True,"Professor Id": 12},
    {"Id": 14, "Descrição": "Análise e Desen. de Sistemas", "Ativa": False, "Professor Id": 15}     
]}

dadosTurma.remove
 # Criando Classes de excessões 

class ProfessorNaoIdentificado(Exception):
    def __init__(self,msg="Erro, Professor não indentificado ou inexistente!"):
        self.msg = msg
        super().__init__(self.msg)

class TurmaNaoIdentificada(Exception):
    def __init__(self, msg="Erro, Turma não identificada ou inexistente!"):
        self.msg = msg
        super().__init__(self.msg)

class TurmaExistente(Exception):
    def __init__(self, msg="Erro, Turma já existente!"):
        self.msg = msg
        super().__init__(self.msg)


# Aqui estão as rotas para as determinadas requisições Http

@app.route("/Turma", methods=["GET"])           #Conferindo lista de turmas
def listarTurma():
    return jsonify(dadosTurma)

# @app.route("/Turma:<Id:int>")

# @app.route("/Turma/<int:id_tuma>", methods=["GET"])           #Procurar turma específica
# def procurarTurma(id_turma):
#     try:
#         for id in dadosTurma:
#             if id 
        

# @app.route("/Turma.criar", methods=["POST"])
# def criarTurma():
#     novo_dict = request.jsonify



# def listProfessor(id_Professor):
#     id_Profs = [professor]              # Aqui eu puxo de dados, onde estará professor.
#     for Ids in id_Profs:
#         if Ids["Id"] == id_Professor:
#             return Ids
#         raise ProfessorNaoIdentificado()
    
        
# def addProfessor(novo_dict):
#     return dadosTurma["Turma"].append(novo_dict)

if __name__ == "__name__":
    app.run(debug=True)