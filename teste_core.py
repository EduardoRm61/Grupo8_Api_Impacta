import unittest
from app import app

# Comentário: Importa as bibliotecas necessárias.

class TestBase(unittest.TestCase):
    # Comentário: Classe base para os testes, com configurações iniciais e finais.
    def setUp(self):
        '''Configura o ambiente de teste'''
        self.app = app.test_client()
        self.professores_iniciais = {
            "professor": [
                {"id": 10, "nome": "Caio", "idade": 27, "materia": "Dev API E Micros", "obs": "Contato com aluno via Chat"},
                {"id": 11, "nome": "Odair", "idade": 30, "materia": "DevOps", "obs": None}
            ]
        }
        global professores # Correção: Acessar a variável global corretamente
        professores = self.professores_iniciais.copy() # Correção: Inicializar a variável global no teste
        # Comentário: Define os professores iniciais para cada teste.

    def tearDown(self):
        '''Restaura o ambiente de teste para o estado inicial'''
        global professores # Correção: Acessar a variável global corretamente
        professores = self.professores_iniciais.copy() # Comentário: Restaura os professores iniciais após cada teste.

class Teste_GET_Professor(TestBase):
    # Comentário: Classe para testar as rotas GET de professores.
    def test_get_all_professores(self):
        '''Listar todos os professores'''
        response = self.app.get('/professores')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["mensagem"], "Ok")
        self.assertEqual(data["professores"], self.professores_iniciais["professor"]) # Correção: Verificar a chave correta
        # Comentário: Testa se a rota GET para /professores retorna todos os professores corretamente.

    def test_get_existing_professor(self):
        '''Buscar um professor existente'''
        response = self.app.get('/professores/10')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["mensagem"], "Ok")
        self.assertEqual(data["professor"], self.professores_iniciais["professor"][0])
        # Comentário: Testa se a rota GET para /professores/<id> retorna um professor existente corretamente.

    def test_get_nonxistent_professor(self):
        '''Mensagem de professor inexistente'''
        response = self.app.get("/professores/18")
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data["erro"], "Not Found - Professor inexistente") # Correção: Verificar a chave correta
        # Comentário: Testa se a rota GET para /professores/<id> retorna erro para um professor inexistente.

class Teste_POST_Professor(TestBase):
    # Comentário: Classe para testar a rota POST de professores.
    def test_post_professor(self):
        '''Adicionar novo professor'''
        novo_professor = {
            "nome": "Gustavo",
            "idade": None,         #no postmain deve trocar para null para não dar erro
            "materia": "Dev Mob",
            "obs": "Sexta é dia da maldade"
        }
        response = self.app.post('/professores', json=novo_professor)
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["mensagem"], "Created")
        self.assertEqual(data["professor"]["id"], 12)   # ID esperado é 12
        self.assertEqual(data["professor"]["nome"], novo_professor["nome"])
        self.assertEqual(data["professor"]["materia"], novo_professor["materia"])
        self.assertEqual(data["professor"]["obs"], novo_professor["obs"])
        # Comentário: Testa se a rota POST para /professores adiciona um novo professor corretamente.

    def teste_falha_post_professor(self):
        # Comentário: Testa se a rota POST para /professores retorna erro para dados inválidos.
        '''Análise de requisitos obrigatórios'''
        novo_professor = {
            "nome": "Gustavo",
            "idade": None,         #no postmain deve trocar para null para não dar erro
            "materia": None,
            "obs": "Sexta é dia da maldade"
        }
        response = self.app.post("/professores", json = novo_professor)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data["erro"], "Nome e matéria são obrigatórios") # Correção: A mensagem de erro esperada no teste estava diferente

class Teste_PUT_Professor(TestBase):
    # Comentário: Classe para testar a rota PUT de professores.
    def test_put_professor(self):
        '''Atualizar um professor existente'''
        atualizado = {
            "nome": "Caio Eduardo",
        }       #só por referência a ser atualizada
        response = self.app.put('/professores/10', json=atualizado)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        '''Atualizado'''
        self.assertEqual(data["professor"]["nome"], "Caio Eduardo")
        '''Mantido'''
        self.assertEqual(data["professor"]["id"], 10)
        self.assertEqual(data["professor"]["idade"], 27)
        self.assertEqual(data["professor"]["materia"], "Dev API E Micros")
        self.assertEqual(data["professor"]["obs"], "Contato com aluno via Chat")
        # Comentário: Testa se a rota PUT para /professores/<id> atualiza um professor existente corretamente.

class Teste_DELETE_Professor(TestBase):
    # Comentário: Classe para testar a rota DELETE de professores.
    def test_delete_professor(self):
        '''Deletar um professor existente)'''
        # Verifica se o professor com id=11 existe antes de deletar
        response = self.app.delete('/professores/11') #havia posto get
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["mensagem"], "Professor deletado com sucesso") # Correção: A string comparada estava com um ponto extra
        # Comentário: Testa se a rota DELETE para /professores/<id> deleta um professor existente corretamente.

    def Teste_delete_professor_inexistente(self):
        response = self.app.delete('/professores/19')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data["erro"], "Not Found - Professor inexistente") # Correção: A mensagem de erro esperada no teste estava diferente
        # Comentário: Testa se a rota DELETE para /professores/<id> retorna erro para um professor inexistente.

        # # Verifica se o professor com id=11 foi deletado
        # response = self.app.get('/professores/11')
        # self.assertEqual(response.status_code, 404)

        # # Verifica se os outros professores ainda existem
        # response = self.app.get('/professores/10')
        # self.assertEqual(response.status_code, 200)
        # data = response.get_json()
        # self.assertNotIn(11, [p["id"] for p in data["professor"]])


if __name__ == "__main__":
    unittest.main()
    # Comentário: Executa os testes quando o script é rodado diretamente.