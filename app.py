from flask import Flask, jsonify, request

app = Flask(__name__)

dados = {
    "alunos": [
        {
            "Id": 20,
            "Nome": "Thaina",
            "Idade": 19,
            "Turma_Id": 12,
            "Data_nascimento": "10/08/2005",
            "Nota_Primeiro_Semestre": 8.0,
            "Nota_Segundo_semestre": 9.0,
            "Media_final": 8.5
        },

        {
            "Id": 25,
            "Nome": "Rafaela",
            "Idade": 25,
            "Turma_Id": 16,
            "Data_nascimento": "10/09/2000",
            "Nota_Primeiro_Semestre": 6.0,
            "Nota_Segundo_semestre": 9.0, 
            "Media_final": 7.5
        }
    ]
}


professores = {"professor": [
    {
    "id": 10,
    "nome": "Caio",
    "idade": 27,
    "materia": "Dev API E Micros",
    "obs": "Contato com aluno via Chat"},

    {"id": 11,
    "nome": "Odair",
    "idade": 30, 
    "materia": "DevOps",
    "obs": None}
]}


dadosTurma = {"Turma":[
    {"Id": 12, "Descrição": "Eng. Software","Ativa": True,"Professor Id": 10},
    {"Id": 14, "Descrição": "Análise e Desen. de Sistemas", "Ativa": False, "Professor Id": 11}     
]}

# dadosTurma = {"Turma":[     
# ]}

#Criando todas as classes de exceções:
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

class AlunoNaoIdentificado(Exception):
    def _init_(self, msg="Erro, Aluno não identificado ou inexistente!"):
        self.msg = msg
        super()._init_(self.msg)

class AlunoExistente(Exception):
    def _init_(self, msg="Erro, Aluno já existente!"):
        self.msg = msg
        super()._init_(self.msg)

class CadastroDeAlunoFalhado(Exception):
    def _init_(self, msg="Erro, Id do aluno ou Turma_Id incorretos!"):
        self.msg = msg
        super()._init_(self.msg)

class AtualizacaoAlunoFalhou(Exception):
    def _init_(self, msg="Erro, Não foi possível atualizar os dados do aluno! Reveja os campos e preencha corretamente"):
        self.msg = msg
        super()._init_(self.msg)

class ProfessorNaoIdentificado(Exception):
    def __init__(self, msg="Not Found - Professor inexistente"):
        self.msg = msg
        super().__init__(self.msg)

class ProfessorExiste(Exception):
    def __init__(self, msg="Professor já existente"):
        self.msg = msg
        super().__init__(self.msg)

class CadastroDeProfessorFalhado(Exception): # Correção: Nome da classe estava incorreto na chamada do except
    def __init__(self, msg="ID, nome e matéria são obrigatórios"):
        self.msg = msg
        super().__init__(self.msg)

#Criando funções para as requisições:

def ProcurarTurmaPorId(id_turma):
            for dict in dadosTurma["Turma"]:
                if dict['Id'] == id_turma:
                    return dict
            raise TurmaNaoIdentificada()

def CriarNovaTurma(nv_dict):
    dadosTurma["Turma"].append(nv_dict)
    return


def apaga_tudo():
    dados['alunos'] = []
    professores["Professor"] = []
    dadosTurma["Turma"] = []


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
    for professor in professores["professor"]:
        if professor["id"] == Id_professor:
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
                

# def gerar_novo_id():
#     '''Criação de id, obrigatório'''
#     if not professores["professor"]: # Correção: A verificação deve ser na lista de professores
#         return 1
#     return max(professor["id"] for professor in professores["professor"]) + 1 # Correção: Iterar sobre a lista correta


def procurarProfessorPorId(id_professor):   #def é minúscula
    for professor in professores["professor"]:
        if professor['id'] == id_professor:
            return professor
    raise ProfessorNaoIdentificado()

def criarNovoProfessor(nv_dict):
    professores["professor"].append(nv_dict)
    return

def deletarProfessorPorId(id_professor):
    for indice, professor in enumerate(professores["professor"]):
        if professor["id"] == id_professor:
            professores["professor"].pop(indice)
            return {"mensagem": "Professor deletado com sucesso"} # Correção: Retorno estava com ponto final extra
    raise ProfessorNaoIdentificado()

def procurar_aluno_por_id(id_aluno):
    for aluno in dados["alunos"]:
        if aluno["Id"] == id_aluno:
            return aluno
    raise AlunoNaoIdentificado()

def criar_novo_aluno(novo_aluno):
    dados["alunos"].append(novo_aluno)
    return {"Resposta":"Aluno criando com sucesso"}

def listar_alunos():
    return dados["alunos"]

def deletar_aluno_por_id(id_aluno):
    alunos = dados["alunos"]
    for indice, aluno in enumerate(alunos):
        if aluno["Id"] == id_aluno:
            alunos.pop(indice)
            return {"Mensagem": "Aluno deletado com sucesso."}
    raise AlunoNaoIdentificado()

def aluno_ja_existe(id_aluno):
    for aluno in dados["alunos"]:
        if aluno["Id"] == id_aluno:
            return True
    return False

