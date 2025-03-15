from flask import Flask, jsonify, request         #Flask Framework, jsonfy "tradução" de py para json, request decesso aos dados 

app = Flask(__name__)     #estou instanciando esta classe na varável app

dados = {"alunos":[], 
        "professores":[
            {"ide": 10, "nome": "Caio", "idade": 27, "matéria": "Dev API E Micros", "obsercacoes": "Contato com aulo via Chat"},
            {"ide": 11, "nome": "Odair", "idade": 30, "matéria": "- DevOps", "obsercacoes":None }
            ]
        }
class Professor_Not_found(Exception):
    pass

    @app.route ("/professores", methods = ["POST"])
    
    def addProfessor():
        
        '''
        Método para adicionar (envio) novos alunos à lista de professores
        
        explicando o cod: 
        
        '''
        
        if not request.is_json:
        return jsonify({"erro": "Bad Request - Formato deve ser me json"}), 400
    
        newProf = request.json
        professores.append(newProf)
        return jsonify ({"mensagem": "Novo professor adicionado"}), 201
    
    @app.route ("/professores", methods = ["GET"])
    
    def buscaProfessor(id):
        newProf = request.json
        
        for professor ["id"] == "id":
            return jsonify (professores)
            
    
    
    # pelo que me lembre pass é para seguir com o cód sem ter uma ação | se o professor não for encontrado pula cód para fora # # desta classe.
    # addProfessor - função para adicionar professor
def addProfessor():
    # Verifica se o request contém JSON
    if not request.is_json:
        return jsonify({"erro": "O conteúdo deve ser enviado em JSON"}), 400
    
    # Tenta acessar o JSON
    try:
        newProf = request.get_json()  # ou request.json
    except Exception as e:
        return jsonify({"erro": "JSON inválido"}), 400
    
    # Verifica se os campos obrigatórios estão presentes
    if not all(key in newProf for key in ["ide", "nome", "idade", "matéria", "observacoes"]):
        return jsonify({"erro": "Campos obrigatórios faltando"}), 400
    
    # Adiciona o novo professor
    dados["professores"].append(newProf)
    return jsonify({"mensagem": "Novo professor adicionado"}), 201