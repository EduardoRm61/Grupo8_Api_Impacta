from flask import Flask, jsonify, request


professores = {"professor":[
            {"id": 10, "nome": "Caio", "idade": 27, "materia": "Dev API E Micros", "obs": "Contato com aluno via Chat"},     #lembrar da vírula  | troquei para obs, o nome dava muito erro
            {"id": 11, "nome": "Odair", "idade": 30, "materia": "DevOps", "obs": None }   #correção do nome - Dev para apenas Dev = cuiaddo, dá erro
            ]
        }

app = Flask(__name__)



@app.route('/professores', methods=['GET'])
def listar_professores():
    
    ''' Retorno dos dados da list/dict professor'''
    
    return jsonify({"mensagem": "Ok", "professor": professores["professor"]}), 200  #faltou chamar a chave


@app.route("/professores/<int:id>", methods=["GET"])

def pesquisa_professor(id):
        
    '''Retorno do dono dos dados id/pk do dict professor'''
            
    for professor in professores["professor"]:     #lembrar - chamar nome da lista e dentro do colchete o dado a ser acessado, neste caso dict professores
        if professor["id"] == id:
            return jsonify({"mensagem": "Ok", "professor": professor}), 200    # chave mensagem possui ok, chave professor possui dict professor NESTE CASO CHAMA DIRETO A CHAVE E NÃO O DICT
        return jsonify({"error": "Not Found - Professor inexistente"}), 404     #Não vi que o do Edu estava como o meu, arrumando

        
#observar cod no comentário a baixo
# @app.route('/professores', methods=['POST'])
# def cadastrar_professores():
    
#     '''Adição de novo professor'''
    
#     professores = request.json
#     novo_professor = {
#         'id': len(professores) +1,
#         'nome':professores.get('nome')
#     }
#     professores.append(novo_professor)
#     return jsonify(novo_professor), 201


@app.route('/professores', methods=['POST'])

def cadastrar_professores():

    '''Cadastra um novo professor'''
   
    novo_professor = request.json

    if not novo_professor or "nome" not in novo_professor or "materia" not in novo_professor:  #adicionando materia como campo obrigatório além do nome | correção do or após "nome", ele não existe
        return jsonify({"error": "Id, nome e matéria são obrigatórios"}), 400
    '''pegar último, compara, adiciona 1 no índice, add o prof. Caso list vazia, inicia no índice 1 (trás pra frente)'''
    if professores["professor"]:
        ultimo_professor = professores["professor"][-1]
        novo_id_prof = ultimo_professor["id"] + 1
    else:
       novo_id_prof = 1

    novo_professor["id"] = novo_id_prof
    professores["professor"].append(novo_professor)

    return jsonify({"mensagem": "Created", "professor": novo_professor}), 201    #retorna novo professor 
    
@app.route('/profesores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    
    ''' Atualização dos dados do professor'''
    
    professores = request.json
    for professor in professores:
        if professor['id'] == id:
            professor['nome'] = professores.get('nome', professor['nome'])
            professor['idade'] = professores.get('idade', professor['idade'])
            professor['materia'] = professores.get('materia', professor['materia'])
            professor['obs'] = professores.get('obs', professor['obs'])
            return jsonify({"mensagem": "Atualizado", "professor": professor}), 200  #não retorna a lista, apenas os dados da chave professor
    return jsonify({"error": "Not Found - Professor inexistente"}), 404

@app.route("/professsores/<int:id>", methods = ["DELETE"])

def delete_professor(id):
    for professor in professores["professor"]:   #lembrar que chamo 1° o dict e dentro do colchete[] chamo a chave
        if professor["id"] == id:
            professores["professor"].remove(professor)   #mesmo erro da de cima dict ["chave"]
            return jsonify({"mensagem": "Deletado", "professor": professor}) #apenas o prfessor deletado
    return jsonify({"error": "Not Found - Professor inexistente"}), 404

if __name__ == '__main__':
    app.run(debug=True)
    
