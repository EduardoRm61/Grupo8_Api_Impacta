from swagger.swagger_config import configure_swagger
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


app.register_blueprint(bp_professor, url_prefix='/api')
app.register_blueprint(bd_Turma, url_prefix='/api')
app.register_blueprint(bp_aluno, url_prefix='/api')

configure_swagger(app)

# Criando o app



# Inicializando o Banco com o app
#db.init_app(app)


if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
