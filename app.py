from flask import Flask, jsonify, request


app = Flask(__name__)


dados = {
    "alunos": [
        {
            "Id": 20,
            "Nome": "Thaina",
            "Idade": 19,
            "Turma_Id": 12,
            "Data_nascimento": "10/08/2005",
            "Nota_Primeiro_Semestre": 8.0,
            "Nota_Segundo_semestre": 9.0,
        }
    ]
}


# Criando classes para minhas exceções:
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




# Aqui estão as funções auxiliares para as rotas:
def procurar_aluno_por_id(id_aluno):
    for aluno in dados["alunos"]:
        if aluno["Id"] == id_aluno:
            return aluno
    raise AlunoNaoIdentificado()

def criar_novo_aluno(novo_aluno):
    dados["alunos"].append(novo_aluno)
    return

def listar_alunos():
    return dados["alunos"]

def deletar_aluno_por_id(id_aluno):
    alunos = dados["alunos"]
    for indice, aluno in enumerate(alunos):
        if aluno["Id"] == id_aluno:
            alunos.pop(indice)
            return {"Mensagem": "Aluno deletado com sucesso."}
    raise AlunoNaoIdentificado()

def aluno_ja_existe(id_aluno):
    for aluno in dados["alunos"]:
        if aluno["Id"] == id_aluno:
            return True
    return False

def alterar_informacoes_aluno(id_aluno, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre): #NÃO SEI SE VAI PRECISAR
    try:
        for aluno in dados["alunos"]:
            if aluno["Id"] == id_aluno:
                aluno["Nome"] = nome
                aluno["Idade"] = idade
                aluno["Turma_Id"] = turma_id
                aluno["Data_nascimento"] = data_nascimento
                aluno["Nota_Primeiro_Semestre"] = nota_primeiro_semestre
                aluno["Nota_Segundo_semestre"] = nota_segundo_semestre
                return {"Detalhes": "Aluno atualizado com sucesso!"}, 200
        raise AlunoNaoIdentificado()
    except Exception as e:
        return {"Erro": "Não foi possível atualizar o aluno", "Descrição": str(e)}, 500


# Aqui estão todas as rotas:

@app.route("/") 
def hello():
        print("rodei mesmo") 
        return "Hello World!"


@app.route("/alunos", methods=["GET"])
def listar_alunos():
    alunos = ListarAlunos()
    return jsonify(alunos), 200

@app.route("/Auno/<int:id_aluno>", methods=["GET"])
def encontrar_aluno (id_aluno):
    try:
        aluno = ProcurarAlunoPorId(id_aluno)
        return jsonify(aluno)
    except AlunoNaoIdentificado as ani:
        return jsonify({"ERRO": str(ani)}), 404
    
@app.route("/aluno", methods=["POST"])
def criar_aluno():
    nv_dict = request.json
    nv_dict["Id"] = int(nv_dict["Id"])
    nv_dict["Id_aluno"] = int(nv_dict["Id_aluno"])
    try:
        nv_dict = request.json
        if not AlunoJaExiste(nv_dict["id_aluno"]):
            return jsonify({
                "ERRO": "Requisição inválida.",
                "Mensagem": "Os campos 'Id' é obrigatório."
            }), 400

        CriarNovoAluno(nv_dict)
        return jsonify({
            "Mensagem": "Aluno criado com sucesso!",
            "alunos": ListarAlunos()
        }), 201

    except Exception as e:
        return jsonify({
            "ERRO": "Falha ao cadastrar novo aluno.",
            "Detalhes": str(e)
        }), 500

@app.route("/alunos/<int:idAluno>", methods=['PUT'])
def atualizar_alunos(idAluno):
    try:
        novos_dados = request.json
        nome = novos_dados.get("Nome")
        resultado = AlterarInformacoes(idAluno, nome=nome)
        return jsonify(resultado), 200
    except AlunoNaoIdentificado as ani:
        return jsonify({"erro": str(ani)}), 404
    
@app.route("/aluno/resetar/<int:id_aluno>", methods=["DELETE"])
def resetar_aluno_Id(id_aluno):
    try:
        resetar_aluno_Id(id_aluno)
        return jsonify(dados["alunos"]), 200
    except AlunoNaoIdentificado as ani:
          return jsonify({"Erro:": str(ani)}), 404


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug=True)





