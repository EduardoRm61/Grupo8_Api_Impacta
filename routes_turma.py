from flask import Blueprint, request, jsonify
import model_turma as modTur


Bd_Turma = Blueprint('Turma', __name__ )

@Blueprint.route("/Turma",methods=["GET"])                              
def listar_turma():
    try:
        Turmas = modTur.ListarTurma()
        return jsonify(Turmas)
    except modTur.TurmaNaoIdentificada as Tr:
        return {"Requisição inválida":str(Tr)}, 400


