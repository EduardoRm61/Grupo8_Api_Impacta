''' Devio ocorrência de falhas entre Turma e Alunos, esta table irá analisar, apenas, códigos relacionados a professores.
Deverá ser integrado a file de teste geral sql'''

from apps.config import app, db_serv
from apps.professores.route_prof import bp_professor
from apps.professores.model_prof import Professor

app.register_blueprint(bp_professor, url_prefix="/professores")

if __name__ == '__main__':
    with app.app_context():
        # Cria SOMENTE a tabela do Professor
        if not db_serv.engine.dialect.has_table(db_serv.engine.connect(), "professor"):
            Professor.__table__.create(db_serv.engine)
    
    app.run(host="0.0.0.0", port=5002, debug=True)
