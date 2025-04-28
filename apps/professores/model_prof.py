# msysql

from config import db_serv

# __________________INSTÂNCIANDO________________________________________
   
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
    
    def direcionar(self):
        
        '''função que relaciona a chave com dados, formando retorno de um dicinário'''
        
        return {
            "id" : self.id,
            "nome" : self.nome,
            "idade" : self.idade,
            "materia" : self.materia,
            "obs" : self.obs
        }

# ____________ CLASSE DE EXCEÇÃO NÃO É DADOS- DEIXAR________________________

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

# _________________________ FUNÇÕES________________________

# def apaga_tudo():
#      professores["Professor"] = []

def ProfessorExistente(Id_professor):
    return Professor.query.get(Id_professor) is not None


def procurarProfessorPorId(id_professor):   #def é minúscula
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoIdentificado()
    return professor.direcionar()

def criarNovoProfessor(new_direcionar):
    if not new_direcionar.get("id") or not new_direcionar.get("nome") or not new_direcionar.get("materia"):
    # se não tiver 1 ou 2 ou todos, falha
        raise CadastroDeProfessorFalhado()
    
    if ProfessorExistente(new_direcionar["id"]):
        raise ProfessorExiste()
    
    novo_professor = Professor (
        id=new_direcionar["id"],
        nome=new_direcionar["nome"],
        materia=new_direcionar["materia"],
        idade=new_direcionar.get("idade"),
        obs=new_direcionar.get("obs")
    )
        
    db_serv.session.add(novo_professor)  # add o objeto à sessão do banco de dados
    db_serv.session.commit()             # confirma a transação, grava o objeto no banco de dados mysql
    return novo_professor.to_dict()      # converte em diconário
    
    #cuidado com identação e abrir e fechar ( )

def deletarProfessorPorId(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoIdentificado
    
    db_serv.session.delete(professor)
    db_serv.session.commit()

def resetar_professores():
    professores["professor"] = []
    return


# ++++++++++++++++++++++++++++++++++++++ ok ++++++++++++++++++++++++++++++++++++++++++++++++++++++++