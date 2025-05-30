from flask_restx import Namespace, Resource, fields
from turma.model_turma import procurarTurmaPorId, criarNovaTurma, listarTurma, deletarTurma, deletarTurmaPorId, valoorBuleano, alterarInformacoes

turma_ns = Namespace("Turma", description="Operações relacionadas as Turmas")

turma_model = turma_ns.model("Turma", {
    "id": fields.Integer(required=True, description="Id da turma"),
    "descricao": fields.String(required=True, description="Descrição da Turma/nome"),
    "ativa": fields.Boolean(required=True, description="Turma ativa: True ou False"),
    "professor_id": fields.Integer(required=True, description="Id do professor associado"),
})

turma_output_model = turma_ns.model("TurmaOutput",{
    "id": fields.Integer(description="Id da Turma"),
    "descricao": fields.String(description="Descrição da Turma"),
    "ativa": fields.Boolean(description="Turma está ativa: True ou False"),
    "professor_id": fields.Integer(description= "Id relacionado a Professor")
})

@turma_ns.route('/')
class TurmaResource(Resource):
    @turma_ns.marshal_list_with(turma_output_model)
    def get(self):
        """Listar todas as turma"""
        return listarTurma()
    
    @turma_ns.expect(turma_model)
    def post(self):
        """"Criar uma nova turma"""
        data = turma_ns.payload
        response, status_code = criarNovaTurma(data)
        return response, status_code
    
@turma_ns.route("/<int:id_turma>")
class TurmaIdResource(Resource):
    @turma_ns.marshal_list_with(turma_output_model)
    def get(self, id_turma):
        "Obtém uma turma pelo seu ID"
        return procurarTurmaPorId(id_turma)
    
    @turma_ns.expect(turma_model)
    def put(self, id_turma):
        """Atualiza uma turma pelo seu ID"""
        data = turma_ns.payload
        alterarInformacoes(
            id_turma,
            data.get('descricao'),
            data.get('ativa'),
            data.get('professor_id'))
        return data, 200

    def delete(self, id_turma):
        """Excluí uma turma pelo seu ID"""
        return deletarTurmaPorId(id_turma)


@turma_ns.route('/resetar')
class Turmareset(Resource):
    def delete(self):
        """Resetar todas as Turma"""
        return deletarTurma()