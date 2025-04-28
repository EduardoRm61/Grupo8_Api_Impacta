# msysql

from config import db_serv


   
class Professor(db_serv.Model):
    id = db_serv.Column(db_serv.Integer, primary_key=True, NotNullable=False)
    nome = db_serv.Column(db_serv.String (100), NotNullable=False)
    idade = db_serv.Column(db_serv.Integer)
    materia = db_serv.Column(db_serv.String (150), NotNullable=False)
    idade = db_serv.Column(db_serv.Integer)
    
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

class ProfessorNaoIdentificado(Exception):
    def __init__(self,msg="Erro, Professor não indentificado ou existente!"):
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

def apaga_tudo():
     professores["Professor"] = []

def ProfessorExistente(Id_professor):
    for professor in professores["professor"]:
        if professor["id"] == Id_professor:
            return True  
    return False


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


# ++++++++++++++++++++++++++++++++++++++ ok ++++++++++++++++++++++++++++++++++++++++++++++++++++++++