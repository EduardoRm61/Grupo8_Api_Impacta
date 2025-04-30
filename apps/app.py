
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from swagger.swagger_config import configure_swagger
from flask import Flask, jsonify, request
from config import app
from professores.route_prof import bp_professor
from turma.routes_turma import Bd_Turma
from alunos.route_aluno import bp_aluno


app.register_blueprint(bp_professor, url_prefix='/api')
app.register_blueprint(Bd_Turma, url_prefix='/api')
app.register_blueprint(bp_aluno, url_prefix='/api')

swagger_url ='/docs' #url aonde o swagger estará disponivel
API_URL = '/static/swagger.json' #ccaminho para o arquvio json
configure_swagger(app)


if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
