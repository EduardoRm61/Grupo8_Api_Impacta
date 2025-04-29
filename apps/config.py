import os   #porque impostar os se não estou usando?
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["HOST"] = "0.0.0.0"  # 127.0.0.1 - apenas host local, mudei para 0.0.0.0 para remoto poder acessar
app.config["PORT"]= 5002
app.config["DEBUG"] = True

#-----------------------------------------------------------------------------------------------------------#
#                                   Conexão com .env - usar mysql                                           #
#--------------------------------------------------------------------------------------------------------#

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://${adm}:${12345}@${db}/${dados_mysql}"  # como será a conexão do flask ao mysql
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# DB_HOST: db  # Nome do serviço MySQL no compose
# DB_NAME: dados_mysql
# DB_USER: adm
# DB_PASSWORD: 12345
# "mysql+pymysql://DB_USER:DB_PASSWORD@DB_HOST/DB_NAME"
# ESTÁ EM APP: ENVIRONMENT

db_serv = SQLAlchemy(app)   #instanciando/criando objeto do SQLAlchemy vinculado ao app/flask
