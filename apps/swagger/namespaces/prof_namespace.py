from flask_restx import Namespace, Resource, fields
from apps.professores import model_prof as modpro

professor_ns = Namespace("professores", description="Operações relacionadas aos professores")

professor_model = professor_ns.model("Professor", {
    "id": fields.Integer(required=True, description="Identificação (id) do professor"),
    "nome": fields.String(required=True, description="Nome do professor"),
    "idade": fields.Integer(required=False, description="Idade do professor"),
    "materia": fields.String(required=True, description="Matéria que o professor leciona"),
    "obs": fields.String(required=False, description="Observação adicional")
})

professor_output_model = professor_ns.model("ProfessorOutput", {
    "id": fields.Integer(description="Identificação (id) do professor"),
    "nome": fields.String(description="Nome do professor"),
    "idade": fields.Integer(description="Idade do professor"),
    "materia": fields.String(description="Matéria que o professor leciona"),
    "obs": fields.String(description="Observação adicional")
})

@professor_ns.route("/")
class ProfessorLista(Resource):
    @professor_ns.expect(professor_model)
    def post(self):
        """Cria um novo professor"""
        data = professor_ns.payload
        return modpro.criarNovoProfessor(data)

@professor_ns.route("/<int:id_professor>")
class ProfessorResource(Resource):
    def get(self, id_professor):
        """Busca um professor pelo ID"""
        return modpro.procurarProfessorPorId(id_professor)

    @professor_ns.expect(professor_model)
    def put(self, id_professor):
        """Atualiza um professor pelo ID"""
        data = professor_ns.payload
        return modpro.atualizarProfessor(id_professor, data)

    def delete(self, id_professor):
        """Deleta um professor pelo ID"""
        return modpro.deletarProfessorPorId(id_professor)

@professor_ns.route("/resetar")
class ProfessorReset(Resource):
    def delete(self):
        """Reseta todos os professores"""
        return modpro.resetar_professores()
    
    #teste push/conexão/ estava falhando