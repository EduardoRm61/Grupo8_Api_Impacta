from flask import Flask, jsonify

dados = {"alunos":[], 
        "professores":[
            {"ide": 10, "nome": "Caio", "idade": 27, "matéria": "Dev API E Micros", "obsercacoes": "Contato com aulo via Chat"}
            {"ide": 11, "nome": "Odair", "idade": 30, "matéria": "- DevOps", "obsercacoes": None }
            ]
        }

app = Flask(__name__)

@app.route('/professores', methods=['GET'])
def listar_professores():
    
    return jsonify(professores), 200

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
