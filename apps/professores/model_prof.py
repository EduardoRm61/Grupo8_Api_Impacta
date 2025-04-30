from config import db_serv

class Professor (db.Model):
    id = db_serv.Column(db.Integer, primary_key=True, nullable=False)       # cuidado estava column
    nome = db_serv.Column(db.String (100), nullable=False)
    idade = db_serv.Column(db.Integer)  # cuidado estava nullabe
    materia = db_serv.Column(db.String (100), nullable=False)
    obs = db_serv.Column(db.String (200))   

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
    try:  
        return Professor.query.get(Id_professor) is not None
    except Exception as e:
        raise Exception (f"Erro, Professor não indentificado ou existente!: {str(e)}")

# sem esquecer que str(e) é transformar em string o objeto/mensagem exeção 2° tipo de erro (classe+mensagem do .py), 1° mesagem do erro personalizada

def procurarProfessorPorId(id_professor):   
    try:
        professor = Professor.query.get(id_professor)
        if not professor:
            raise ProfessorNaoIdentificado()
        return professor.direcionar()
    
    except ProfessorNaoIdentificado:
        raise
    except Exception as e:
        raise Exception(f"Erro, Professor não indentificado ou existente: {str(e)}")


def criarNovoProfessor(new_direcionar):
    try:
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
        return novo_professor.direcionar()      # converte em diconário
    
    except (CadastroDeProfessorFalhado, ProfessorExiste):
        raise
    except Exception as e:
        db_serv.session.rollback()
        # sessão do banco de dados/zona de trabalho - db_serv.session
        # evitar dados inconsistentes no banco, desfazendo operações realizadas no último commit
        raise Exception(f"{str(e)}: Erro ao criar o professor")
        
        #cuidado com identação e abrir e fechar ( )
        
def atualizarProfessor(id_professor, novo_dado ):
    try:
        professor = Professor.query.get(id_professor)
        if not professor:
            raise ProfessorNaoIdentificado
        
        # professor.id = novo_dado["id"]
        # professor.nome = novo_dado["nome"]
        # professor.idade = novo_dado["idade"]
        # professor.materia = novo_dado["materia"]
        # professor.obs = novo_dado["obs"]
        # estava nesta forma mas ela é um bloco fechado e inflexível, então se não add qualquer um deles dará retorno de erro de KeyError e quebra o cód
        # aqui não vê linha por linhas, não é unidade, é grupo 
        
        # aforma posta/ corrigida é flexível, e corre de linha em linha, se não for da chave, passa para próxima, se for, atua e vai para próxima ou sai e segue o cód. Então se não tem uma informação, ele não quebra, ele pula e segue
        # é algo unitário, diferente da forma posta antes
        
        db_serv.session.commit()
    
        return professor.direcionar()
    
    except (ProfessorNaoIdentificado, CadastroDeProfessorFalhado):
        raise
    except Exception as e:
        db_serv.session.rollback()
        raise Exception(f"{str(e)}: Falha ao atualizar professor")
    
def deletarProfessorPorId(id_professor): #excluir aluno
    try:
        nome_del = professor.nome
        
        professor = Professor.query.get(id_professor)
        if not professor:
            raise ProfessorNaoIdentificado()
        
        # variável para receber quem será deletado e guardar informação
        
        
        db_serv.session.delete(professor)
        db_serv.session.commit()
        return {"mensagem": f"Professor {nome_del} eletado com sucesso"}
    
    except ProfessorNaoIdentificado:
        raise
    except Exception as e:
        db_serv.session.rollback()
        raise Exception(f"{str(e)}: Erro ao deletar professor {nome_del}")

def resetar_professores():
    try:
        Professor.query.delete()
        db_serv.session.commit()
        return
    
    except Exception as e:
        db_serv.session.rollback()
        raise Exception(f"{str(e)}: Erro ao resetar professor")


# ++++++++++++++++++++++++++++++++++++++ ok ++++++++++++++++++++++++++++++++++++++++++++++++++++++++