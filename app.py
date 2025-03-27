from flask import Flask, jsonify, request


app = Flask(__name__)


dados = {
    "alunos": [
        {
            "Id": 20,
            "Nome": "Thaina",
            "Idade": 28,
            "Turma_Id": 12,
            "Data_nascimento": "10/08/2005",
            "Nota_Primeiro_Semestre": 8.0,
            "Nota_Segundo_semestre": 9.0,
            "Media_final": 8.5
        },

        {
            "Id": 25,
            "Nome": "Rafaela",
            "Idade": 25,
            "Turma_Id": 16,
            "Data_nascimento": "10/09/2000",
            "Nota_Primeiro_Semestre": 6.0,
            "Nota_Segundo_semestre": 9.0, 
            "Media_final": 7.5
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

def alterar_informacoes_aluno(id_aluno, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre, media_final): #NÃO SEI SE VAI PRECISAR
    try:
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


# Aqui estão todas as rotas:
@app.route("/alunos", methods=["GET"])
def listar_alunos_route():
    alunos = listar_alunos()
    return jsonify(alunos)

@app.route("/alunos/<int:id_aluno>", methods=["GET"])
def procurar_aluno_route(id_aluno):
    try:
        aluno = procurar_aluno_por_id(id_aluno)
        return jsonify(aluno)
    except AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404

@app.route("/alunos", methods=["POST"])
def adicionar_aluno():
    novo_aluno = request.json
    novo_aluno["Id"] = int(novo_aluno["Id"])
    novo_aluno["Turma_Id"] = int(novo_aluno["Turma_Id"])

    try:
        if aluno_ja_existe(novo_aluno["Id"]):
            raise AlunoExistente()
        criar_novo_aluno(novo_aluno)
        return jsonify({"mensagem": "Aluno criado com sucesso!", "aluno": novo_aluno}), 201
    except AlunoExistente as e:
        return jsonify({"Erro": str(e)}), 400
    except Exception as e:
        return jsonify({"Erro": "Falha ao cadastrar aluno", "Detalhes": str(e)}), 400

@app.route("/alunos/<int:id_aluno>", methods=["DELETE"])
def deletar_aluno_route(id_aluno):
    try:
        resultado = deletar_aluno_por_id(id_aluno)
        return jsonify(resultado), 200
    except AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404

@app.route("/alunos/<int:id_aluno>", methods=["PUT"])
def alterar_aluno_route(id_aluno):
    dados_aluno = request.json

    if not dados_aluno:
        return jsonify({
            "Erro": "Requisição inválida",
            "Descrição": "O corpo da requisição está vazio, preencha todos os campos"
        }), 400

    try:
        resultado, status_code = alterar_informacoes_aluno(
            id_aluno,
            dados_aluno.get("Nome"),
            dados_aluno.get("Idade"),
            dados_aluno.get("Turma_Id"),
            dados_aluno.get("Data_nascimento"),
            dados_aluno.get("Nota_Primeiro_Semestre"),
            dados_aluno.get("Nota_Segundo_semestre"),
            dados_aluno.get("media_final")
        )
        return jsonify(resultado), status_code
    except AlunoNaoIdentificado as e:
        return jsonify({"Erro": str(e)}), 404
    except Exception as e:
        return jsonify({"Erro": "Falha ao atualizar aluno", "Detalhes": str(e)}), 500



###### TESTES##### 
import requests
import unittest


class TestStringMethods(unittest.TestCase):

    def teste_000_lista_turmaGET(self):
        r = requests.get('http://localhost:5002/Turma')

        if r.status_code == 404:
            self.fail("voce nao definiu a pagina /Turma no seu server")
        try:
            obj_return = r.json()
        except:
            self.fail("O Retorndo deve ser em JSON")
        self.assertEqual(type(obj_return),type([]))

    def test_001_criar_turmaPOST(self):
        try:
            # Cria a primeira turma
            r1 = requests.post('http://localhost:5002/Turma', json={"Id": 22, "Descrição": "Eng. Requisitos", "Ativa": False, "Professor Id": 12})
            if r1.status_code != 201:  # 201 significa "Created"
                self.fail(f"Falha ao criar a turma 01. Status code: {r1.status_code}")

            # Cria a segunda turma
            r2 = requests.post('http://localhost:5002/Turma', json={"Id": 13, "Descrição": "Eng. Sistemas", "Ativa": True, "Professor Id": 12})
            if r2.status_code != 201:
                self.fail(f"Falha ao criar a turma 02. Status code: {r2.status_code}")

            # Obtém a lista de turmas
            r_list = requests.get('http://localhost:5002/Turma')
            if r_list.status_code != 200:
                self.fail(f"Falha ao obter a lista de turmas. Status code: {r_list.status_code}")

            r_list_return = r_list.json()  # Corrigido: usa json() para obter o conteúdo

            # Verifica se as turmas foram criadas corretamente
            turma01_encontrada = False
            turma02_encontrada = False

            for turma in r_list_return:
                if turma['Id'] == 22:
                    turma01_encontrada = True
                if turma['Id'] == 13:
                    turma02_encontrada = True

            if not turma01_encontrada:
                self.fail('Turma 01 não encontrada na lista de turmas')
            if not turma02_encontrada:
                self.fail('Turma 02 não encontrada na lista de turmas')

        except requests.exceptions.RequestException as e:
            self.fail(f"Erro ao fazer requisição: {e}")

    def test_002_pesquisaId_turma(self):
        # base_url = 'http://localhost:5002/Turma'
        
    

        r = requests.post('http://localhost:5002/Turma',json={
            "Id": 23,
            "Descrição": "Banco de Dados",
            "Ativa": False,
            "Professor Id": 12 })
        

        resposta = requests.get('http://localhost:5002/Turma/23')
        dict_return = resposta.json()
        self.assertEqual(type(dict_return),dict)
        self.assertIn('Id',dict_return)
        self.assertEqual(dict_return['Id'],23)

    def test_003_resetar(self):

        r = requests.post('http://localhost:5002/Turma',json={
            "Id": 24,
            "Descrição": "Banco de Dados",
            "Ativa": False,
            "Professor Id": 12 })
        
        r_list = requests.get('http://localhost:5002/Turma')
        self.assertTrue(len(r_list.json()) > 0)
        r_reset = requests.delete('http://localhost:5002/Turma/Resetar')
        self.assertEqual(r_reset.status_code,200)
        r_nvlist = requests.get('http://localhost:5002/Turma')
        self.assertEqual(len(r_nvlist.json()),0)

    def teste_004_deletaId(self):
        r_reset = requests.delete('http://localhost:5002/Turma/Resetar')
        self.assertEqual(r_reset.status_code, 200, "Falha ao resetar as turmas")

        # Cria 3 turmas
        requests.post('http://localhost:5002/Turma', json={
            "Id": 25,
            "Descrição": "Eng. Requisitos",
            "Ativa": False,
            "Professor Id": 12
        })
        requests.post('http://localhost:5002/Turma', json={
            "Id": 26,
            "Descrição": "Eng. Software",
            "Ativa": False,
            "Professor Id": 15
        })
        requests.post('http://localhost:5002/Turma', json={
            "Id": 27,
            "Descrição": "Eng. Sistemas",
            "Ativa": False,
            "Professor Id": 12
        })

        # Obtém a lista de turmas
        r_list = requests.get('http://localhost:5002/Turma')
        r_return = r_list.json()
        self.assertEqual(len(r_return), 3, "A lista de turmas deve ter 3 elementos após a criação")

        # Deleta a turma com ID 25
        requests.delete('http://localhost:5002/Turma/Resetar/25')

        # Obtém a lista de turmas novamente
        r_list2 = requests.get('http://localhost:5002/Turma')
        r_return2 = r_list2.json()
        self.assertEqual(len(r_return2), 2, "A lista de turmas deve ter 2 elementos após a deleção")

        # Verifica se as turmas corretas permaneceram
        turmaId26 = False
        turmaId27 = False
        for turma in r_return2:
            if turma['Id'] == 26:
                turmaId26 = True
            if turma['Id'] == 27:
                turmaId27 = True
        if not turmaId26 or not turmaId27:
            self.fail('Você deletou a turma errada')

        # Deleta a turma com ID 27
        requests.delete('http://localhost:5002/Turma/Resetar/27')

        # Obtém a lista de turmas novamente
        r_list3 = requests.get('http://localhost:5002/Turma')
        r_return3 = r_list3.json()
        self.assertEqual(len(r_return3), 1, "A lista de turmas deve ter 1 elemento após a segunda deleção")

        # Verifica se a turma restante é a correta
        if r_return3[0]['Id'] == 26:
            pass
        else:
            self.fail("Você parece ter deletado a turma errada!")

    def teste_005_edita(self):
        r_reset = requests.delete('http://localhost:5002/Turma/Resetar')
        self.assertEqual(r_reset.status_code,200)

        requests.post('http://localhost:5002/Turma', json={
            "Id": 26,
            "Descrição": "Eng. Software",
            "Ativa": False,
            "Professor Id": 15
        })

        r_antes = requests.get('http://localhost:5002/Turma/26')
        self.assertEqual(r_antes.json()['Descrição'],'Eng. Software')

        requests.put('http://localhost:5002/Turma/Alterar/26',json={
            "Id": 26,
            "Descrição": "Eng. Dos esquisitos",
            "Ativa": False,
            "Professor Id": 15})
        
        r_depois = requests.get('http://localhost:5002/Turma/26')

        self.assertEqual(r_depois.json()['Descrição'],'Eng. Dos esquisitos')
        #mas o id nao mudou
        self.assertEqual(r_depois.json()['Id'],26)

    def test_006a_id_inexistente_no_put(self):
        r_reset = requests.delete('http://localhost:5002/Turma/Resetar')
        self.assertEqual(r_reset.status_code,200)
        r = requests.put('http://localhost:5002/Turma/Alterar/11',json={
            "Id": 2222,
            "Descrição": "Eng. Dos esquisitos",
            "Ativa": True,
            "Professor Id": 15
        })
        
        self.assertIn(r.status_code,[400,404])
        # self.assertEqual(r.json()['erro'],'Turma não encontrada')

    def test_006b_id_inexistente_no_get(self):
        r_reset = requests.delete('http://localhost:5002/Turma/Resetar')
        self.assertEqual(r_reset.status_code,200)
        r = requests.get('http://localhost:5002/Turma')
        self.assertIn(r.status_code,[400,404])
        self.assertEqual(r.json()['erro'],'Turma não identificada')




if __name__ == '__main__':
    unittest.main()
if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug=True)





