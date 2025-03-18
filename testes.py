import unittest
import requests
from app import app

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
        self.assertTrue(len(r_list()) > 0)
        r_reset = requests.post('http://localhost:5002/Turma/Resetar')
        





























if __name__ == '__main__':
    unittest.main()