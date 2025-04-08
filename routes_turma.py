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
    
@Blueprint.route("/Turma/<int:id_turma>", methods=["GET"])            
def procurarTurma(id_turma):
     try:
        dados = modTur.ProcurarTurmaPorId(id_turma)
        return jsonify(dados)
     except modTur.TurmaNaoIdentificada as trm:
          return jsonify({"Erro:": str(trm)}), 402  #Isso precisa ser alterado



