from flask import Flask, jsonify

dados = {"alunos":[], 
        "professores":[
            {"ide": 10, "nome": "Caio", "idade": 27, "matéria": "Dev API E Micros", "obsercacoes": "Contato com aulo via Chat"},     #lembrar da vírula
            {"ide": 11, "nome": "Odair", "idade": 30, "matéria": "- DevOps", "obsercacoes": None }
            ]
        }

app = Flask(__name__)

@app.route('/professores', methods=['GET'])
def listar_professores():
    
    ''' Retorno dos dados da list/dict professor'''
    
    return jsonify("mensagem": "Dados gerais do professor ": professores), 200


@app.route("/professores/<int:id>", methods=["GET"])

def pesquisa_professor(id):
        
    '''Retorno do dono dos dados id/pk do dict professor'''
            
    for professor in dados["professores"]:     #lembrar - chamar nome da lista e dentro do colchete o dado a ser acessado, neste caso dict professores
        print(professor)
        if professor["id"] == id:
            return jsonify("mensagem": "Dados do professor": professor), 200
        return jsonify({"mensagem": "Not Found - Professor inexistente"}), 404

        

@app.route('/professores', methods=['POST'])
def cadastrar_professores():
    dados = request.json
    novo_professor = {
        'id': len(professores) +1,
        'nome':dados.get('nome')

        
    }
    professores.append(novo_professor)
    return jsonify(novo_professor), 201
    
    @app.route('/profesores/<int:id>', methods=['PUT'])
    def atualizar_professor(id):
        dados = request.json
        for professor in professores:
        f professor['id'] == id:
            professor['nome'] = dados.get('nome', professor['nome'])
            professor['disciplina'] = dados.get('disciplina', professor['disciplina'])
            return jsonify(professor), 200
    return jsonify({'erro': 'Professor não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
