from professores.model_prof import Professor
# import turma.model_turma as modAlu
from config import db_serv




# Aqui estão todas as classes para o Banco de Dados

class Turma(db_serv.Model):
    __tablename__ = "turmas"
    __table_args__ = {'extend_existing': True}

    id = db_serv.Column(db_serv.Integer, primary_key=True)
    descricao = db_serv.Column(db_serv.String(30),nullable=False)
    ativa = db_serv.Column(db_serv.Boolean,nullable=False)

    alunos = db_serv.relationship('Aluno', back_populates='turma')
    professor_id = db_serv.Column(db_serv.Integer, db_serv.ForeignKey("professor.id"),nullable=False)

    def __init__(self, id, descricao, ativa, professor_id):
        self.id = id
        self.descricao = descricao
        self.ativa = ativa
        self.professor_id = professor_id

    def to_dict(self):
        return {"id":self.id, "descricao":self.descricao,"ativa":self.ativa, "professor_id":self.professor_id}


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

# def apaga_tudo():
#     modAlu.dados['alunos'] = []
#     modPro.professores["Professor"] = []
#     dadosTurma["Turma"] = []

# def procurarTurmaPorId(id_turma):
#     for dict in dadosTurma["Turma"]:
#         if dict['Id'] == id_turma:
#                     return dict
#         raise TurmaNaoIdentificada()

def professorExistente(Id_professor):
    return Professor.query.get(Id_professor) is not None

def turmaJaExiste(id_turma):
    turma = Turma.query.get(id_turma)
    return turma is not None

    
def procurarTurmaPorId(id_turma): 
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoIdentificada()
    return turma.to_dict()


# def criarNovaTurma(nv_dict):
#     dadosTurma["Turma"].append(nv_dict)
#     return

def criarNovaTurma(nv_dict):
    nova_turma = Turma(
        id = nv_dict['id'],
        descricao = nv_dict['descricao'],
        professor_id= nv_dict['professor_id'],
        ativa = nv_dict['ativa']
    )

    db_serv.session.add(nova_turma)
    db_serv.session.commit()
    return {"Descrição":"Turma criada com êxito! "},200

# def listarTurma():
#     return dadosTurma["Turma"]

def listarTurma():
    turmas = Turma.query.all()
    #print(turmas)
    return [turma.to_dict() for turma in turmas]


# def deletarTurma():
#     dadosTurma["Turma"] = []

def deletarTurma():
    db_serv.session.delete()
    db_serv.session.commit()


# def deletarTurmaPorId(id_turma):
#     turmas = dadosTurma["Turma"]

#     for indice, turma in enumerate(turmas):
#         if turma["Id"] == id_turma:
#             turmas.pop(indice)
#             return {"Mensagem": "Turma deletada com sucesso."}
#     raise TurmaNaoIdentificada()

def deletarTurmaPorId(id_turma):
    turma = db_serv.session.query(Turma).get(id_turma)
    if turma is None:
        return {"message": f"Turma com ID {id_turma} não encontrada."}, 404
    db_serv.session.delete(turma)
    db_serv.session.commit()

def valoorBuleano(valorbool):
    if valorbool is True or valorbool is False:
        return True
    return False

# def alterarInformacoes(Id_turma, Descricao, Ativa, Id_Pro):
#     nv_dados = dadosTurma["Turma"]
#     try:
#         for turma in nv_dados:
#             if turma["Id"] == Id_turma:
#                 if not professorExistente(Id_Pro):
#                     return ({
#                         "Erro": "Requisição inválida",
#                         "Descrição": "Id do Professor inexistente"
#                     }), 400
#                 if not valoorBuleano(Ativa):
#                     return ({
#                         "Erro": "Requisição inválida",
#                         "Descricao": "Valor de Ativa incorreto. Digite True ou False"
#                     }), 409 
#                 turma["Descrição"] = Descricao
#                 turma["Professor Id"] = Id_Pro
#                 turma["Ativa"] = Ativa
#                 return {"Detalhes":"Turma atualizada com seucesso!"}, 200
#         return ({
#             "Erro": "Requisição inválida",
#             "Descrição": "Id da turma inexistente"
#         }), 400
#     except Exception as e:
#         return({
#             "Erro": "Não foi possível fazer a requisição",
#             "Descrição": str(e)
#         }), 500

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
        
        
        nv_dados.descricao = Descricao
        nv_dados.professor_id = Id_Pro
        nv_dados.ativa = Ativa
        db_serv.session.commit()
        return {"Detalhes":"Turma atualizada com seucesso!"}, 200
    
    except Exception as e:
        return ({
            "Erro":"Não foi possível fazer a requisição",
            "Descrição": str(e)
        }), 500

        
