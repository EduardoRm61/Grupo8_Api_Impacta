import os
from flask import Flask, jsonify, request
from config import app
from route_prof import bp_professor

app.register_blueprint(bp_professor)

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
