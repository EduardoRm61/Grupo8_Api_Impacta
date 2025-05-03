import os   
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["HOST"] = "0.0.0.0"  # 127.0.0.1 - apenas host local, mudei para 0.0.0.0 para remoto poder acessar
app.config["PORT"]= 5002
app.config["DEBUG"] = True

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False

db_serv = SQLAlchemy(app)