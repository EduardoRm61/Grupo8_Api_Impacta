import unittest
import requests
from app import app


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

        ''' def test_001_adiciona_alunos(self):
        r = requests.post('http://localhost:5002/alunos', json={'nome': 'fernando', 'id': 1})
        r = requests.post('http://localhost:5002/alunos', json={'nome': 'roberto', 'id': 2})
        r_lista = requests.get('http://localhost:5002/alunos')
        lista_retornada = r_lista.json()
        achei_fernando = False
        achei_roberto = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'fernando':
                achei_fernando = True
            if aluno['nome'] == 'roberto':
                achei_roberto = True
        if not achei_fernando:
            self.fail('aluno fernando nao apareceu na lista de alunos')
        if not achei_roberto:
            self.fail('aluno roberto nao apareceu na lista de alunos')

    def test_002_aluno_por_id(self):
        r = requests.post('http://localhost:5002/alunos', json={'nome': 'mario', 'id': 20})
        resposta = requests.get('http://localhost:5002/alunos/20')
        dict_retornado = resposta.json()
        self.assertEqual(type(dict_retornado), dict)
        self.assertIn('nome', dict_retornado)
        self.assertEqual(dict_retornado['nome'], 'mario')

    def test_003_reseta(self):
        r = requests.post('http://localhost:5002/alunos', json={'nome': 'cicero', 'id': 29})
        r_lista = requests.get('http://localhost:5002/alunos')
        self.assertTrue(len(r_lista.json()) > 0)
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code, 200)
        r_lista_depois = requests.get('http://localhost:5002/alunos')
        self.assertEqual(len(r_lista_depois.json()), 0)
    def test_004_deleta(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code, 200)
        requests.post('http://localhost:5002/alunos', json={'nome': 'cicero', 'id': 29})
        requests.post('http://localhost:5002/alunos', json={'nome': 'lucas', 'id': 28})
        requests.post('http://localhost:5002/alunos', json={'nome': 'marta', 'id': 27})
        r_lista = requests.get('http://localhost:5002/alunos')
        lista_retornada = r_lista.json()
        self.assertEqual(len(lista_retornada), 3)
        requests.delete('http://localhost:5002/alunos/28')
        r_lista2 = requests.get('http://localhost:5002/alunos')
        lista_retornada2 = r_lista2.json()
        self.assertEqual(len(lista_retornada2), 2)
        acheiMarta = False
        acheiCicero = False
        for aluno in lista_retornada:
            if aluno['nome'] == 'marta':
                acheiMarta = True
            if aluno['nome'] == 'cicero':
                acheiCicero = True
        if not acheiMarta or not acheiCicero:
            self.fail("voce parece ter deletado o aluno errado!")
        requests.delete('http://localhost:5002/alunos/27')
        r_lista3 = requests.get('http://localhost:5002/alunos')
        lista_retornada3 = r_lista3.json()
        self.assertEqual(len(lista_retornada3), 1)
        if lista_retornada3[0]['nome'] == 'cicero':
            pass
        else:
            self.fail("voce parece ter deletado o aluno errado!")

    def test_005_edita(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code, 200)
        requests.post('http://localhost:5002/alunos', json={'nome': 'lucas', 'id': 28})
        r_antes = requests.get('http://localhost:5002/alunos/28')
        self.assertEqual(r_antes.json()['nome'], 'lucas')
        requests.put('http://localhost:5002/alunos/28', json={'nome': 'lucas mendes'})
        r_depois = requests.get('http://localhost:5002/alunos/28')
        self.assertEqual(r_depois.json()['nome'], 'lucas mendes')
        self.assertEqual(r_depois.json()['id'], 28)

    def test_006a_id_inexistente_no_put(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code, 200)
        r = requests.put('http://localhost:5002/alunos/15', json={'nome': 'bowser', 'id': 15})
        self.assertIn(r.status_code, [400, 404])
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')

    def test_006b_id_inexistente_no_get(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code, 200)
        r = requests.get('http://localhost:5002/alunos/15')
        self.assertIn(r.status_code, [400, 404])
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')

    def test_006c_id_inexistente_no_delete(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code, 200)
        r = requests.delete('http://localhost:5002/alunos/15')
        self.assertIn(r.status_code, [400, 404])
        self.assertEqual(r.json()['erro'], 'aluno nao encontrado')

    def test_007_criar_com_id_ja_existente(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code, 200)
        r = requests.post('http://localhost:5002/alunos', json={'nome': 'bond', 'id': 7})
        self.assertEqual(r.status_code, 200)
        r = requests.post('http://localhost:5002/alunos', json={'nome': 'james', 'id': 7})
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'id ja utilizada')

    def test_008a_post_sem_nome(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code, 200)
        r = requests.post('http://localhost:5002/alunos', json={'id': 8})
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'aluno sem nome')

    def test_008b_put_sem_nome(self):
        r_reset = requests.post('http://localhost:5002/reseta')
        self.assertEqual(r_reset.status_code, 200)
        r = requests.post('http://localhost:5002/alunos', json={'nome': 'maximus', 'id': 7})
        self.assertEqual(r.status_code, 200)
        r = requests.put('http://localhost:5002/alunos/7', json={'id': 7})
        self.assertEqual(r.status_code, 400)
        self.assertEqual(r.json()['erro'], 'aluno sem nome')'''


if __name__ == '__main__':
    runTests()



