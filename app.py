# inicia a aplicação
# entrada principal para app, entrada do flask
#render sobe aplicação por este arquivo
#não possui rotas
#recebe as configurações do arquivo (entendi que é do config)
# registro dos bluprints

import os
from flask import Flask, jsonify, request
from config_prof import app
from route_prof import bp_professor
from index_professor import profes

app.register_blueprint(bp_professor)
app.register_blueprint(profes)
# app.register_blueprint(#nome blueprint professor)
# # estou importando as blueprints para app
# #app.register_blueprint(professor)

if __name__ == "__main__":
    app.run(host = app.config["HOST"], port = app.config["PORT"], debug = app.config["DEBUG"])

