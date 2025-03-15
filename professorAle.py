from flask import Flask, jsonify, request         #Flask Framework, jsonfy "tradução" de py para json, request decesso aos dados 

app = Flask(__name__)     #estou instanciando esta classe na varável app

dados = {"alunos":[], 
        "professores":[
            {"ide": 10, "nome": "Caio", "idade": 27, "matéria": "Dev API E Micros", "obsercacoes": "Contato com aulo via Chat"}
            {"ide": 11, "nome": "Odair", "idade": 30, "matéria": "- DevOps", "obsercacoes": }
            
        ]}
class Professor_Not_found(Exception):
    pass


    
    @app.route ("/professores", methods = ["POST"])
    
    def addProfessor():
        adicionarProf = request
    
    @app.route ()
    
    # pelo que me lembre pass é para seguir com o cód sem ter uma ação | se o professor não for encontrado pula cód para fora # # desta classe.
    # addProfessor - função para adicionar professor
