
import sys
import os
from flask import Flask, jsonify, request, redirect, url_for
from apps.config import app, db_serv
from apps.swagger.swagger_config import configure_swagger
from apps.professores.route_prof import bp_professor
from apps.turma.routes_turma import Bd_Turma
from apps.alunos.route_aluno import bp_aluno
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from apps.swagger.namespaces import prof_namespace, aluno_namespace, turma_namespace


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# app.register_blueprint(bp_professor)
# app.register_blueprint(Bd_Turma)
# app.register_blueprint(bp_aluno)
# app.register_blueprint(bp_professor, url_prefix='/api')
# app.register_blueprint(Bd_Turma, url_prefix='/api')
# app.register_blueprint(bp_aluno, url_prefix='/api')
app.register_blueprint(bp_professor, url_prefix="/professores")
app.register_blueprint(Bd_Turma, url_prefix="/alunos")
app.register_blueprint(bp_aluno, url_prefix="/turmas")


api = Api(
  app, 
  version= "1.0", 
  title= "Grupo8_Api_Impacta",  
  description= "Aplicativo de gerenciamênto de dados de turmas, professor e alunos da faculdade Impacta", 
  doc = "/docs"  
)
with app.app_context(): 
  db_serv.create_all() 

# swagger_url ='/docs' 
# API_URL = '/static/swagger.json' 
# configure_swagger(app)

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
