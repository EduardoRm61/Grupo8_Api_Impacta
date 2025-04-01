from flask import Flask, jsonify, request
import model_turma as modTur
import model_professor as modProf
import model_aluno as modAlu

app = Flask(__name__)

# dados = {
#     "alunos": [
#         {
#             "Id": 20,
#             "Nome": "Thaina",
#             "Idade": 19,
#             "Turma_Id": 12,
#             "Data_nascimento": "10/08/2005",
#             "Nota_Primeiro_Semestre": 8.0,
#             "Nota_Segundo_semestre": 9.0,
#             "Media_final": 8.5
#         },

#         {
#             "Id": 25,
#             "Nome": "Rafaela",
#             "Idade": 25,
#             "Turma_Id": 16,
#             "Data_nascimento": "10/09/2000",
#             "Nota_Primeiro_Semestre": 6.0,
#             "Nota_Segundo_semestre": 9.0, 
#             "Media_final": 7.5
#         }
#     ]
# }


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


def apaga_tudo():
    modAlu.dados['alunos'] = []
    modProf.professores["Professor"] = []
    modTur.dadosTurma["Turma"] = []


def procurarProfessorPorId(id_professor):   #def é minúscula
    for professor in modProf.professores["professor"]:
        if professor['id'] == id_professor:
            return professor
    raise modProf.ProfessorNaoIdentificado()

def criarNovoProfessor(nv_dict):
    modProf.professores["professor"].append(nv_dict)
    return

def deletarProfessorPorId(id_professor):
    for indice, professor in enumerate(modProf.professores["professor"]):
        if professor["id"] == id_professor:
            modProf.professores["professor"].pop(indice)
            return {"mensagem": "Professor deletado com sucesso"} # Correção: Retorno estava com ponto final extra
    raise modProf.ProfessorNaoIdentificado()

# ..........................

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


# -------------------------- RESET PROF ------------------------------------#
    
def resetar_professores():
    modProf.professores["professor"] = []
    return
#............................................................................
def deletar_alunos():
    dados["alunos"] = []
    return
                
# Todas as rotas:
#TODAS ROTAS PROFESSORES DEVEM FICAR APENAS NA APP.PY E RESTO MODEL

@app.route("/reseta", methods=["POST","DELETE"])
def reseta():
    apaga_tudo()
    return "resetado" 


@app.route("/Turma",methods=["GET"])                              
def listar_turma():
    Turmas = modTur.ListarTurma()
    return jsonify(Turmas)

@app.route("/Turma/<int:id_turma>", methods=["GET"])            
def procurarTurma(id_turma):
     try:
        dados = modTur.ProcurarTurmaPorId(id_turma)
        return jsonify(dados)
     except modTur.TurmaNaoIdentificada as trm:
          return jsonify({"Erro:": str(trm)}), 402

@app.route("/Turma", methods=["POST"])
def AddTurma():
    nv_dict = request.json
    nv_dict['Id'] = int(nv_dict['Id'])
    nv_dict['Professor Id'] = int(nv_dict['Professor Id'])

    try:
         
        if not modTur.ProfessorExistente(nv_dict["Professor Id"]):
            return jsonify({
                "Erro": "Requisição inválida",
                "Detalhes": "Id do Professor inexistente"
            }), 404   #inexistente | estava bad request

        if modTur.TurmaJaExiste(nv_dict["Id"]):
            return jsonify({
                "Erro": "Requisição inválida",
                "Detalhes": "Id da Turma já existente"
            }), 409  #conflict - duplicado ou duplo - estava 400 bad request
        modTur.CriarNovaTurma(nv_dict)
        return jsonify({"mensagem": "Turma criada com sucesso!", "turma": nv_dict}), 201
    
    except modTur.CadastroDeTurmaFalhado as cdtf:
         return jsonify({
            "Erro": "Falha ao cadastrar turma",
            "detalhes": str(cdtf)
         }), 400    

