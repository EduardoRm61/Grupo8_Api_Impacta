import sys
import os
#import pytest
from flask import Flask, jsonify, request, redirect, url_for
from apps.config import app, db_serv
from apps.swagger.swagger_config import configure_swagger
from apps.professores.route_prof import bp_professor
from apps.turma.routes_turma import Bd_Turma
from apps.alunos.route_aluno import bp_aluno
from flask_sqlalchemy import SQLAlchemy
from apps.swagger.namespaces import prof_namespace, aluno_namespace, turma_namespace
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
app.register_blueprint(bp_professor, url_prefix="/professores")
app.register_blueprint(Bd_Turma, url_prefix="/alunos")
<<<<<<< HEAD
app.register_blueprint(bp_aluno, url_prefix="/turmas")
<<<<<<< HEAD
api = Api(
  app, 
  version= "1.0", 
  title= "Grupo8_Api_Impacta",  
  description= "Aplicativo de gerenciamênto de dados de turmas, professor e alunos da faculdade Impacta", 
  doc = "/docs"  
)
=======
=======
app.register_blueprint(bp_aluno, url_prefix="/Turmas")
>>>>>>> 822735b0d6da287de69bb19d7f56b42a1fe26e1f


configure_swagger(app)

>>>>>>> fa5cbe1bff6b14a46e3172cb50834cfb30ab22af
with app.app_context(): 
  db_serv.create_all() 

# swagger_url ='/docs' 
# API_URL = '/static/swagger.json' 


if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
