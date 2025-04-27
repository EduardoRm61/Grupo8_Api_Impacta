import os
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desativando o rastreamento de modificações para melhorar o desempenho


app.config['HOST'] = '0.0.0.0'
app.config['PORT']= 5002
app.config['DEBUG'] = True
