from swagger.swagger_config import configure_swagger
from config import app
from professores.route_prof import bp_professor
from turma.routes_turma import bd_Turma
from alunos.route_aluno import bp_aluno
#from flask_sqlalchemy import SQLAlchemy # Não está fazendo nada
from apps.swagger import bp_api
from apps.swagger.namespace.turma_namespace import turma_ns



#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://adm:12345@db:3306/SistemaEscolar'
#app.config.from_object(Config)
#db_serv = SQLAlchemy(app)
#db_serv.init_app(app)

#api.add_namespace(turma_ns) # Adicionando o namespace ao Api

app.register_blueprint(bp_api) # Registrando o Blueprint do swagger
configure_swagger(app)

app.register_blueprint(bp_professor, url_prefix='/api')
app.register_blueprint(bd_Turma, url_prefix='/api')
app.register_blueprint(bp_aluno, url_prefix='/api')



# Criando o app



# Inicializando o Banco com o app
#db.init_app(app)


if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
