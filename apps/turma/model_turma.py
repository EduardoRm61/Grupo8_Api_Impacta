import apps.professores.model_prof as modPro
import apps.turma.model_turma as modAlu
import professores.model_prof as modclas
from ..config import db_serv


    
#Aqui estão todas as classes de exceções:

class ProfessorExiste(Exception):
    def __init__(self, msg="Professor já existente"):
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

class TurmaNaoIdentificada(Exception):
    def __init__(self, msg="Erro, Turma não identificada ou inexistente!"):
        self.msg = msg
        super().__init__(self.msg)

class TurmaJaDeletada(Exception):
    def __init__(self, msg= "Erro, Turma já deletada ou inexistente!!"):
        self.msg = msg
        super().__init__(msg)

#Aqui estão as funções auxiliares para Turma em app.py:

class Turma(db_serv.Model):
    __tablename__ = "turmas"
    id = db_serv.Column(db_serv.Integer, primary_key=True)
    descricao = db_serv.Column(db_serv.String(30),nullable=False)
    ativa = db_serv.Column(db_serv.Boolean,nullable=False)
    professor_id = db_serv.Column(db_serv.Integer, db_serv.ForeignKey("professor.id"),nullable=False)    

    def __init__(self, id, descricao, ativa, professor_id):
        self.id = id
        self.descricao = descricao
        self.ativa = ativa
        self.professor_id = professor_id

    def to_dict(self):
        return {"id":self.id, "descricao":self.descricao,"ativa":self.ativa, "professor_id":self.professor_id}



def TrumaJaExiste(Id_turma):
    try: 
        dic = Turma.query.get(Id_turma)
        if dic == None:
            return False
        return True
    except Exception:
        return False


def professorExistente(Id_professor):
    try:
        dic = modclas.Professor.query.get(Id_professor)
        if dic == None:
            return False
        return True
    except Exception:
        return False
    


def procurarTurmaPorId(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoIdentificada()
    return turma.to_dict()

def criarNovaTurma(nv_dict):
    db_serv.session.add(nv_dict)
    db_serv.session.commit()
    return {"Descrição":"Turma criada com êxito! "},200

def listarTurma():
    turmas = Turma.query.all()
    print(turmas)
    return [turma.to_dict() for turma in turmas]

def deletarTurma():
    db_serv.session.delete()
    db_serv.session.commit()


def deletarTurmaPorId(id_turma):
    db_serv.session.delete(id_turma)
    db_serv.session.commit()


def valoorBuleano(valorbool):
    if valorbool is True or valorbool is False:
        return True
    return False

def alterarInformacoes(Id_turma, Descricao, Ativa, Id_Pro):
    nv_dados = Turma.query.get(Id_turma)
    try:
        if not nv_dados:
            raise TurmaNaoIdentificada()
        
        if not professorExistente(Id_Pro):
            return ({
                "Erro": "Requisição inválida",
                "Descrição": "Id do Professor inexistente"
                }), 400
        
        if not valoorBuleano(Ativa):
            return ({
                "Erro": "Requisição inválida",
                "Descricao": "Valor de Ativa incorreto. Digite True ou False"
                    }), 409
        
        
        nv_dados["Descrição"] = Descricao
        nv_dados["Professor Id"] = Id_Pro
        nv_dados["Ativa"] = Ativa
        db_serv.session.commit()
        return {"Detalhes":"Turma atualizada com seucesso!"}, 200
    
    except Exception as e:
        return ({
            "Erro":"Não foi possível fazer a requisição",
            "Descrição": str(e)
        }), 500
    
