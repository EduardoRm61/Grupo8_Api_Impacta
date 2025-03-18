from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados iniciais
dados = {
    "alunos": [
    {"Id": 20, "Nome": "Thaina", "Idade": 28, "Turma_Id": 12, "Data de nascimento": 20/5/1996, "Nota do primeiro semestre": 8, "Nota do segundo semestre": 8, "Media Final": 8},
    {"Id": 20, "Nome": "Eduardo", "Idade": 20, "Turma_Id": 14, "Data de nascimento": 1/1/2005, "Nota do primeiro semestre": 10, "Nota do segundo semestre": 10, "Media Final": 10}

    ],
    "professores": []
}


# Classes de exceções para possíveis erros no código

class AlunoNaoIdentificado(Exception):
    def __init__(self, msg="Erro, Aluno não identificado ou inexistente!"):
        self.msg = msg
        super().__init__(self.msg)

class AlunoJaExistente(Exception):
    def __init__(self, msg="Erro, Aluno já existente!"):
        self.msg = msg
        super().__init__(self.msg)

class CadastroDeAlunoFalhado(Exception):
    def __init__(self, msg="Erro, Falha ao cadastrar aluno. Verifique os dados!"):
        self.msg = msg
        super().__init__(self.msg)

class AtualizacaoAlunoFalhou(Exception):
    def __init__(self, msg="Erro, Não foi possível atualizar os dados do aluno. Verifique os campos!"):
        self.msg = msg
        super().__init__(self.msg)

# Aqui estão as funções auxiliares para as rotas:

def ListarAlunos():
    return dados["alunos"]

def CriarNovoAluno(nv_dict):
    dados["Aluno"].append(nv_dict)
    return

def DeletarTodosAlunos():
    dados["alunos"] = []
    return

def DeletarAlunoPorId(id_aluno):
    alunos = dados["Aluno"]
    for indice, alunos in enumerate(alunos):
        if alunos["Id"] == id_aluno:
            alunos.pop(indice)
            return {"Mensagem": "Aluno foi deletado."}
        raise AlunoNaoIdentificado()

def ProcurarAlunoPorId(id_aluno):
    for dict in dados["Aluno"]:
        if dict['Id'] == id_aluno:
            return dict
        raise AlunoNaoIdentificado
    
def AlunoJaExiste(id_aluno):
    for aluno in dados["Aluno"]:
        if aluno["Id"] == id_aluno:
            return True
        return False
    
def AlterarInformacoes(Id_aluno, Nome, Idade, Id_professor, Data_nascimento, Nota_primeiro_semestre, Nota_segundo_semestre, Media_final):
    novos_dados = dados["Aluno"]
    try:
        for aluno in novos_dados:
            if aluno["Id"] == Id_aluno:
                if not AlunoJaExistente(Id_aluno):
                    return({
                        "ERRO": "Aluno já cadastrado com esse Id"
                    }), 400
            aluno["Nome"] = Nome
            aluno["Idade"] = Idade
            aluno["Id professor"] = Id_professor
            aluno["Data_nascimento"] = Data_nascimento
            aluno["Nota do Primeiro Semestre"] = Nota_primeiro_semestre
            aluno["Nota do Segundo Semestre"] = Nota_segundo_semestre
            aluno["Média Final"] = Media_final
            return {"Aluno atualizado com sucesso!"}, 200
        return({
            "ERRO": "Este Id já está associado a um aluno."
    }), 400 #400 ou 404?
    except Exception as e:
        return({
            "ERRO": "Não é possível fazer essa requisição",
            "Descrição": str(e)
        })
    

# Aqui estão todas as rotas:

@app.route("/alunos", methods=["GET"])
def listar_alunos():
    alunos = ListarAlunos()
    return jsonify(alunos), 200