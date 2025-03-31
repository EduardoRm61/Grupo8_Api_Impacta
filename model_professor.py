from flask import Flask, jsonify, request
# import model_turma as modTur - no app.py
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
    
def resetar_professores():
    professores["professor"] = []
    return


# Todas as rotas: São Controller 

if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)