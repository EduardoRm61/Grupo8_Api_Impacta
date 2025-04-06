import unittest
import requests
from app_prof import app

class TestStringMethods(unittest.TestCase):

   
    def test_008_getProfessorId(self):
        r = requests.post('http://localhost:5002/professores', json={
            "id": 17,
            "nome": "Caio00",
            "idade": 21,
            "materia": "Banco de Dados",
            "obs": "Contato com aluno via Chat"
        })
        #print(r.json())
        resposta = requests.get('http://localhost:5002/professores/17')
        dict_return = resposta.json()
        self.assertEqual(type(dict_return), dict)
        self.assertIn('id', dict_return['professor'])  # Linha corrigida
        self.assertEqual(dict_return['professor']['id'], 17)  # Linha corrigida

    def test_009_POSTProfessor(self):
        try:
            # Cria um novo professor
            resp = requests.post('http://localhost:5002/professores', json={
                "id": 18,
                "nome": "Caio H.",
                "idade": 27,
                "materia": "Dev API E Micros",
                "obs": "Contato com aluno via Chat"
            })
            
            # Verifica se o POST foi bem-sucedido
            if resp.status_code != 201:
                self.fail(f"Falha ao criar Professor. Status code: {resp.status_code}")
            ##print("POST Response:", resp.json())  # Adicionado para depuração

            # Obtém a lista de professores
            r_list = requests.get('http://localhost:5002/professores')
            #print("GET Response:", r_list.status_code, r_list.json())  # Adicionado para depuração
            if r_list.status_code != 200:  # Corrigido: status code 200 para GET
                self.fail(f"Falha ao obter a lista de Professores. Status code: {r_list.status_code}")

            r_list = r_list.json()  # Converte a resposta para JSON

            # Verifica se o novo professor está na lista
            nv_professor = False
            professores = r_list.get('professores', [])  # Acessa a lista de professores
            for professor in professores:
                if professor['id'] == 18:
                    nv_professor = True
                    break  # Otimização: para o loop quando encontrar o professor
            if not nv_professor:
                self.fail('Professor não encontrado na lista de professores')
        except requests.exceptions.RequestException as e:
            self.fail(f"Erro na requisição: {e}")

    def test_010_PUT_Professor(self):
        try:
            # Resetar a lista de professores
            r_reset = requests.delete('http://localhost:5002/professores/resetar')
            self.assertEqual(r_reset.status_code, 200)

            # Criar um novo professor
            post_response = requests.post('http://localhost:5002/professores', json={
                "id": 34,
                "nome": "Caio",
                "idade": 27,
                "materia": "Dev API E Micros",
                "obs": "Contato com aluno via Chat"
            })
            self.assertEqual(post_response.status_code, 201)  # Verifica se o POST foi bem-sucedido
            #print("POST Response:", post_response.json())  # Depuração

            # Consultar o professor criado
            r_antes = requests.get('http://localhost:5002/professores/34')
            self.assertEqual(r_antes.status_code, 200)  # Verifica se o GET foi bem-sucedido
            #print("GET Response (Antes):", r_antes.json())  # Depuração

            # Verifica se o nome do professor está correto
            professor_antes = r_antes.json().get('professor', {})  # Acessa o dicionário 'professor'
            self.assertEqual(professor_antes['nome'], 'Caio')

            # Atualizar o professor
            put_response = requests.put('http://localhost:5002/professores/34', json={
                "id": 34,
                "nome": "Caiooo",
                "idade": 27,
                "materia": "Dev API E Micros",
                "obs": "Contato com aluno via Chat" 
            })
            self.assertEqual(put_response.status_code, 200)  # Verifica se o PUT foi bem-sucedido
            #print("PUT Response:", put_response.json())  # Depuração

            # Consultar o professor atualizado
            r_depois = requests.get('http://localhost:5002/professores/34')
            self.assertEqual(r_depois.status_code, 200)  # Verifica se o GET foi bem-sucedido
            #print("GET Response (Depois):", r_depois.json())  # Depuração

            # Verifica se o nome e o ID do professor estão corretos
            professor_depois = r_depois.json().get('professor', {})  # Acessa o dicionário 'professor'
            self.assertEqual(professor_depois['nome'], 'Caiooo')
            self.assertEqual(professor_depois['id'], 34)
        except requests.exceptions.RequestException as e:
            self.fail(f"Erro na requisição: {e}")
        
    def test_011_DELETE(self):
        try:
            # Adiciona um professor para garantir que há dados no dicionário
            post_response = requests.post('http://localhost:5002/professores', json={
                "id": 1,
                "nome": "Professor Teste",
                "idade": 40,
                "materia": "Matemática",
                "obs": "Teste de reset"
            })
            self.assertEqual(post_response.status_code, 201)  # Verifica se o POST foi bem-sucedido
            #print("POST Response (Adicionar Professor):", post_response.json())

            # Verifica se o professor foi adicionado
            get_response = requests.get('http://localhost:5002/professores/1')
            self.assertEqual(get_response.status_code, 200)  # Verifica se o GET foi bem-sucedido
            #print("GET Response (Antes do Reset):", get_response.json())

            # Reseta o dicionário de professores
            reset_response = requests.delete('http://localhost:5002/professores/resetar')
            self.assertEqual(reset_response.status_code, 200)  # Verifica se o DELETE foi bem-sucedido
            #print("DELETE Response (Resetar Professores):", reset_response.json())

            # Tenta buscar o professor após o reset
            get_response_after_reset = requests.get('http://localhost:5002/professores/1')
            #print("GET Response (Após o Reset):", get_response_after_reset.json())  # Depuração
            self.assertEqual(get_response_after_reset.status_code, 404)  # Verifica se o professor não existe mais

        except requests.exceptions.RequestException as e:
            self.fail(f"Erro na requisição: {e}")


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()