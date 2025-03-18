import unittest
from app import app  # Importa o aplicativo Flask do arquivo app.py

class TestBase(unittest.TestCase):
    def setUp(self):
        '''Configura o ambiente de teste'''
        self.app = app.test_client()
        self.professores_iniciais = {
            "professor": [
                {"id": 10, "nome": "Caio", "idade": 27, "materia": "Dev API E Micros", "obs": "Contato com aluno via Chat"},
                {"id": 11, "nome": "Odair", "idade": 30, "materia": "DevOps", "obs": None}
            ]
        }
        app.config['PROFESSORES'] = self.professores_iniciais.copy()

    def tearDown(self):
        '''Restaura o ambiente de teste para o estado inicial'''
        app.config['PROFESSORES'] = self.professores_iniciais.copy()

class Teste_GET_Professor(TestBase):
    def test_get_all_professores(self):
        '''Testa a rota GET /professores (listar todos os professores)'''
        response = self.app.get('/professores')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["mensagem"], "Ok")
        self.assertEqual(data["professor"], self.professores_iniciais["professor"])

    def test_get_existing_professor(self):
        '''Testa a rota GET /professores/<id> (buscar um professor existente)'''
        response = self.app.get('/professores/10')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["mensagem"], "Ok")
        self.assertEqual(data["professor"], self.professores_iniciais["professor"][0])

    def test_get_nonxistent_professor(self):
        '''Testa a rota GET /professores/<id> (buscar um professor inexistente)'''
        response = self.app.get("/professores/13")
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data["error"], "Not Found - Professor inexistente")

class Teste_POST_Professor(TestBase):
    def test_post_professor(self):
        '''Testa a rota POST /professores (adicionar novo professor)'''
        novo_professor = {
            "nome": "Gustavo",
            "idade": None,
            "materia": "Dev Mob",
            "obs": "Sexta é dia da maldade"
        }
        response = self.app.post('/professores', json=novo_professor)
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["mensagem"], "Created")
        self.assertEqual(data["professor"]["id"], 12)  # ID esperado é 12
        self.assertEqual(data["professor"]["nome"], novo_professor["nome"])
        self.assertEqual(data["professor"]["materia"], novo_professor["materia"])
        self.assertEqual(data["professor"]["obs"], novo_professor["obs"])

class Teste_PUT_Professor(TestBase):
    def test_put_professor(self):
        '''Testa a rota PUT /professores/<id> (atualizar um professor existente)'''
        atualizado = {
            "nome": "Caio Eduardo",
        }
        response = self.app.put('/professores/10', json=atualizado)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["mensagem"], "Atualizado")
        self.assertEqual(data["professor"]["nome"], "Caio Eduardo")
        self.assertEqual(data["professor"]["id"], 10)
        self.assertEqual(data["professor"]["idade"], 27)
        self.assertEqual(data["professor"]["materia"], "Dev API E Micros")
        self.assertEqual(data["professor"]["obs"], "Contato com aluno via Chat")

class Teste_DELETE_Professor(TestBase):
    def test_delete_professor_11(self):
        '''Testa a rota DELETE /professores/<id> (deletar um professor existente)'''
        # Verifica se o professor com id=11 existe antes de deletar
        response = self.app.get('/professores/11')
        self.assertEqual(response.status_code, 200)

        # Deleta o professor com id=11
        response = self.app.delete('/professores/11')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["mensagem"], "Deletado")
        self.assertEqual(data["professor"]["id"], 11)

        # Verifica se o professor com id=11 foi deletado
        response = self.app.get('/professores/11')
        self.assertEqual(response.status_code, 404)

        # Verifica se os outros professores ainda existem
        response = self.app.get('/professores/10')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()