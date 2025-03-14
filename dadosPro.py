#import professor as prof

dadosTurma = {"Turma":[
    {"Id": 12, "Descrição": "Eng. Software","Ativa": True,"Professor Id": dados.prof},
    {"Id": 14, "Descrição": "Análise e Desen. de Sistemas", "Ativa": False, "Professor Id": dados.prof}     #o Id do professor não estou desenvolvendo, quando estiver pronto eu importareo
]}

class ProfessorNaoIdentificado(Exception):
    def __init__(self,msg="Erro, Professor não indentificado ou inexistente"):
        self.msg = msg
        super().__init__(self.msg)

def listProfessor(id_Professor):
    id_Profs = [professor]              # Aqui eu puxo de dados, onde estará professor.
    for Ids in id_Profs:
        if Ids["Id"] == id_Professor:
            return Ids
        raise ProfessorNaoIdentificado()
    
        
def addProfessor(novo_dict):
    return dadosTurma["Turma"].append(novo_dict)