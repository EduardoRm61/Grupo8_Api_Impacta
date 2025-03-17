from flask import Flask, jsonify

app = Flask(__name__)

dadosAluno = {"Aluno":[
    {"Id": 20, "Nome": "Thaina", "Idade": 28, "Turma_Id": 12, "Data de nascimento": 20/5/1996, "Nota do primeiro semestre": 8, "Nota do segundo semestre": 8, "Media Final": 8},
    {"Id": 20, "Nome": "Eduardo", "Idade": 20, "Turma_Id": 14, "Data de nascimento": 1/1/2005, "Nota do primeiro semestre": 10, "Nota do segundo semestre": 10, "Media Final": 10}
]}

dadosTurma = {"Turma":[
    {"Id": 1, "Descrição": "Banco de dados", "professor_id": 500, "Ativa": False},
    {"Id": 1, "Descrição": "Desenvolvimento Mobile", "professor_id": 555, "Ativa": True}
]}

#CLASSES

class AlunoNaoEncontrado(Exception):
    def __init__(self, msg = "EERO! Aluno não encontrado."):
        self.msg = msg
        super().__init__(self.msg)

class AlunoJaCadastrado(Exception):
    def __init__(self, msg = "ERRO! Aluno já está cadastrado no sistema."):
        self.msg = msg
        super().__init__(msg)

class TurmaNaoEncontrada(Exception):
    def __init__(self, msg = "ERRO! Turma não encontrada."):
        self.msg = msg 
        super().__init__(msg)

class TurmaJaCadastrada(Exception):
    def __init__(self, msg = "ERRO! Turma já está cadastrada no sistema."):
        self.msg = msg
        super().__init__(msg)

class FalhaAoCadastrarAluno(Exception):
    def __init__(self, msg = "ERRO, algum dado foi inserido errado, revise Id do Aluno e Id Turma."): #NÃO SEI SE PRECISA TER NA MENSAGEM ID TURMA
        super().__init__(msg)

class ValorBool(Exception): #COPIEI DO EDU, NÃO SEI SE PRECISA TER DUAS VEZES
    def __init__(self, msg = "Erro, valor Booleano incorreto, deigite True ou False."):
        self.msg = msg
        super().__init__(self.msg)

#REQUISIÇÕES

def ProcurarAlunoPorId(id_aluno):
    for dict in dadosAluno["Aluno"]:
        if dict['Id'] == id_aluno:
            return dict
        raise AlunoNaoEncontrado
    
def ProcurarTurmaPorId(id_turma): #OBS: NÃO SEI SE VAI PRECISAR
    for dict in dadosTurma["Turma"]:
        if dict['Id'] == id_turma:
            return dict
        raise TurmaNaoEncontrada
    
def CriarNovoAluno(nv_dict):
    dadosAluno["Aluno"].append(nv_dict)
    return

def ListarAlunos():
    return dadosAluno["Aluno"]

def DeletarAlunoPorId(id_aluno):
    alunos = dadosAluno["Aluno"]
    for indice, turma in enumerate(alunos):
        if alunos["Id"] == id_aluno:
            alunos.pop(indice)
            return {"Mensagem": "Aluno com id {id_aluno} foi deletado."}
        raise AlunoNaoEncontrado()
    
def AlunoJaExiste(id_aluno):
    for aluno in dadosAluno["Aluno"]:
        if aluno["Id"] == id_aluno:
            return True
        return False #DÁ PRA COLOCAR UMA MENSAGEM?
    
def TurmaJaExiste(Id_turma): #PRECISA ?
    for turma in dadosTurma["Turma"]:
        if turma["Id"] == Id_turma:
            return True
    return False

def ValoorBuleano(valorbool): #COPIEI DO EDU, NÃO SEI DE PRECISA TER DUAS VEZES
    if valorbool is True or valorbool is False:
        return True
    return False

def AlterarInformacoes(Id_aluno, Nome, Idade, Id_professor, Data_nascimento, Nota_primeiro_semestre, Nota_segundo_semestre, Media_final):
    novos_dados = dadosAluno["Aluno"]
    try:
        for aluno in novos_dados:
            if aluno["Id"] == Id_aluno:
                if not AlunoJaCadastrado(Id_aluno):
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

#ROTAS

@app.route("/Aluno", methods=["GET"])
def listar_alunos():
    Alunos = listar_alunos()
    return jsonify(Alunos)

@app.route("/Auno/<int:id_aluno>", methods=["GET"])
def encontrar_aluno (id_aluno):
    try:
        dados = ProcurarAlunoPorId(id_aluno)
        return jsonify(dados)
    except AlunoNaoEncontrado as aln:
        return jsonify({"ERRO": str(aln)}), 404
    
@app.route("/Aluno", methods=["POST"])
def criar_aluno():
    novo_dic = request.json
    novo_dic['Id'] = int(novo_dic['Id'])
    try:
        if not AlunoJaExiste(novo_dic["Id"]):
            return jsonify({
                "ERRO": "Requisição inválida.",
                "Mensagem": "Este Id já está associado a um aluno"
            }), 400
        CriarNovoAluno(novo_dic)
        return jsonify({"Mensagem": "Aluno criado com sucesso!", "Aluno": novo_dic}), 201
    except FalhaAoCadastrarAluno as fca:
        return jsonify({
            "ERRO": "Falha ao cadastrar novo aluno.",
            "Detalhes": str(fca)
        }), 400

@app.route("/alunos/<int:idAluno>", methods=['PUT'])
def atualizar_alunos(idAluno):
    try:
        novos_dados = request.json
        nome = novos_dados.get("Nome")
        idade = novos_dados.get("Idade")
        id_professor = novos_dados.get("Id_professor")
        data_nascimento = novos_dados.get("Data_nascimento")
        nota_primeiro_semestre = novos_dados.get("Nota_primeiro_semestre")
        nota_segundo_semestre = novos_dados.get("Nota_segundo_semestre")
        media_final = novos_dados.get("Media_final")

        resultado = AlterarInformacoes(
            idAluno,
            nome=nome,
            idade=idade,
            id_professor=id_professor,
            data_nascimento=data_nascimento,
            nota_primeiro_semestre=nota_primeiro_semestre,
            nota_segundo_semestre=nota_segundo_semestre,
            media_final=media_final
        )
        return jsonify(resultado), 200
    except AlunoNaoEncontrado as ane:
        return jsonify({"erro": str(ane)}), 404

  

if __name__ == '__main__':
    app.run(debug=True)
