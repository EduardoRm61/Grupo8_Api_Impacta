from flask import Flask, jsonify, request
# import model_turma as modTur - no app.py
app = Flask(__name__)


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

def listar_professores(): #estava sem
    return professores

# def apaga_tudo():
#     dados['alunos'] = []
#     modProf.professores["Professor"] = []
#     modTur.dadosTurma["Turma"] = []
#faz parte do turma



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