import unittest
import requests


class TestStringMethods(unittest.TestCase):

    def test_000_alunos_retorna_lista(self):
        r = requests.get('http://localhost:5002/alunos')
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina /alunos no seu server")
        try:
            obj_retornado = r.json()
        except:
            self.fail("queria um json mas voce retornou outra coisa")
        self.assertEqual(type(obj_retornado),type([]))

if __name__ == '__main__':
    runTests()



