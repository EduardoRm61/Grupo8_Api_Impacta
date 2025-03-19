import unittest
import requests
from app import app


###TESTE###
class TestAlunoAPI(unittest.TestCase):


    def teste_000_alunos_retorna_lista(self):
        r = requests.get('http://localhost:5002/alunos')
        if r.status_code == 404:
            self.fail("Você não definiu a página/alunos no seu servidor")
        try:
            obj_retornado = r.json()
        except:
            self.fail("O retorno deve ser em JSON")
        self.assertEqual(type(obj_retornado), type([]))

        ##

    def teste_001_criar_alunoPOST(self):
        try:
            #criando um aluno
            r1 = requests.post('http://localhost:5002/alunos', json={
                "Id": 29,
                "Nome": "Alessandra",
                "Idade": 20,
                "Turma_Id": 13,
                "Data_nascimento": "01/10/2010",
                "Nota_Primeiro_Semestre": 10.0,
                "Nota_Segundo_semestre": 10.0,
                "Media_final": 10.0
            })

            if r1.status_code != 201:
                self.fail(f"Falha ao criar aluno 01: {r1.status_code}")

            r2 = requests.post('http://localhost:5002/alunos', json={
                "Id": 27,
                "Nome": "Eduardo",
                "Idade": 20,
                "Turma_Id": 14,
                "Data_nascimento": "05/05/2005",
                "Nota_Primeiro_Semestre": 6.0,
                "Nota_Segundo_semestre": 7.0,
                "Media_final": 6.5
            })

            
            if r2.status_code != 201:
                self.fail(f"Falha ao criar aluno 01: {r2.status_code}")

            #obtém a lista de alunos
            r_list = requests.get('http://localhost:5002/alunos')
            if r_list.status_code != 200:
                self.fail(f"Falha ao obter a lista de alunos. Status code: {r_list.status_code}")
 
            r_list_return = r_list.json()

            aluno01_encontrado = False
            aluno02_encontrado = False

            for aluno in r_list_return:
                if aluno['Id'] == 29:
                    aluno01_encontrado = True
                if aluno['Id'] == 27:
                    aluno02_encontrado = True

            if not aluno01_encontrado:
                self.fail('Aluno 01 não encontrada na lista de alunos')
            if not aluno02_encontrado:
                self.fail('Aluno 02 não encontrada na lista de alunos')

        except requests.exceptions.RequestException as e:
            self.fail(f"Erro ao fazer requisição: {e}")


        ##

    def teste_002_pesquisaId_alunos(self):
        r = requests.post('http://localhost:5002/alunos',json={
            "Id": 20,
            "Nome": "Thaina",
            "Idade": 28,
            "Turma_Id": 12,
            "Data_nascimento": "10/08/2005",
            "Nota_Primeiro_Semestre": 8.0,
            "Nota_Segundo_semestre": 9.0,
            "Media_final": 8.5
        })
        resposta = requests.get('http://localhost:5002/alunos/20')
        dict_return = resposta.json()
        self.assertEqual(type(dict_return),dict)
        self.assertIn('Id',dict_return)
        self.assertEqual(dict_return['Id'],20)


        ##

        

        
