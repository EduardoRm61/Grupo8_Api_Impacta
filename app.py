import sys 
import os  
from flask import Flask, jsonify, request, redirect, url_for 
from apps.swagger.swagger_config import configure_swagger #
from apps.config import app, db_serv                                     
from apps.professores.route_prof import bp_professor
from apps.turma.routes_turma import Bd_Turma 
from apps.alunos.route_aluno import bp_aluno             
from flask_restx import Api


sys.path.append(os.path.dirname(os.path.abspath(__file__))) # já tinha - não tinha no meu teste

from flask_sqlalchemy import SQLAlchemy # já tinha - não tinha no meu teste


app.register_blueprint(bp_professor)
app.register_blueprint(Bd_Turma)
app.register_blueprint(bp_aluno)

# VER QUAL FICA
# app.register_blueprint(bp_professor, url_prefix='/api') # já tinha - não tinha no meu teste 
# app.register_blueprint(Bd_Turma, url_prefix='/api') # já tinha - não tinha no meu teste
# app.register_blueprint(bp_aluno, url_prefix='/api') # já tinha - não tinha no meu teste

# @app.route("/")
# def redirecionamento():
#     return redirect(url_for("professores.listar_professores"))

#rafa, vc tirou este ou vc não o tinha?

api = Api(
  app, 
  version= "1.0", 
  title= "Grupo8_Api_Impacta",  
  description= "Aplicativo de gerenciamênto de dados de turmas, professor e alunos da faculdade Impacta", 
  doc = "/docs"  
)
with app.app_context(): 
    db_serv.create_all() 

swagger_url ='/docs' #url aonde o swagger estará disponivel
API_URL = '/static/swagger.json' #ccaminho para o arquvio json
configure_swagger(app)


if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
