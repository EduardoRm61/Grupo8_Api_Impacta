import unittest        #import, não fr
from app import app

class Teste_GET_Professor(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get(self):
        response = self.app.get('/professores')
        self.assertEqual(200, response.status_code)

    def test_get_existing_user(self):
        response = self.app.get('/professores/10')  
        data = response.get_json()  
        self.assertEqual(dict, type(data))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["id"], 10)
        self.assertEqual(data["nome"], 'Caio')
        self.assertEqual(data["idade"], 27)
        self.assertEqual(data["materia"], "Dev API E Micros")
        self.assertEqual(data["observacoe"], "Contato com aluno via Chat")
   
        response = self.app.delete('/professsores/10')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["id"], 10)


if __name__ == "__main__":
    unittest.main()