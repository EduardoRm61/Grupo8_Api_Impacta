import os
from flask import Flask, jsonify, request
from config import app
from professores.route_prof import bp_professor
from routes_turma import Bd_Turma
from route_aluno import bp_aluno


app.register_blueprint(bp_professor)
app.register_blueprint(Bd_Turma)
app.register_blueprint(bp_aluno)


if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
