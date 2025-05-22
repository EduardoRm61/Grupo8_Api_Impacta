from ..config import db_serv

class Professor (db_serv.Model):
    id = db_serv.Column(db_serv.Integer, primary_key=True, nullable=False) 
    nome = db_serv.Column(db_serv.String (100), nullable=False)
    idade = db_serv.Column(db_serv.Integer)  
    materia = db_serv.Column(db_serv.String (100), nullable=False)
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

class CadastroDeProfessorFalhado(Exception): 
    def __init__(self, msg="ID, nome e matéria são obrigatórios"):
        self.msg = msg
        super().__init__(self.msg)

# _________________________ FUNÇÕES________________________
 
def ProfessorExistente(Id_professor): 
    try:  
        return Professor.query.get(Id_professor) is not None
    except Exception as e:
        raise Exception (f"Erro, Professor não indentificado ou existente: {str(e)}")


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
            
        db_serv.session.add(novo_professor)  
        db_serv.session.commit()  
        return novo_professor.direcionar()     
    
    except (CadastroDeProfessorFalhado, ProfessorExiste):
        raise
    except Exception as e:
        db_serv.session.rollback()
        raise Exception(f"{str(e)}: Erro ao criar o professor")
        

        
def atualizarProfessor(id_professor, novo_dado ):
    try:
        professor = Professor.query.get(id_professor)
        if not professor:
            raise ProfessorNaoIdentificado
        
        if "id" in novo_dado:
            professor.id = novo_dado["id"]
        if "nome" in novo_dado:
            professor.nome = novo_dado["nome"]
        if "idade" in novo_dado:
            professor.idade = novo_dado["idade"]
        if "materia" in novo_dado:
            professor.materia = novo_dado["materia"]
        if "obs" in novo_dado:
            professor.obs = novo_dado["obs"]

        
        db_serv.session.commit()
    
    except (ProfessorNaoIdentificado, CadastroDeProfessorFalhado):
        raise
    except Exception as e:
        db_serv.session.rollback()
        raise Exception(f"{str(e)}: Falha ao atualizar professor")
    
def deletarProfessorPorId(id_professor): 
    try:
        professor = Professor.query.get(id_professor)
        if not professor:
            raise ProfessorNaoIdentificado()
        
        nome_del = professor.nome
        
        db_serv.session.delete(professor)
        db_serv.session.commit()
        return {"mensagem": f"Professor {nome_del} eletado"}
    
    except ProfessorNaoIdentificado:
        raise
    except Exception as e:
        db_serv.session.rollback()
        raise Exception(f"{str(e)}: Erro ao deletar professor {nome_del}")

def resetar_professores():
    try:
        dict_prof_del = Professor.query.delete()
        db_serv.session.commit()
        return {"mensagem": f"{dict_prof_del} professor resetado"}, 200


#------------------------------------QUERY--------------------------------------

    except Exception as e:
        db_serv.session.rollback()
        raise Exception(f"{str(e)}: Erro ao resetar professor")