@app.route("/Turma/Resetar", methods=["DELETE"])
def ResetarTodaTurma():
     modTur.DeletarTurma()
     return jsonify({"mensagem": "Resetado"}), 200

@app.route("/Turma/Resetar/<int:id_turma>", methods=["DELETE"])
def ResetarTurmaId(id_turma):
     try:
          modTur.DeletarTurmaPorId(id_turma)
          return jsonify(modTur.dadosTurma["Turma"]), 200
     except modTur.TurmaNaoIdentificada as trm:
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
    
    resultado, status_code = modTur.AlterarInformacoes(id_turma, dados["Descrição"], dados["Ativa"], dados["Professor Id"])
    return jsonify(resultado), status_code      

# -------------------------------- PROFESSOR GET----------------------------------------#

@app.route('/professores', methods=['GET'])
def listar_professores():
    
    '''Mostra todos professores - geral'''
    
    professores = modProf.listar_professores() #trazendo do import
    
    try:
        return jsonify({"professor": professores["professor"]}) 
    except Exception as e:
        return jsonify({"error": f"Not Found: {str(e)}"}), 500 #tirei 500 internal erro e coloquei 404 not found 

@app.route("/professores/<int:id>", methods=["GET"])
def pesquisa_professor(id):
    try:
        professor = modProf.procurarProfessorPorId(id) #trazendo do import
        return jsonify({"mensagem": "Ok", "professor": professor}), 200
    except modProf.ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404
    
# ----------------------------------- PROFESSOR POST -----------------------------------#

@app.route('/professores', methods=['POST'])
def cadastrar_professores():
    novo_professor = request.json
    if not novo_professor or "nome" not in novo_professor or "materia" not in novo_professor:
        return jsonify({"erro": "Nome e matéria são obrigatórios"}), 400
    try:
        if modProf.ProfessorExistente(novo_professor["id"]):  # Correção: Verifica se o professor já existe
            raise modProf.ProfessorExiste("Professor já existe")
        modProf.criarNovoProfessor(novo_professor)
        return jsonify({"professor": novo_professor}), 201
    except modProf.ProfessorExiste as e:
        return jsonify({"erro": str(e)}), 400
    
# ----------------------------------- PROFESSOR PUT ---------------------------------------#

@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    atualizado = request.json
    try:
        professor = modProf.procurarProfessorPorId(id) # Correção: Usar a função de procurarProfessorPorId correta
        if "nome" in atualizado:
            professor['nome'] = atualizado['nome']
        if "idade" in atualizado:
            professor['idade'] = atualizado['idade']
        if "materia" in atualizado:
            professor['materia'] = atualizado['materia']
        if "obs" in atualizado:
            professor['obs'] = atualizado['obs']
        return jsonify({"professor": professor}), 200
    except modProf.ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": f"Internal Server Error: {str(e)}"}) # Correção: Mensagem de erro mais clara

@app.route("/professores/deletar/<int:id_professor>", methods=["DELETE"])
def delete_professor(id_professor):
    try:
        resultado = modProf.deletarProfessorPorId(id_professor)
        return jsonify(resultado), 200
    except modProf.ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404

@app.route('/professores/resetar', methods=['DELETE'])
def resetar_professor():
    resetar_professores()  # Função que reseta o dicionário de professores
    return jsonify({"mensagem": "Resetado"}), 200

# ----------------------------------- # PROFESSOR FIM # -----------------------------------#

# ----------------------------------- INICIO ALUNOS ---------------------------------------#


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


@app.route("/alunos/deletar/<int:id_aluno>", methods=["DELETE"])
def deletar_aluno_route(id_aluno):
    try:
        resultado = deletar_aluno_por_id(id_aluno)
        return jsonify(resultado), 200
    except AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404
    
@app.route('/alunos/resetar', methods=['DELETE'])
def resetar_alunoId():
    deletar_alunos()
    return jsonify({"mensagem": "Resetado"}), 200


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