import os
from flask import Flask, jsonify, request
from config import app                                      # estava apps.config import ...
from professores.route_prof import bp_professor
from turma.routes_turma import Bd_Turma
from alunos.route_aluno import bp_aluno
# adicionar para configurar doxkermysql / flask
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, url_for

app.register_blueprint(bp_professor, url_prefix="/professores" )
app.register_blueprint(Bd_Turma, url_prefix="/Turma")
app.register_blueprint(bp_aluno, url_for="/alunos")

# _________________________________________REDIRECIONAMENTO_____________________________________________________


# @app.route("/")
# def redirecionamento():
#     return redirect(url_for(""))

@app.route("/")
def redirecionamento():
    return redirect(url_for("professores.listar_professores"))
# dá erro, não vem http://127.0.0.1:5002/professores - pesquisar mais depois

# _______ para render -  seria uma pag principal que terá texto e link para professor, aluno, turma (criar a pag)
# from flask import render_template
# @app.route("/")
# def Home():
#   return render_template("index.html")

  
if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
