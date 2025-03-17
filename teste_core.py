import unittest
from app import app

class Teste_GET_Professor(unittest.TestCase):
    
    '''Classe apara analise da rota GET - retorno dos dados da lista'''

    def setUp(self):
        
        '''Cliente = dict que simula um cliente real '''
        
        self.app = app.test_client()
        self.professores_iniciais = {
            "professor": [
                {"id": 10, "nome": "Caio", "idade": 27, "materia": "Dev API E Micros", "obs": "Contato com aluno via Chat"},
                {"id": 11, "nome": "Odair", "idade": 30, "materia": "DevOps", "obs": None}       #cuiado com escrita, acentuação, podem dar erro
            ]
        }
        app.config['PROFESSORES'] = self.professores_iniciais.copy()

    def test_get_all_professores(self):
        
        response = self.app.get('/professores')
        self.assertEqual(response.status_code, 200)
        data = response.get_json() #variável data/ que poderia ser dados, recebe a resposta do retorno/get em json e transforma em .py
        self.assertEqual(data["mensagem"], "Ok")    
        self.assertEqual(data["professor"], self.professores_iniciais["professor"])  #retorno de duas chaves - 1° mensagem ou erro com seus valores - 2° professor com chave professor

    def test_get_existing_professor(self):
        
        '''GET por id específico, "individual" '''
        
        response = self.app.get('/professores/10')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["mensagem"], "Ok")
        self.assertEqual(data["professor"], self.professores_iniciais["professor"][0])  #acessa índice 0 da lista (1° chave)
        #  [self.professores_iniciais["professor"][0]] porque é uma segunda lista
        
    def test_get_nonxistent_professor(self):
        
        '''Vê o erro de Not found professor'''
        
        response = self.app.get("/professores/13")
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertIsNotNone("Not Found - Professor inexistente", data)
        #não havia colocado NotNone - outra falha era retorno do app.py
        
        
    def test_post_professor(self):
        
        '''Testa a rota POST /professores (adicionar novo professor)'''
        
        novo_professor = {
            "id": 12, 
            "nome": "Gustavo",
            "idade": None,
            "materia": "Dev Mob",
            "obs": "Sexta é dia da maldade"
        }
        response = self.app.post('/professores', json=novo_professor)
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data["mensagem"], "Created")     #cuidado em abrir e feichar colchetes estava [mensagem , creted]
        self.assertEqual(data["professor"]["id"], novo_professor["id"])  
        self.assertEqual(data["professor"]["nome"], novo_professor["nome"]) 
        self.assertEqual(data["professor"]["materia"], novo_professor["materia"]) 
        self.assertEqual(data["professor"]["obs"], novo_professor["obs"]) 
        # comparando os dados da variável data [observacao] com o do novo_professor, ! NÃO COLOCA [-1] PORQUE É UM TESTE COM RETORNO DE CADASTRO "DIRETO"
        
    def test_put_professor(self):
        
        '''Testa a rota PUT - atualiza prof (já existente)'''
        
        atualizado = {
            "nome": "Caio Eduardo",
        } #"chamar" apenas o que se quer modificar, o resto ignorar
        response = self.app.put('/professores/10', json=atualizado)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["mensagem"], "Atualizado")
        #modificado
        self.assertEqual(data["professor"]["nome"], "Caio Eduardo") #lembrar de chamar 1° a chave professor do return e depois a chave nome com seu valor
        #inalterado
        self.assertEqual(data["professor"]["id"], 10)  
        self.assertEqual(data["professor"]["idade"], 27)  
        self.assertEqual(data["professor"]["materia"], "Dev API E Micros")
        self.assertEqual(data["professor"]["obs"], "Contato com aluno via Chat")
        
if __name__ == "__main__":
    unittest.main()