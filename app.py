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

#Criando classes para minhas excessões:
class TurmaNaoIdentificada(Exception):
    def __init__(self, msg="Erro, Turma não identificada ou inexistente!"):
        self.msg = msg
        super().__init__(self.msg)
    
class ProfessorNaoIdentificado(Exception):
    def __init__(self,msg="Erro, Professor não indentificado ou inexistente!"):
        self.msg = msg
        super().__init__(self.msg)

class TurmaExistente(Exception):
    def __init__(self, msg="Erro, Turma já existente!"):
        self.msg = msg
        super().__init__(self.msg)

#Criando fuções para as requisições:

def ProcurarTurmaPorId(id_turma):
            for dict in dadosTurma["Turma"]:
                if dict['Id'] == id_turma:
                    return dict
            raise TurmaNaoIdentificada()

def CriarNovaTurma(nv_dict):
    dadosTurma["Turma"].append(nv_dict)
    return

def ListarTurma():
    return dadosTurma["Turma"]

def DeletarTurma():
    dadosTurma["Turma"] = []

def DeletarTurmaPorId(id_turma):
    turmas = dadosTurma["Turma"]
    for turma in turmas:
          if turma["Id"] == id_turma:
               turmas.remove(turma)
               return 
    raise TurmaNaoIdentificada()

#Criando as rotas:

@app.route("/Turma",methods=["GET"])           #Conferindo lista de turmas
def listar_turma():
    Turmas = ListarTurma()
    return jsonify(Turmas)

@app.route("/Turma/<int:id_turma>", methods=["GET"])           #Procurar turma específica
def procurarTurma(id_turma):
     try:
        dados = ProcurarTurmaPorId(id_turma)
        return jsonify(dados)
     except TurmaNaoIdentificada as trm:
          return jsonify({"Erro:": str(trm)}), 402

@app.route("/Turma", methods=["POST"])
def AddTurma():
     nv_dict = request.json
     nv_dict['Id'] = int(nv_dict['Id'])
     CriarNovaTurma(nv_dict)
     ListarTurma()
     return 

@app.route("/Turma/Resetar", methods=["DELETE"])
def ResetarTodaTurma():
     DeletarTurma()
     return "Resetado"

@app.route("/Turma/Resetar/<int:id_turma>")
def ResetarTurmaId(id_turma):
     try:
          DeletarTurmaPorId(id_turma)
          return jsonify(dadosTurma["Turma"]), 200
     except TurmaNaoIdentificada as trm:
          return jsonify({"Erro:": str(trm)}), 404
     

if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)