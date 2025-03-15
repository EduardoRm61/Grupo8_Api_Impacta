#Flask Framework, jsonfy "tradução" de py para json, request decesso aos dados 

from flask import Flask, jsonify, request 




app = Flask(__name__)     #estou instanciando esta classe na varável app

dados = {"alunos":[], 
        "professores":[
            {"ide": 10, "nome": "Caio", "idade": 27, "matéria": "Dev API E Micros", "obsercacoes": "Contato com aulo via Chat"},
            {"ide": 11, "nome": "Odair", "idade": 30, "matéria": "- DevOps", "obsercacoes":None }
            ]
        }

@app.route ("/professores", methods = ["POST"])

'''
o que fiz
'''

def 
    
