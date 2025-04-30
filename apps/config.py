import os   #porque impostar os se não estou usando?
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["HOST"] = "0.0.0.0"  # 127.0.0.1 - apenas host local, mudei para 0.0.0.0 para remoto poder acessar
app.config["PORT"]= 5002
app.config["DEBUG"] = True

#_______________________________ mysql _______________________________

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False

db_serv = SQLAlchemy(app)



