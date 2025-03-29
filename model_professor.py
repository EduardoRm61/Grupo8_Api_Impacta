from flask import Flask, jsonify, request
import model_turma as modTur
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


#Model
#Criando todas as classes de exceções:


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
# Ainda são dados e sua manupulação e armazenamento

def apaga_tudo():
    dados['alunos'] = []
    professores["Professor"] = []
    modTur.dadosTurma["Turma"] = []



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
    professores["professor"] = []
    return

def deletar_alunos():
    dados["alunos"] = []
    return
                
# Todas as rotas: São Controller 

if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)