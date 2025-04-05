from flask import Blueprint

profes = Blueprint("professores", __name__)

@profes.route("/professores", methods = ["GET"])
def main():
    return "Rotas dos professores"