def alterar_informacoes_aluno(id_aluno, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final): #NÃO SEI SE VAI PRECISAR
    try:
        for aluno in dados["alunos"]:
            if aluno["Id"] == id_aluno:
                aluno["Nome"] = nome
                aluno["Idade"] = idade
                aluno["Turma_Id"] = turma_id
                aluno["Data_nascimento"] = data_nascimento
                aluno["Nota_Primeiro_Semestre"] = nota_primeiro_semestre
                aluno["Nota_Segundo_semestre"] = nota_segundo_semestre
                aluno["Media_final"] = media_final
                return {"Detalhes": "Aluno atualizado com sucesso!"}, 200
        raise AlunoNaoIdentificado()
    except Exception as e:
        return {"Erro": "Não foi possível atualizar o aluno", "Descrição": str(e)}, 500
    
def resetar_professores():
    professores["Professor"] = []
    return
                
# Todas as rotas:

@app.route("/reseta", methods=["POST","DELETE"])
def reseta():
    apaga_tudo()
    return "resetado" 


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
    
    resultado, status_code = AlterarInformacoes(id_turma, dados["Descrição"], dados["Ativa"], dados["Professor Id"])
    return jsonify(resultado), status_code      


@app.route('/professores', methods=['GET'])
def listar_professores():
    try:
        return jsonify({"mensagem": "Ok", "professores": professores["professor"]}) 
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500 

@app.route("/professores/<int:id>", methods=["GET"])
def pesquisa_professor(id):
    try:
        professor = procurarProfessorPorId(id)
        return jsonify({"mensagem": "Ok", "professor": professor}), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404
    
###############################################################################################################
@app.route('/professores', methods=['POST'])
def cadastrar_professores():
    novo_professor = request.json
    if not novo_professor or "nome" not in novo_professor or "materia" not in novo_professor:
        return jsonify({"erro": "Nome e matéria são obrigatórios"}), 400
    try:
        if ProfessorExistente(novo_professor["id"]):  # Correção: Verifica se o professor já existe
            raise ProfessorExiste("Professor já existe")
        criarNovoProfessor(novo_professor)
        return jsonify({"mensagem": "Created", "professor": novo_professor}), 201
        #return jsonify({"mensagem": "Turma criada com sucesso!", "turma": nv_dict}), 201
    except ProfessorExiste as e:
        return jsonify({"erro": str(e)}), 400
###############################################################################################################

@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    atualizado = request.json
    try:
        professor = procurarProfessorPorId(id) # Correção: Usar a função de procurarProfessorPorId correta
        if "nome" in atualizado:
            professor['nome'] = atualizado['nome']
        if "idade" in atualizado:
            professor['idade'] = atualizado['idade']
        if "materia" in atualizado:
            professor['materia'] = atualizado['materia']
        if "obs" in atualizado:
            professor['obs'] = atualizado['obs']
        return jsonify({"mensagem": "Atualizado", "professor": professor}), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": f"Internal Server Error: {str(e)}"}) # Correção: Mensagem de erro mais clara

@app.route("/professores/deletar/<int:id_professor>", methods=["DELETE"])
def delete_professor(id_professor):
    try:
        resultado = deletarProfessorPorId(id_professor)
        return jsonify(resultado), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404

@app.route('/professores/resetar', methods=['DELETE'])
def resetar_professor():
    resetar_professores()
    return jsonify({"mensagem": "Resetado"}), 200


@app.route("/alunos", methods=["GET"])
def listar_alunos_route():
    alunos = listar_alunos()
    return jsonify(alunos)

@app.route("/alunos/<int:id_aluno>", methods=["GET"])
def procurar_aluno_route(id_aluno):
    try:
        aluno = procurar_aluno_por_id(id_aluno)
        return jsonify(aluno)
    except AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404

@app.route("/alunos", methods=["POST"])
def adicionar_aluno():
    novo_aluno = request.json
    novo_aluno["Id"] = int(novo_aluno["Id"])
    novo_aluno["Turma_Id"] = int(novo_aluno["Turma_Id"])

    try:
        if aluno_ja_existe(novo_aluno["Id"]):
            raise AlunoExistente()
        criar_novo_aluno(novo_aluno)
        return jsonify({"mensagem": "Aluno criado com sucesso!", "aluno": novo_aluno}), 201
    except AlunoExistente as es:
        return jsonify({"Erro": str(es)}), 400


@app.route("/alunos/resetar/<int:id_aluno>", methods=["DELETE"])
def deletar_aluno_route(id_aluno):
    try:
        resultado = deletar_aluno_por_id(id_aluno)
        return jsonify(resultado), 200
    except AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404

@app.route("/alunos/<int:id_aluno>", methods=["PUT"])
def alterar_aluno_route(id_aluno):
    dados_aluno = request.json

    if not dados_aluno:
        return jsonify({
            "Erro": "Requisição inválida",
            "Descrição": "O corpo da requisição está vazio, preencha todos os campos"
        }), 400

    try:
        resultado, status_code = alterar_informacoes_aluno(
            id_aluno,
            dados_aluno.get("Nome"),
            dados_aluno.get("Idade"),
            dados_aluno.get("Turma_Id"),
            dados_aluno.get("Data_nascimento"),
            dados_aluno.get("Nota_Primeiro_Semestre"),
            dados_aluno.get("Nota_Segundo_semestre"),
            dados_aluno.get("Media_final")
        )
        return jsonify(resultado), status_code
    except AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404
    except Exception as e:
        return jsonify({"Erro": "Falha ao atualizar aluno", "Detalhes": str(e)}), 500


if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)