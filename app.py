from flask import Flask, jsonify, request

app = Flask(__name__)

dadosProfessor = {"Professor":[
    {"Id": 12, "Nome": "Caio"},
    {"Id": 15, "Nome": "Furlan"}
]}

# dadosTurma = {"Turma":[
#     {"Id": 12, "Descrição": "Eng. Software","Ativa": True,"Professor Id": 12},
#     {"Id": 14, "Descrição": "Análise e Desen. de Sistemas", "Ativa": False, "Professor Id": 15}     
# ]}

dadosTurma = {"Turma":[     
]}

#Criando classes para minhas excessões:
class TurmaNaoIdentificada(Exception):
    def __init__(self, msg="Erro, Turma não identificada ou inexistente!"):
        self.msg = msg
        super().__init__(self.msg)

class ProfessorNaoIdentificado(Exception):
    def __init__(self,msg="Erro, Professor não indentificado ou existente!"):
        self.msg = msg
        super().__init__(self.msg)

class TurmaExistente(Exception):
    def __init__(self, msg="Erro, Turma já existente!"):
        self.msg = msg
        super().__init__(self.msg)

class CadastroDeTurmaFalhado(Exception):
     def __init__(self, msg="Erro, Id turma e Id Professor incorretos!"):
          self.msg = msg
          super().__init__(self.msg)

class AtualizacaoTurma(Exception):
    def __init__(self, msg="Erro, Não foi possível atualizar os dados da turma! Reveja os campos e preencha corretamente"):
        self.msg = msg
        super().__init__(self.msg)

class ValorBool(Exception):
    def __init__(self, msg="Erro, valor Booleano incorreto, deigite True ou False"):
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

##############################
# Função para todo o servidor:
# def apaga_tudo():
#     dados['alunos'] = []
##############################
def ListarTurma():
    return dadosTurma["Turma"]

def DeletarTurma():
    dadosTurma["Turma"] = []


def DeletarTurmaPorId(id_turma):
    turmas = dadosTurma["Turma"]

    for indice, turma in enumerate(turmas):
        if turma["Id"] == id_turma:
            turmas.pop(indice)
            return {"Mensagem": "Turma deletada com sucesso."}
    raise TurmaNaoIdentificada()


def ProfessorExistente(Id_professor):
    for professor in dadosProfessor["Professor"]:
        if professor["Id"] == Id_professor:
            return True  
    return False

def TurmaJaExiste(Id_turma):
    for turma in dadosTurma["Turma"]:
        if turma["Id"] == Id_turma:
            return True
    return False

def ValoorBuleano(valorbool):
    if valorbool is True or valorbool is False:
        return True
    return False

def AlterarInformacoes(Id_turma, Descricao, Ativa, Id_Pro):
    nv_dados = dadosTurma["Turma"]
    try:
        for turma in nv_dados:
            if turma["Id"] == Id_turma:
                if not ProfessorExistente(Id_Pro):
                    return ({
                        "Erro": "Requisição inválida",
                        "Descrição": "Id do Professor inexistente"
                    }), 400
                if not ValoorBuleano(Ativa):
                    return ({
                        "Erro": "Requisição inválida",
                        "Descricao": "Valor de Ativa incorreto. Digite True ou False"
                    }), 400
                turma["Descrição"] = Descricao
                turma["Professor Id"] = Id_Pro
                turma["Ativa"] = Ativa
                return {"Detalhes":"Turma atualizada com seucesso!"}, 200
        return ({
            "Erro": "Requisição inválida",
            "Descrição": "Id da turma inexistente"
        }), 400
    except Exception as e:
        return({
            "Erro": "Não foi possível fazer a requisição",
            "Descrição": str(e)
        }), 500
                
 
#Criando as rotas, lembrando que a função jsonify só pode ser usada nas rotas:

#################################################
#Rota para apagar todo o servidor
# @app.route("/reseta", methods=["POST","DELETE"])
# def reseta():
#     apaga_tudo()
#     return "resetado" 
##################################################

@app.route("/Turma",methods=["GET"])                              
def listar_turma():
    Turmas = ListarTurma()
    return jsonify(Turmas)

@app.route("/Turma/<int:id_turma>", methods=["GET"])            
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
    nv_dict['Professor Id'] = int(nv_dict['Professor Id'])

    try:
         
        if not ProfessorExistente(nv_dict["Professor Id"]):
            return jsonify({
                "Erro": "Requisição inválida",
                "Detalhes": "Id do Professor inexistente"
            }), 400

        if TurmaJaExiste(nv_dict["Id"]):
            return jsonify({
                "Erro": "Requisição inválida",
                "Detalhes": "Id da Turma já existente"
            }), 400
        CriarNovaTurma(nv_dict)
        return jsonify({"mensagem": "Turma criada com sucesso!", "turma": nv_dict}), 201
    
    except CadastroDeTurmaFalhado as cdtf:
         return jsonify({
            "Erro": "Falha ao cadastrar turma",
            "detalhes": str(cdtf)
         }), 400    

@app.route("/Turma/Resetar", methods=["DELETE"])
def ResetarTodaTurma():
     DeletarTurma()
     return jsonify({"mensagem": "Resetado"}), 200

@app.route("/Turma/Resetar/<int:id_turma>", methods=["DELETE"])
def ResetarTurmaId(id_turma):
     try:
          DeletarTurmaPorId(id_turma)
          return jsonify(dadosTurma["Turma"]), 200
     except TurmaNaoIdentificada as trm:
          return jsonify({"Erro:": str(trm)}), 404
     
@app.route("/Turma/Alterar/<int:id_turma>", methods=["PUT"])
def AlterarInfo(id_turma):
    dados = request.json
    
    #dict['id'] = int (dict['id'])

    if not dados:
        return jsonify({
            "Erro": "Requisição inválida",
            "Descrição": "O corpo da requisição está vazio, preencha todos os campos"
        }), 400
    
    if "Descrição" not in dados:
        return jsonify({
            "Erro": "Não foi possível fazer a requisição",
            "Dscrição": "O campo Descrição da turma é obrigatório ser preenchido"
        }), 400
    
    if "Ativa" not in dados:
        return jsonify({
            "Erro": "Não foi possível fazer a requisição",
            "Descrição": "O campo Ativa é obrigatório ser preenchido "
        }), 400
    
    if "Professor Id" not in dados:
        return jsonify({
            "Erro": "Não foi possível fazer a requisição",
            "Descrição": "O campo Professor Id é obrigatório se preechido"
        }), 400
    


    # Chama a função AlterarInformacoes e retorna a resposta
    resultado, status_code = AlterarInformacoes(id_turma, dados["Descrição"], dados["Ativa"], dados["Professor Id"])
    return jsonify(resultado), status_code      #Aqui eu quase chorei

  
     



# app = Flask(__name__)
# @app.route('/professores', methods=['GET'])
# def listar_professores():
#     return jsonify(professores), 200

# @app.route('/professores', methods=['POST'])
# def cadastrar_professores():
#     dados = request.json
#     novo_professor = {
#         'id': len(professores) +1,
#         'nome':dados.get('nome')

        
#     }
#     professores.append(novo_professor)
#     return jsonify(novo_professor), 201
    
#     @app.route('/profesores/<int:id>', methods=['PUT'])
#     def atualizar_professor(id):
#         dados = request.json
#         for professor in professores:
#         f professor['id'] == id:
#             professor['nome'] = dados.get('nome', professor['nome'])
#             professor['disciplina'] = dados.get('disciplina', professor['disciplina'])
#             return jsonify(professor), 200
#     return jsonify({'erro': 'Professor não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)



