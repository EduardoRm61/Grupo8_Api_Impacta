# msysql

from config import db_serv


   
class Professor(db_serv.Model):
    
    '''Criando Mysql/classe professor com suas variáveis separadas em colunas, com tipo, referêncoia de chave e nulabilidade '''
    
    id = db_serv.Column(db_serv.Integer, primary_key=True, NotNullable=False)
    nome = db_serv.Column(db_serv.String (100), NotNullable=False)
    idade = db_serv.Column(db_serv.Integer)
    materia = db_serv.Column(db_serv.String (100), NotNullable=False)
    obs = db_serv.Column(db_serv.String (200))
    
    def __init__(self, id, nome, materia, idade=None, obs=None):
        
        '''função para instanciar este objeto professor, com seus parametro
        #lembrando que none é vazia, sendo assim não obrigatório'''
        
        self.id = id
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.obs = obs
    
    def direcionar (self):
        
        '''função que relaciona a chave com dados, formando retorno de um dicinário'''
        
        return {
            "id" : self.id,
            "nome" : self.nome,
            "idade" : self.idade,
            "materia" : self.materia,
            "obs" : self.obs
        }


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