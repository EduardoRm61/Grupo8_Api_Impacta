import unittest
from app import app

class Teste_GET_Professor(unittest.TestCase):
    '''Classe apara analise da rota GET - retorno dos dados da lista'''

    def setUp(self):
        '''Cliente = dict que simula um cliente real '''
        self.app = app.test_client()
        self.professores_iniciais = {
            "professor": [
                {"id": 10, "nome": "Caio", "idade": 27, "materia": "Dev API E Micros", "observacoe": "Contato com aluno via Chat"},
                {"id": 11, "nome": "Odair", "idade": 30, "materia": "DevOps", "observacoe": None}
            ]
        }
        app.config['PROFESSORES'] = self.professores_iniciais.copy()

    def test_get_all_professores(self):
        
        response = self.app.get('/professores')
        self.assertEqual(response.status_code, 200)
        data = response.get_json() #variável data/ que poderia ser dados, recebe a resposta do retorno/get em json e transforma em .py
        self.assertEqual(data, self.professores_iniciais)

    def test_get_existing_professor(self):
        '''GET por id específico, "individual" '''
        response = self.app.get('/professores/10')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data, self.professores_iniciais["professor"][0])  #acessa índice 0 da lista (1° chave)

if __name__ == "__main__":
    unittest.main()