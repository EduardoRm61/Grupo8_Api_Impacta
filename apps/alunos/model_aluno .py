from datetime import datetime
from ..config import db_serv
#from apps.turma.model_turma import dadosTurma 
from apps.turma.model_turma import dadosTurma 

class Aluno(db_serv.Model):
    __tablename__ = "alunos"

    id = db_serv.Column(db_serv.Integer, primary_key=True)
    nome = db_serv.Column(db_serv.String(100), nullable=False)
    idade = db_serv.Column(db_serv.Integer, nullable=False)
    data_nascimento = db_serv.Column(db_serv.Date, nullable=False)
    nota_primeiro_semestre = db_serv.Column(db_serv.Float, nullable=False)
    nota_segundo_semestre = db_serv.Column(db_serv.Float, nullable=False)
    media_final = db_serv.Column(db_serv.Float, nullable=False)

#RELAÇÃO DA CHAVE ESTRANGEIRA
    turma_id = db_serv.Column(db_serv.Integer, db_serv.ForeignKey('turma_id'), nullable=False) #CHAVE ESTRANGEIRA --não sei se tenho que colocar id_turma como está em model_turma
    turma = db_serv.relationship("Turma", back_populates="alunos") 
    #foreignKey = cria o vínculo no BANCO DE DADOS
    #relationship = cria vínculo no CÓGIDO PYTHON
    #back_populates = torna o RELACIONAMENTO BIDERICIONAL

    def __init__(self, nome, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, turma_id):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = self.calcular_media()
        self.idade = self.calcular_idade()
        self.turma_id = turma_id

##
def calcular_media(self):
    media = (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2
    mediaFim = f"{media:.1f}"
    return mediaFim
   

def calcular_idade(self):
    if not self.data_nascimento:  
        return None
    try:
        data_nasc = datetime.strptime(self.data_nascimento, '%d/%m/%Y')
        data_atual = datetime.today()
        idade = data_atual.year - data_nasc.year - ((data_atual.month, data_atual.day) < (data_nasc.month, data_nasc.day))
        return idade
    except ValueError:
        return None

##
def procurar_aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno) 
    if aluno:
        return aluno
    raise AlunoNaoIdentificado()

def listar_aluno():
    alunos = Aluno.query.all()
    print(alunos)

def criar_novo_aluno(novo_aluno):
    #verifica se turma existe, se não existir vai aparecer o erro 404, se existir o código continua
    turma = turma.query.get(novo_aluno['turma_id'])
    if(turma is None):
        return {"Turma não encontrada"}, 404

    adc_aluno = Aluno(
        nome = novo_aluno['nome'],
        data_nascimento = datetime.strftime(novo_aluno['data_nascimento'], "%d/%m/%Y"),
        nota_primeiro_semestre = float(novo_aluno['nota_primeiro_semestre']),
        nota_segundo_semestre = float(novo_aluno['nota_segundo_semestre']),
        turma_id = int(novo_aluno['turma_id'])
    )

    db_serv.session.add(adc_aluno)  
    db_serv.session.commit()            
    return {"Resposta":"Aluno criado com sucesso!"}, 201


def deletar_aluno_por_id(id_aluno):
    aluno = db_serv.session.get(Aluno, id_aluno) 
    if not aluno:
        raise AlunoNaoIdentificado()
    
    db_serv.session.delete(aluno)  
    db_serv.session.commit()      
    return {"Mensagem": "Aluno deletado com sucesso."}

def alterar_informacoes_aluno(id_aluno, novo_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoIdentificado()
    
    aluno.nome = novo_aluno['nome']
    aluno.idade = aluno.calcular_idade()
    aluno.data_nascimento = novo_aluno['data_nascimento']
    aluno.nota_primeiro_semestre = novo_aluno['nota_primeiro_semestre']
    aluno.nota_segundo_semestre = novo_aluno['nota_segundo_semestre']
    aluno.media = novo_aluno.calcular_media()
    aluno.turma.id = novo_aluno['turma_id']

    db_serv.session.commit()

def aluno_ja_existe(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if aluno: #se o aluno existir, levanta a exceção
        raise AlunoExistente()

##
class AlunoNaoIdentificado(Exception):
    def _init_(self, msg="Erro, Aluno não identificado ou inexistente!"):
        self.msg = msg
        super()._init_(self.msg)

class AlunoExistente(Exception):
    def _init_(self, msg="Erro, Aluno já existente!"):
        self.msg = msg
        super()._init_(self.msg)

class CadastroDeAlunoFalhado(Exception):
    def _init_(self, msg="Erro, Id do aluno ou Turma_Id incorretos!"):
        self.msg = msg
        super()._init_(self.msg)

class AtualizacaoAlunoFalhou(Exception):
    def _init_(self, msg="Erro, Não foi possível atualizar os dados do aluno! Reveja os campos e preencha corretamente"):
        self.msg = msg
        super()._init_(self.msg)

##

def procurar_aluno_por_id(id_aluno): #ok
    for aluno in dados["alunos"]:
        if aluno["Id"] == id_aluno:
            return aluno
    raise AlunoNaoIdentificado()

def criar_novo_aluno(novo_aluno): #ok
    dados["alunos"].append(novo_aluno)
    return {"Resposta":"Aluno criando com sucesso"}

def listar_alunos(): #ok
    return dados["alunos"]

def deletar_aluno_por_id(id_aluno): #ok
    alunos = dados["alunos"]
    for indice, aluno in enumerate(alunos):
        if aluno["Id"] == id_aluno:
            alunos.pop(indice)
            return {"Mensagem": "Aluno deletado com sucesso."}
    raise AlunoNaoIdentificado()

def aluno_ja_existe(id_aluno): #ok
    for aluno in dados["alunos"]:
        if aluno["Id"] == id_aluno:
            return True
    return False

def alterar_informacoes_aluno(id_aluno, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final): #NÃO SEI SE VAI PRECISAR
    try: #ok
        for aluno in dados["alunos"]:
            if aluno["Id"] == id_aluno:
                aluno["Nome"] = nome
                aluno["Idade"] = idade
                aluno["Turma_Id"] = turma_id
                aluno["Data_nascimento"] = data_nascimento
                aluno["Nota_Primeiro_Semestre"] = nota_primeiro_semestre
                aluno["Nota_Segundo_semestre"] = nota_segundo_semestre
                aluno["Media_final"] = media_final
                return {"Detalhes": "Aluno atualizado com sucesso!"}, 200
        raise AlunoNaoIdentificado()
    except Exception as e:
        return {"Erro": "Não foi possível atualizar o aluno", "Descrição": str(e)}, 500

def deletar_alunos():
    dados["alunos"] = []
    return

