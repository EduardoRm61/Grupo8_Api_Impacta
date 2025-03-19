import unittest
import requests
from app import app

class TestStringMethods(unittest.TestCase):

    #Teste para listar Turma: 
    def teste_000_lista_professorGET(self):
        r = requests.get('http://localhost:5002/Turma')

        if r.status_code == 404:
            self.fail("voce nao definiu a pagina /Turma no seu server")
        try:
            obj_return = r.json()
        except:
            self.fail("O Retorndo deve ser em JSON")
        self.assertEqual(type(obj_return),type([]))

        #Teste para criar nova turma:
    def test_001_criar_turmaPOST(self):
        try:
            # Cria a primeira turma
            r1 = requests.post('http://localhost:5002/Turma', json={
                "Id": 22,
                "Descrição": "Eng. Requisitos",
                "Ativa": False,
                "Professor Id": 10})
            
            if r1.status_code != 201: 
                self.fail(f"Falha ao criar a turma 01. Status code: {r1.status_code}")

            # Cria a segunda turma
            r2 = requests.post('http://localhost:5002/Turma', json={
                "Id": 13,
                "Descrição": "Eng. Sistemas",
                "Ativa": True,
                "Professor Id": 11})
            
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
            "Id": 27,
            "Descrição": "Banco de Dados",
            "Ativa": False,
            "Professor Id": 10 })
        

        resposta = requests.get('http://localhost:5002/Turma/27')
        dict_return = resposta.json()
        self.assertEqual(type(dict_return),dict)
        self.assertIn('Id',dict_return)
        self.assertEqual(dict_return['Id'],27)

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

    def test_004_criar_turmaPOST(self):
        try:
            # Cria a primeira turma
            r1 = requests.post('http://localhost:5002/Turma', json={
                "Id": 52,
                "Descrição": "Eng. Requisitos",
                "Ativa": False,
                "Professor Id": 10})
            #print(r1.json())
            if r1.status_code != 201:  # 201 significa "Created"
                self.fail(f"Falha ao criar a turma 01. Status code: {r1.status_code}")

            # Cria a segunda turma
            r2 = requests.post('http://localhost:5002/Turma', json={
                "Id": 53,
                "Descrição": "Eng. Sistemas",
                "Ativa": True,
                "Professor Id": 11})
            
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
                if turma['Id'] == 52:
                    turma01_encontrada = True
                if turma['Id'] == 53:
                    turma02_encontrada = True

            if not turma01_encontrada:
                self.fail('Turma 01 não encontrada na lista de turmas')
            if not turma02_encontrada:
                self.fail('Turma 02 não encontrada na lista de turmas')

        except requests.exceptions.RequestException as e:
            self.fail(f"Erro ao fazer requisição: {e}")
 

    def teste_005_edita(self):
        r_reset = requests.delete('http://localhost:5002/Turma/Resetar')
        self.assertEqual(r_reset.status_code,200)

        #{"Id": 12, "Descrição": "Eng. Software","Ativa": True,"Professor Id": 10}

        requests.post('http://localhost:5002/Turma', json={
            "Id": 26,
            "Descrição": "Eng. Software",
            "Ativa": False,
            "Professor Id": 11
        })

        #print(r_reset.json())      Aqui está resetado
        #print("POST Response:", resp.status_code, resp.json())
        r_antes = requests.get('http://localhost:5002/Turma/26')
        #print(r_antes.json())
        self.assertEqual(r_antes.json()['Descrição'],'Eng. Software')

        
        requests.put('http://localhost:5002/Turma/Alterar/26',json={
            "Id": 26,
            "Descrição": "Eng. Dos esquisitos",
            "Ativa": False,
            "Professor Id": 11})
        
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

        #print(r.json()) #
        self.assertEqual(r.json()['Erro'], 'Requisição inválida')

    def test_006b_id_inexistente_no_get(self):
        r_reset = requests.delete('http://localhost:5002/Turma/Resetar')
        self.assertEqual(r_reset.status_code,200)
        r = requests.get('http://localhost:5002/Turma/12')
        self.assertIn(r.status_code,[400,404,402])
        # print(r.json())
        self.assertEqual(r.json()['Erro:'],'Erro, Turma não identificada ou inexistente!')
   
if __name__ == '__main__':
    unittest.main()