# centraliza e gerencia as configurações do app
# ex: chaves secretas, url de BD e conf de ambiente
# customiza, separa, simplifica o desenvolvimento
# todas configurações de bd

import os
from flask import Flask

app = Flask(__name__) 
# a variável app recebe class Flask(aqui receberá no nome do arquivo - algo automático, até onde entendi)

app.config["HOST"] = "localhost"
app.config["PORT"]  = 5002
app.config["DEBUG"] = True

# o local de configuração do app [computador] é "localhost | define o servidor, a máquina - até onde entendi pi 127.0.0.1
# a porta de comunicação/entrada do servidor é 5002
# debug ativa o modo de depuração (identificar, analizar e corrigir erros/bugd) | faz recarga automática | erros - mostra linha, tipo e caminho | em true é porque está ativo

#aqui entra configuração de sql, pelo que entendi