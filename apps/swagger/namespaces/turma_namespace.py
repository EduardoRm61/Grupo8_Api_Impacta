from flask_restx import Namespace, Resource, fields
from apps.turma import model_turma as modTur

turma_ns = Namespace("turma", description="Operações relacionadas às turmas")

turma_model = turma_ns.model("Turma", {
    "Id": fields.Integer(required=True, description="ID da turma"),
    "Descrição": fields.String(required=True, description="Descrição da turma"),
    "Ativa": fields.Boolean(required=True, description="Status da turma (True/False)"),
    "Professor Id": fields.Integer(required=True, description="ID do professor responsável")
})

turma_output_model = turma_ns.model("TurmaOutput", {
    "Id": fields.Integer(description="ID da turma"),
    "Descrição": fields.String(description="Descrição da turma"),
    "Ativa": fields.Boolean(description="Status da turma"),
    "Professor Id": fields.Integer(description="ID do professor responsável")
})

@turma_ns.route("/")
class TurmaResource(Resource):
    @turma_ns.marshal_list_with(turma_output_model)
    def get(self):
        """Lista todas as turmas"""
        return modTur.listarTurma()

    @turma_ns.expect(turma_model)
    def post(self):
        """Cria uma nova turma"""
        data = turma_ns.payload
        return modTur.criarNovaTurma(data)

@turma_ns.route("/<int:id_turma>")
class TurmaIdResource(Resource):
    @turma_ns.marshal_with(turma_output_model)
    def get(self, id_turma):
        """Obtém uma turma pelo ID"""
        return modTur.procurarTurmaPorId(id_turma)

    @turma_ns.expect(turma_model)
    def put(self, id_turma):
        """Atualiza uma turma pelo ID"""
        data = turma_ns.payload
        return modTur.alterarInformacoes(
            Id_turma=id_turma,
            Descricao=data["Descrição"],
            Ativa=data["Ativa"],
            Id_Pro=data["Professor Id"]
        )

    def delete(self, id_turma):
        """Exclui uma turma pelo ID"""
        return modTur.deletarTurmaPorId(id_turma)

@turma_ns.route("/reset")
class TurmaResetResource(Resource):
    def delete(self):
        """Remove todas as turmas"""
        return modTur.deletarTurma()