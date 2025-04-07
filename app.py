import os
from flask import flask, jsoify, request
from config import app
from rout_prof import bp_professor

app.register_blueprint(bp_professor)
app.register_blueprint(professor)

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
