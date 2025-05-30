from flask import Blueprint, request, jsonify
import turma.model_turma as modTur



bd_Turma = Blueprint('Turma', __name__ )

@bd_Turma.route("/Turma",methods=["GET"])                              
def listar_turma():
    try:
        Turmas = modTur.listarTurma()
        return jsonify(Turmas)
    except modTur.TurmaNaoIdentificada as Tr:
        return jsonify ({"Requisição inválida":str(Tr)}), 400
    
@bd_Turma.route("/Turma/<int:id_turma>", methods=["GET"])            
def procurarTurma(id_turma):
     try:
        dados = modTur.procurarTurmaPorId(id_turma)
        return jsonify(dados)
     except modTur.TurmaNaoIdentificada as trm:
          return jsonify({"Erro:": str(trm)}), 402  #Isso precisa ser alterado


@bd_Turma.route("/Turma", methods=["POST"])
def AddTurma():
    nv_dict = request.json

    try: 
         
        if not modTur.professorExistente(nv_dict["Professor Id"]):
            return jsonify({
                "Erro": "Requisição inválida",
                "Detalhes": "Id do Professor inexistente"
            }), 404   #inexistente | estava bad request

        if modTur.turmaJaExiste(nv_dict["Id"]):
            return jsonify({
                "Erro": "Requisição inválida",
                "Detalhes": "Id da Turma já existente"
            }), 409  #conflict - duplicado ou duplo - estava 400 bad request
        
        dados_turma = {
            'id': int(nv_dict.get('Id')),
            'descricao': nv_dict('Descrição'),
            'professor_id': int(nv_dict.get('Professor Id')),
            'ativa': nv_dict('Ativa', True)
        }

        modTur.criarNovaTurma(nv_dict)
        return jsonify({"mensagem": "Turma criada com sucesso!", "turma": nv_dict}), 201
    
    except modTur.CadastroDeTurmaFalhado as cdtf:
         return jsonify({
            "Erro": "Falha ao cadastrar turma",
            "detalhes": str(cdtf)
         }), 400    


@bd_Turma.route("/Turma/Resetar", methods=["DELETE"])
def ResetarTodaTurma():
    try:
        modTur.deletarTurma()
        return jsonify({"mensagem": "Resetado"}), 200
    except modTur.TurmaJaDeletada as Trm:
        return jsonify ({"Requisção Inválida": str(Trm)}), 400 
    
@bd_Turma.route("/Turma/Resetar/<int:id_turma>", methods=["DELETE"])
def ResetarTurmaId(id_turma):
     try:
          modTur.deletarTurmaPorId(id_turma)
          return jsonify({"Descrição": "Turma cadastrada com êxito!"}), 200
     except modTur.TurmaNaoIdentificada as trm:
          return jsonify({"Erro:": str(trm)}), 404

@bd_Turma.route("/Turma/Alterar/<int:id_turma>", methods=["PUT"])
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
    
    resultado, status_code = modTur.alterarInformacoes(id_turma, dados["descrição"], dados["ativa"], dados["professor_id"])
    return jsonify(resultado), status_code  