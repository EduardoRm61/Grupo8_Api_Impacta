from flask import Blueprint, request, jsonify
import model_turma as modTur


Bd_Turma = Blueprint('Turma', __name__ )

@Blueprint.route("/Turma",methods=["GET"])                              
def listar_turma():
    try:
        Turmas = modTur.ListarTurma()
        return jsonify(Turmas)
    except modTur.TurmaNaoIdentificada as Tr:
        return jsonify ({"Requisição inválida":str(Tr)}), 400
    
@Blueprint.route("/Turma/<int:id_turma>", methods=["GET"])            
def procurarTurma(id_turma):
     try:
        dados = modTur.ProcurarTurmaPorId(id_turma)
        return jsonify(dados)
     except modTur.TurmaNaoIdentificada as trm:
          return jsonify({"Erro:": str(trm)}), 402  #Isso precisa ser alterado


@Blueprint.route("/Turma", methods=["POST"])
def AddTurma():
    nv_dict = request.json
    nv_dict['Id'] = int(nv_dict['Id'])
    nv_dict['Professor Id'] = int(nv_dict['Professor Id'])

    try:
         
        if not modTur.ProfessorExistente(nv_dict["Professor Id"]):
            return jsonify({
                "Erro": "Requisição inválida",
                "Detalhes": "Id do Professor inexistente"
            }), 404   #inexistente | estava bad request

        if modTur.TurmaJaExiste(nv_dict["Id"]):
            return jsonify({
                "Erro": "Requisição inválida",
                "Detalhes": "Id da Turma já existente"
            }), 409  #conflict - duplicado ou duplo - estava 400 bad request
        modTur.CriarNovaTurma(nv_dict)
        return jsonify({"mensagem": "Turma criada com sucesso!", "turma": nv_dict}), 201
    
    except modTur.CadastroDeTurmaFalhado as cdtf:
         return jsonify({
            "Erro": "Falha ao cadastrar turma",
            "detalhes": str(cdtf)
         }), 400    


@Blueprint.route("/Turma/Resetar", methods=["DELETE"])
def ResetarTodaTurma():
    try:
        modTur.DeletarTurma()
        return jsonify({"mensagem": "Resetado"}), 200
    except modTur.TurmaJaDeletada as Trm:
        return jsonify ({"Requisção Inválida": str(Trm)}), 400 
