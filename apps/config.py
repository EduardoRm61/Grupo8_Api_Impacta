import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['HOST'] = '0.0.0.0'
app.config['PORT']= 5002
app.config['DEBUG'] = True



app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://${adm}:${12345}@${db}/${SistemaEscolar}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  




app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://adm:12345@db:3306/SistemaEscolar'
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://${adm}:${12345}@${db}/${dados_mysql}"

#Aqui eu estou criando o Objeto db
db_serv = SQLAlchemy(app)