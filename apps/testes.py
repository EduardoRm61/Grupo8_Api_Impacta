import unittest
import requests
from apps.app import app

class TestStringMethods(unittest.TestCase):

    #Teste para listar Turma: 
    def test_000_lista_professorGET(self):
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
 

    def test_005_edita(self):
        r_reset = requests.delete('http://localhost:5002/Turma/Resetar')
        self.assertEqual(r_reset.status_code,200)

        #{"Id": 12, "Descrição": "Eng. Software","Ativa": True,"Professor Id": 10}

        resp = requests.post('http://localhost:5002/Turma', json={
            "Id": 26,
            "Descrição": "Eng. Software",
            "Ativa": False,
            "Professor Id": 11
        })

        #print(r_reset.json())      
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

## ----------------------------------------- PROF GET ----------------------------------------------------#

    def test_007_getProfessor(self):
        r = requests.get('http://localhost:5002/professores')
        if r.status_code == 404:
            self.fail("voce nao definiu a pagina /professores no seu server")
        try:
            obj_return = r.json()
        except:
            self.fail("O Retorndo deve ser em JSON")
            self.assertEqual(type(obj_return),type([]))

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

## ----------------------------------------- PROF POST ----------------------------------------------------#

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

#-------------------------- TESTES ALUNO ----------------------------------

    def test_012_GET_alunos(self):
        r = requests.get('http://localhost:5002/alunos')
        if r.status_code == 404:
            self.fail("Você não definiu a página/alunos no seu servidor")
        try:
            obj_retornado = r.json()
        except:
            self.fail("O retorno deve ser em JSON")
        self.assertEqual(type(obj_retornado), type([]))

    def test_013_POST_POST(self):
        try:
            #criando um aluno
            r1 = requests.post('http://localhost:5002/alunos', json={
                "Id": 29,
                "Nome": "Alessandra",
                "Idade": 20,
                "Turma_Id": 13,
                "Data_nascimento": "01/10/2010",
                "Nota_Primeiro_Semestre": 10.0,
                "Nota_Segundo_semestre": 10.0,
                "Media_final": 10.0
            })

            if r1.status_code != 201:
                self.fail(f"Falha ao criar aluno 01: {r1.status_code}")

            #criando outro aluno
            r2 = requests.post('http://localhost:5002/alunos', json={
                "Id": 27,
                "Nome": "Eduardo",
                "Idade": 20,
                "Turma_Id": 14,
                "Data_nascimento": "05/05/2005",
                "Nota_Primeiro_Semestre": 6.0,
                "Nota_Segundo_semestre": 7.0,
                "Media_final": 6.5
            })

            
            if r2.status_code != 201:
                self.fail(f"Falha ao criar aluno 01: {r2.status_code}")

            #obtém a lista de alunos
            r_list = requests.get('http://localhost:5002/alunos')
            if r_list.status_code != 200:
                self.fail(f"Falha ao obter a lista de alunos. Status code: {r_list.status_code}")
 
            r_list_return = r_list.json()

            aluno01_encontrado = False
            aluno02_encontrado = False

            for aluno in r_list_return:
                if aluno['Id'] == 29:
                    aluno01_encontrado = True
                if aluno['Id'] == 27:
                    aluno02_encontrado = True

            if not aluno01_encontrado:
                self.fail('Aluno 01 não encontrada na lista de alunos')
            if not aluno02_encontrado:
                self.fail('Aluno 02 não encontrada na lista de alunos')

        except requests.exceptions.RequestException as e:
            self.fail(f"Erro ao fazer requisição: {e}")

        
    def test_014_POST_aluno(self):
        r = requests.post('http://localhost:5002/alunos',json={
            "Id": 20,
            "Nome": "Thaina",
            "Idade": 28,
            "Turma_Id": 12,
            "Data_nascimento": "10/08/2005",
            "Nota_Primeiro_Semestre": 8.0,
            "Nota_Segundo_semestre": 9.0,
            "Media_final": 8.5
        })
        resposta = requests.get('http://localhost:5002/alunos/20')
        dict_return = resposta.json()
        self.assertEqual(type(dict_return),dict)
        self.assertIn('Id',dict_return)
        self.assertEqual(dict_return['Id'],20)


    def test_015_DELETE_aluno(self):
        # Resetar a lista de alunos
        r_reset = requests.delete('http://localhost:5002/alunos/resetar')
        self.assertEqual(r_reset.status_code, 200, "Falha ao resetar o aluno")

        # Criar aluno
        try:
            r_create = requests.post('http://localhost:5002/alunos', json={
                "Id": 33,
                "Nome": "Victor",
                "Idade": 32,
                "Turma_Id": 80,
                "Data_nascimento": "04/05/1993",
                "Nota_Primeiro_Semestre": 2.0,
                "Nota_Segundo_semestre": 4.0, 
                "Media_final": 3.0
            })
            self.assertEqual(r_create.status_code, 201, "Falha ao criar o aluno")
        except requests.exceptions.RequestException as e:
            self.fail(f"Erro ao criar aluno: {e}")

        # Verificar se o aluno foi adicionado
        r_list = requests.get('http://localhost:5002/alunos')
        r_return = r_list.json()
        self.assertEqual(len(r_return), 1, "A lista de alunos deve ter incluído 1 aluno")

        # Deletar o aluno
        requests.delete('http://localhost:5002/alunos/deletar/33')

        # Verificar se o aluno foi deletado
        r2_list = requests.get('http://localhost:5002/alunos')
        r2_return = r2_list.json()
        aluno_33 = [aluno for aluno in r2_return if aluno["Id"] == 33]
        self.assertEqual(len(aluno_33), 0, "Erro: Aluno ainda existe após deleção")


    def test_016_aluno_EDITA(self):
        # Deleta o aluno com ID 55, caso exista
        r_reset = requests.delete('http://localhost:5002/alunos/resetar')
        #self.assertIn(r_reset.status_code, [200, 404], "Falha ao resetar o aluno") # Tanto faz a resposta ERRADO
       
        r_post = requests.post('http://localhost:5002/alunos', json={
            "Id": 55,
            "Nome": "Thais",
            "Idade": 18,
            "Turma_Id": 16,
            "Data_nascimento": "10/09/2007",
            "Nota_Primeiro_Semestre": 1.0,
            "Nota_Segundo_semestre": 1.0,
            "Media_final": 2.0
        })
        #print(r_post.status_code)
        self.assertEqual(r_post.status_code, 201, "Criado com sucesso") # ou 404

        # Verifica os dados do aluno anteatus_cs da edição
        r_antes = requests.get('http://localhost:5002/alunos/55')
        self.assertEqual(r_antes.status_code, 200, "Falha ao obter o aluno antes da edição")
        self.assertEqual(r_antes.json()['Nota_Primeiro_Semestre'], 1.0, "Nota antes da edição incorreta")

        # Edita o aluno
        r_put = requests.put('http://localhost:5002/alunos/55', json={
            "Nome": "Thais",
            "Idade": 18,
            "Turma_Id": 16,
            "Data_nascimento": "10/09/2007",
            "Nota_Primeiro_Semestre": 9.0,
            "Nota_Segundo_semestre": 1.0,
            "Media_final": 2.0
        })
        self.assertEqual(r_put.status_code, 200, "Falha ao editar o aluno")

        # Verifica os dados do aluno após a edição
        r_depois = requests.get('http://localhost:5002/alunos/55')
        self.assertEqual(r_depois.status_code, 200, "Falha ao obter o aluno após a edição")
        self.assertEqual(r_depois.json()['Nota_Primeiro_Semestre'], 9.0, "Nota após a edição incorreta")
        self.assertEqual(r_depois.json()['Id'], 55, "O ID do aluno foi alterado incorretamente")


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()