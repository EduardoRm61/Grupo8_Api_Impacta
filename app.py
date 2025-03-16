from flask import Flask, jsonify, request


professores = {"professor":[
            {"id": 10, "nome": "Caio", "idade": 27, "materia": "Dev API E Micros", "observacoe": "Contato com aluno via Chat"},     #lembrar da vírula
            {"id": 11, "nome": "Odair", "idade": 30, "materia": "DevOps", "observacoe": None }   #correção do nome - Dev para apenas Dev = cuiaddo, dá erro
            ]
        }

app = Flask(__name__)



@app.route('/professores', methods=['GET'])
def listar_professores():
    
    ''' Retorno dos dados da list/dict professor'''
    
    return jsonify(professores), 200


@app.route("/professores/<int:id>", methods=["GET"])

def pesquisa_professor(id):
        
    '''Retorno do dono dos dados id/pk do dict professor'''
            
    for professor in professores["professor"]:     #lembrar - chamar nome da lista e dentro do colchete o dado a ser acessado, neste caso dict professores
        if professor["id"] == id:
            return jsonify(professor), 200
        return jsonify({"Not Found - Professor inexistente"}), 404

        
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

    if not novo_professor or "id" not in novo_professor:
        return jsonify({"Id obrigatório"}), 400

    '''pegar último, compara, adiciona 1 no índice, add o prof. Caso list vazia, inicia no índice 1 (trás pra frente)'''
    if professores["professor"]:
        ultimo_professor = professores["professor"][-1]
        novo_id_prof = ultimo_professor["id"] + 1
    else:
       novo_id_prof = 1

    novo_professor["id"] = novo_id_prof
    professores["professor"].append(novo_professor)

    return jsonify(novo_professor), 201
    
@app.route('/profesores/<int:id>', methods=['PUT'])
def atualizar_professor(id):
    
    ''' Atualização dos dados do professor'''
    
    professores = request.json
    for professor in professores:
        if professor['id'] == id:
            professor['nome'] = professores.get('nome', professor['nome'])
            professor['idade'] = professores.get('idade', professor['idade'])
            professor['materia'] = professores.get('materia', professor['materia'])
            professor['obsercacoes'] = professores.get('obsercacoes', professor['obsercacoes'])
            return jsonify(professor), 200
    return jsonify({"Not Found - Professor inexistente"}), 404

@app.route("/professsores/<int:id>", methods = ["DELETE"])

def delete_professor(id):
    for professor in professores:
        if professor["id"] == id:
            professores.remove(professor)
            return jsonify(professor)
    return jsonify("Not Found - Professor inexistente")

if __name__ == '__main__':
    app.run(debug=True)
    
