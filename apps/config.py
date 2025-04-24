import os
from flask import Flask

app = Flask(__name__)

app.config['HOST'] = "0.0.0.0"  # 127.0.0.1 - apenas host local, mudei para 0.0.0.0 para remoto poder acessar
app.config['PORT']= 5002
app.config['DEBUG'] = True

#-----------------------------------------------------------------------------------------------------------#
#                                   Conexão com .env - usar mysql                                           #
#-----------------------------------------------------------------------------------------------------------#

# app.config["USER"] = "localhost"       # nac riação do dockerMySQL aparece o root e depois coloca a senha
# app.config["PASSWORD"] = "ro0t"
# app.config["Name"] = "testeMySQL"