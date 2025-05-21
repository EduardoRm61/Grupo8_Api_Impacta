from flask_restx import Namespace, Resource, fields
from turma.model_turma import procurarTurmaPorId, criarNovaTurma, listarTurma, deletarTurma, deletarTurmaPorId, valoorBuleano, alterarInformacoes

turma_ns = Namespace("Turma", description="Operações relacionadas as Turmas")

turma_model = turma_ns.model("Turma", {
    "id": fields.Integer(required=True, description="Id da turma"),
    "descriaoo": fields.String(required=True, description="Descrição da Turma/nome"),
    "ativa": fields.Boolean(required=True, description="Turma ativa: True ou False"),
    "professor_id": fields.Integer(required=True, description="Id do professor associado"),
})

turma_output_model = turma_ns.model("TurmaOutput",{
    "id": fields.Integer(description="Id da Turma"),
    "descriacao": fields.String(description="Descrição da Turma"),
    "ativa": fields.Boolean(description="Turma está ativa: True ou False"),
    "professor_id": fields.Integer(description= "Id relacionado a Professor")
})

@turma_ns.route('/')
class TurmaResource(Resource):
    @turma_ns.marshal_list_with(turma_output_model)
    def get(self):
        """Listar todas as turma"""
        return listarTurma()
    
