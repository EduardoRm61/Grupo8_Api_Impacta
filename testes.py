import unittest
import requests
from app import app

class TestStringMethods(unittest.TestCase):

    def teste_000_lista_professorGET(self):
        r = requests.get('http://localhost:5002/Turma')

        if r.status_code == 404:
            self.fail("voce nao definiu a pagina /Turma no seu server")
        try:
            obj_return = r.json()
        except:
            self.fail("O Retorndo deve ser em JSON")
        self.assertEqual(type(obj_return),type([]))


if __name__ == '__main__':
    unittest.main()