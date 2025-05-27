from swagger.swagger_config import configure_swagger
from config import app
from apps.swagger import bp_api, api
from swagger.namespace.aluno_namespace import alunos_ns
from swagger.namespace.turma_namespace import turma_ns
from swagger.namespace.professor_namespace import professor_ns
from professores.route_prof import bp_professor
from turma.routes_turma import bd_Turma
from alunos.route_aluno import bp_aluno

api.add_namespace(turma_ns, path="/Turma")
api.add_namespace(alunos_ns, path="/alunos")
api.add_namespace(professor_ns, path="/professores")

app.register_blueprint(bp_api, url_prefix='/api') # Registrando o Blueprint do swagger
# configure_swagger(app)

app.register_blueprint(bp_professor, url_prefix='/api')
app.register_blueprint(bd_Turma, url_prefix='/api')
app.register_blueprint(bp_aluno, url_prefix='/api')



# Criando o app



# Inicializando o Banco com o app
#db.init_app(app)


if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
