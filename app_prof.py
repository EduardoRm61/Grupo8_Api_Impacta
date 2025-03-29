from flask import Flask, jsonify, request
import model_turma as modTur
app = Flask(__name__)
                
# Todas as rotas:

@app.route("/reseta", methods=["POST","DELETE"])
def reseta():
    apaga_tudo()
    return "resetado" 

# apenas professores - juntar, se correto, à app.py

@app.route('/professores', methods=['GET'])
def listar_professores():
    
    '''Devolve list/dict de todos professores'''
    
    try:
        return jsonify({"mensagem": "Ok", "professores": professores["professor"]}) 
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500 
    #posso trocar para 404 not found? 500 é erro interno

@app.route("/professores/<int:id>", methods=["GET"])
def pesquisa_professor(id):
    
    '''Devolve dict professore/professor com base no id (chave/pk)'''
    
    try:
        professor = procurarProfessorPorId(id)
        return jsonify({"mensagem": "Ok", "professor": professor}), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404
    
# ------------------- # --------------------------------------#

@app.route('/professores', methods=['POST'])
def cadastrar_professores():
    
    '''Add novo professor a list/dict'''
    
    novo_professor = request.json
    if not novo_professor or "nome" not in novo_professor or "materia" not in novo_professor:
        return jsonify({"erro": "Nome e matéria são obrigatórios"}), 400
    #aqui deve ter nome, id e matéria obrigatório
    
    try:
        if modTur.ProfessorExistente(novo_professor["id"]):  # Correção: Verifica se o professor já existe
            raise ProfessorExiste("Professor já existe")
        criarNovoProfessor(novo_professor)
        return jsonify({"mensagem": "Created", "professor": novo_professor}), 201

    except ProfessorExiste as e:
        return jsonify({"erro": str(e)}), 400
    #pode ser erro 409 - conflict - conflito entre dados ou dados iguais?
    
# ------------------- # --------------------------------------#

@app.route('/professores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    
    ''' Atualização dos dados de professor já existentes'''
    
    atualizado = request.json
    try:
        professor = procurarProfessorPorId(id) # Correção: Usar a função de procurarProfessorPorId correta
        if "nome" in atualizado:
            professor['nome'] = atualizado['nome']
        if "idade" in atualizado:
            professor['idade'] = atualizado['idade']
        if "materia" in atualizado:
            professor['materia'] = atualizado['materia']
        if "obs" in atualizado:
            professor['obs'] = atualizado['obs']
        return jsonify({"mensagem": "Atualizado", "professor": professor}), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": f"Internal Server Error: {str(e)}"}) # Correção: Mensagem de erro mais clara

# ------------------- # --------------------------------------#

@app.route("/professores/deletar/<int:id_professor>", methods=["DELETE"])
def delete_professor(id_professor):
    
    '''Apagar dados de professor já existente'''
    try:
        resultado = deletarProfessorPorId(id_professor)
        return jsonify(resultado), 200
    except ProfessorNaoIdentificado as e:
        return jsonify({"erro": str(e)}), 404

# ------------------- # --------------------------------------#

@app.route('/professores/resetar', methods=['DELETE'])
def resetar_professor():
    
    '''Restaurar do zero a lista professores'''
    
    resetar_professores()  # Função que reseta o dicionário de professores
    return jsonify({"mensagem": "Resetado"}), 200



if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)