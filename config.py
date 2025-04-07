import os
from flask import Flask

app = Flask(__name__)

app.config['HOST'] = 'localhost'
app.config['PORT']=5002
app.config['DEBUG'] = True
