
import sys

import os
from flask import Flask, jsonify, request
from config import app                                      # estava apps.config import ...
from swagger.swagger_config import configure_swagger

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from swagger.swagger_config import configure_swagger
from flask import Flask, jsonify, request
from config import app
from professores.route_prof import bp_professor
from turma.routes_turma import Bd_Turma
from alunos.route_aluno import bp_aluno
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, url_for

app.register_blueprint(bp_professor)
app.register_blueprint(Bd_Turma)
app.register_blueprint(bp_aluno)
app.register_blueprint(bp_professor, url_prefix='/api')
app.register_blueprint(Bd_Turma, url_prefix='/api')
app.register_blueprint(bp_aluno, url_prefix='/api')


# app.register_blueprint(bp_professor, url_prefix="/professores" )
# app.register_blueprint(Bd_Turma, url_prefix="/Turma")
# app.register_blueprint(bp_aluno, url_for="/alunos")
# para url vir com a rota professor, sem precisar escrever,<status falhou>

# _________________________________________REDIRECIONAMENTO__________________________________________________

# @app.route("/")
# def redirecionamento():
#     return redirect(url_for("professores.listar_professores"))

#rafa, vc tirou este ou vc não o tinha?


swagger_url ='/docs' #url aonde o swagger estará disponivel
API_URL = '/static/swagger.json' #ccaminho para o arquvio json
configure_swagger(app)


if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
