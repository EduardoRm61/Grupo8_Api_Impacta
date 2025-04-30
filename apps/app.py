
from config import app                                      # estava apps.config import ...
from professores.route_prof import bp_professor
from flask_restx import Api

#_____________________________ ROTA_____________________________

app.register_blueprint(bp_professor)

#_____________________________CONFIGURAÇÃO API RESTful USANDO FLASK-RESTX___________________________

api = Api(
  app, # instância/obj da aplicação Flask, criada com Flask(__name__)
  version= "1.0" # posso encontrar informações no fork >> Flask-RESTX Documentation << 
  title= "Grupo8_Api_Impacta"  # título da api
  description= "Aplicativo de gerenciamênto de dados de turmas, professor e alunos da faculdade Impacta" # descrição do app
  doc = "/docs"  # Habilita a documentação Swagger/Open/Api. Define o endpoint onde Swaegger ui estará
)
  
if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )


