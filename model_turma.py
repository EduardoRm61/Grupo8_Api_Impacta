import model_professor as modPro
import model_aluno as modAlu


dadosTurma = {"Turma":[
    {"Id": 12, "Descrição": "Eng. Software","Ativa": True,"Professor Id": 10},
    {"Id": 14, "Descrição": "Análise e Desen. de Sistemas", "Ativa": False, "Professor Id": 11}     
]} 

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

#Aqui estão as funções auxiliares para Turma em app.py:

def apaga_tudo():
    modAlu.dados['alunos'] = []
    modPro.professores["Professor"] = []
    dadosTurma["Turma"] = []

def ProcurarTurmaPorId(id_turma):
            for dict in dadosTurma["Turma"]:
                if dict['Id'] == id_turma:
                    return dict
            raise TurmaNaoIdentificada()

def CriarNovaTurma(nv_dict):
    dadosTurma["Turma"].append(nv_dict)
    return

def ListarTurma():
    return dadosTurma["Turma"]

def DeletarTurma():
    dadosTurma["Turma"] = []


def DeletarTurmaPorId(id_turma):
    turmas = dadosTurma["Turma"]

    for indice, turma in enumerate(turmas):
        if turma["Id"] == id_turma:
            turmas.pop(indice)
            return {"Mensagem": "Turma deletada com sucesso."}
    raise TurmaNaoIdentificada()

def ValoorBuleano(valorbool):
    if valorbool is True or valorbool is False:
        return True
    return False

def AlterarInformacoes(Id_turma, Descricao, Ativa, Id_Pro):
    nv_dados = dadosTurma["Turma"]
    try:
        for turma in nv_dados:
            if turma["Id"] == Id_turma:
                if not ProfessorExistente(Id_Pro):
                    return ({
                        "Erro": "Requisição inválida",
                        "Descrição": "Id do Professor inexistente"
                    }), 400
                if not ValoorBuleano(Ativa):
                    return ({
                        "Erro": "Requisição inválida",
                        "Descricao": "Valor de Ativa incorreto. Digite True ou False"
                    }), 409 
                turma["Descrição"] = Descricao
                turma["Professor Id"] = Id_Pro
                turma["Ativa"] = Ativa
                return {"Detalhes":"Turma atualizada com seucesso!"}, 200
        return ({
            "Erro": "Requisição inválida",
            "Descrição": "Id da turma inexistente"
        }), 400
    except Exception as e:
        return({
            "Erro": "Não foi possível fazer a requisição",
            "Descrição": str(e)
        }), 500
    
def TurmaJaExiste(Id_turma):
    for turma in dadosTurma["Turma"]:
        if turma["Id"] == Id_turma:
            return True
    return False

def ProfessorExistente(Id_professor):
    for professor in modPro.professores["professor"]:
        if professor["id"] == Id_professor:
            return True  
    return False