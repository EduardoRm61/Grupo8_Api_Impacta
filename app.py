import unittest
import requests
from app import app


###TESTE###
class TestStringMethodsI(unittest.TestCase):


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

            #criando outro aluno
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

    def teste_003_deletaId_aluno(self):
        r_reset = requests.delete('http://localhost:5002/alunos/') #ver no código princiapal
        self.assertEqual(r_reset.status_code, 200, "Falha ao resetar o aluno")

        # Cria aluno
        requests.post('http://localhost:5002/alunos', json={
            "Id": 33,
            "Nome": "Victor",
            "Idade": 32,
            "Turma_Id": 80,
            "Data_nascimento": "04/05/1993",
            "Nota_Primeiro_Semestre": 2.0,
            "Nota_Segundo_semestre": 4.0, 
            "Media_final": 3.0
        })


        r_list = requests.get('http://localhost:5002/alunos')
        r_return = r_list.json()
        self.assertEqual(len(r_return), 1, "A lista de aluno deve ter incluido 1 aluno")

        requests.delete('http://localhost:5002/alunos/resetar/33')
        r2_list = requests.get('http://localhost:5002/alunos')
        
      # Verificar se aluno ainda existe
        r2 = requests.get(f"http://127.0.0.1:5000/api/alunos")
        self.assertEqual(r2.status_code, 404, "Erro: Aluno ainda existe após deleção")


    def teste_004_aluno_edita(self):
        r_reset = requests.delete('http://localhost:5002/alunos/resetar/33')
        self.assertEqual(r_reset.status_code,200)

        requests.post('http://localhost:5002/alunos', json={
            "Id": 55,
            "Nome": "Thais",
            "Idade": 18,
            "Turma_Id": 16,
            "Data_nascimento": "10/09/2007",
            "Nota_Primeiro_Semestre": 1.0,
            "Nota_Segundo_semestre": 1.0, 
            "Media_final": 2.0
        })

        r_antes = requests.get('http://localhost:5002/alunos/55')
        self.assertEqual(r_antes.json()['Nota_primeiro_semestre'], 1.0)

        requests.put('http://localhost:5002/Turma/Alterar/55',json={
           "Id": 55,
            "Nome": "Thais",
            "Idade": 18,
            "Turma_Id": 16,
            "Data_nascimento": "10/09/2007",
            "Nota_Primeiro_Semestre": 9.0,
            "Nota_Segundo_semestre": 1.0, 
            "Media_final": 2.0
            })
        
        r_depois = requests.get('http://localhost:5002/alunos/55')

        self.assertEqual(r_depois.json()['Descrição'], 9.0)
        #mas o id nao mudou
        self.assertEqual(r_depois.json()['Id'],55)