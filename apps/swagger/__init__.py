from flask_restx import Api
from flask import Blueprint
# Criando o Blueprint para a API
bp_api = Blueprint("api", __name__, url_prefix="/api")

api = Api(
    bp_api,
    version="1.0",
    title="API de Gestão Escolar",
    description="Documentação da API para Alunos, Professores e Turmas",
    doc="/docs",
    mask_swagger=False, # Desativa o X-Fields no Swagger,
    prefix=""
)