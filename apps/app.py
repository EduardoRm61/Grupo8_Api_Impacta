from config import app
from professores.route_prof import bp_professor
from turma.routes_turma import bd_Turma
from alunos.route_aluno import bp_aluno
from flask_sqlalchemy import SQLAlchemy


#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://adm:12345@db:3306/SistemaEscolar'
#app.config.from_object(Config)
#db_serv = SQLAlchemy(app)
#db_serv.init_app(app)


app.register_blueprint(bp_professor)
app.register_blueprint(bd_Turma)
app.register_blueprint(bp_aluno)



# Criando o app



# Inicializando o Banco com o app
#db.init_app(app)


if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
