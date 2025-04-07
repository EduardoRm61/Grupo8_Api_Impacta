from flask import Flask, jsonify, request
from config_prof import app
from route_prof import bp_professor
from rout_alu import blueprint_aluno
from rout_turma import blueprint_turma
import app 

app.register_blueprint(bp_professor)
app.register_blueprint(blueprint_aluno)
app.register_blueprint(blueprint_turma)

if _name_ == "_main_":
    app.run(host = app.config["HOST"], port = app.config["PORT"], debug = app.config["DEBUG"])