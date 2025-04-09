from flask import Blueprint, request, jsonify
import turma.model_turma as modTur


Bd_Turma = Blueprint('Turma', __name__ )

@Bd_Turma.route("/Turma",methods=["GET"])                              
def listar_turma():
    try:
        Turmas = modTur.ListarTurma()
        return jsonify(Turmas)
    except modTur.TurmaNaoIdentificada as Tr:
        return jsonify ({"Requisição inválida":str(Tr)}), 400
    
@Bd_Turma.route("/Turma/<int:id_turma>", methods=["GET"])            
def procurarTurma(id_turma):
     try:
        dados = modTur.ProcurarTurmaPorId(id_turma)
        return jsonify(dados)
     except modTur.TurmaNaoIdentificada as trm:
          return jsonify({"Erro:": str(trm)}), 402  #Isso precisa ser alterado


@Bd_Turma.route("/Turma", methods=["POST"])
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


@Bd_Turma.route("/Turma/Resetar", methods=["DELETE"])
def ResetarTodaTurma():
    try:
        modTur.DeletarTurma()
        return jsonify({"mensagem": "Resetado"}), 200
    except modTur.TurmaJaDeletada as Trm:
        return jsonify ({"Requisção Inválida": str(Trm)}), 400 
    
@Bd_Turma.route("/Turma/Resetar/<int:id_turma>", methods=["DELETE"])
def ResetarTurmaId(id_turma):
     try:
          modTur.DeletarTurmaPorId(id_turma)
          return jsonify(modTur.dadosTurma["Turma"]), 200
     except modTur.TurmaNaoIdentificada as trm:
          return jsonify({"Erro:": str(trm)}), 404

@Bd_Turma.route("/Turma/Alterar/<int:id_turma>", methods=["PUT"])
def AlterarInfo(id_turma):
    dados = request.json
    
    #dict['id'] = int (dict['id'])

    if not dados:
        return jsonify({
            "Erro": "Requisição inválida",
            "Descrição": "O corpo da requisição está vazio, preencha todos os campos"
        }), 400
    
    if "Descrição" not in dados:
        return jsonify({
            "Erro": "Não foi possível fazer a requisição",
            "Dscrição": "O campo Descrição da turma é obrigatório ser preenchido"
        }), 400
    
    if "Ativa" not in dados:
        return jsonify({
            "Erro": "Não foi possível fazer a requisição",
            "Descrição": "O campo Ativa é obrigatório ser preenchido "
        }), 400
    
    if "Professor Id" not in dados:
        return jsonify({
            "Erro": "Não foi possível fazer a requisição",
            "Descrição": "O campo Professor Id é obrigatório se preechido"
        }), 400
    
    resultado, status_code = modTur.AlterarInformacoes(id_turma, dados["Descrição"], dados["Ativa"], dados["Professor Id"])
    return jsonify(resultado), status_code  