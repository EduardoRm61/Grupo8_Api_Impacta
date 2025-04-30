import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["HOST"] = "0.0.0.0"  # 127.0.0.1 - apenas host local, mudei para 0.0.0.0 para remoto poder acessar
app.config["PORT"]= 5002
app.config["DEBUG"] = True

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://adm:12345@db:3306/SistemaEscolar'
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://${adm}:${12345}@${db}/${dados_mysql}"

#app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql"://{DB_USER}:{DB_PASSWORLD}@{DB_HOST}:{DB_PORT}/{DB_NAME}
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
db_serv = SQLAlchemy(app)