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

    def teste_001_criar_alunoPOST(self):


    def teste_002_pesquisaId_alunos(self):
        r = requests.post('http://localhost:5002/alunos',json={
            #ver objetos
        })
        
