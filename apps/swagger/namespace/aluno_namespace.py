from flask_restx import Namespace, Resource, fields
from alunos.model_aluno import procurar_aluno_por_id, criar_novo_aluno, deletar_aluno_por_id, alterar_informacoes_aluno, listar_alunos

alunos_ns = Namespace("alunos", description="Operações realizadas aos alunos")

aluno_model = alunos_ns.model("Aluno", {
    "nome": fields.String(required=True, description="Nome do aluno"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (YYYY/MM/DD)"),
    "nota_primeiro_semestre": fields.Float(required=True, description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(required=True, description="Nota do segundo semestre"),
    "turma_id": fields.Integer(required=True, description="ID da turma associada")
})

aluno_output_model = alunos_ns.model("AlunoOutput", {
    "id": fields.Integer(description="ID do aluno"),
    "nome": fields.String(description="Nome do aluno"),
    "idade": fields.Integer(description="Idade do aluno"),
    "data_nascimento": fields.String(description="Data de nascimento (YYYY/MM/DD)"),
    "nota_primeiro_semestre": fields.Float(required=True, description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(required=True, description="Nota do segundo semestre"),
    "turma_id": fields.Integer(required=True, description="ID da turma associada"),
    "media_final": fields.Float(description="Média final do aluno")
})

@alunos_ns.route("/")
class AlunosResource(Resource):
    @alunos_ns.marshal_list_with(aluno_output_model)
    def get(self):
        """"Listar todos os alunos"""
        return listar_alunos()
    
    @alunos_ns.expect(aluno_model)
    def post(self):
        """Cria um novo aluno"""
        data = alunos_ns.payload
        response, status_code = criar_novo_aluno(data)
        return response, status_code
    
@alunos_ns.route("/<int:id_aluno>")
class AlunoIdResource(Resource):
    @alunos_ns.marshal_with(aluno_output_model)
    def get(self, id_aluno):
        """Obtém um aluno pelo ID"""
        return procurar_aluno_por_id(id_aluno)
    
    @alunos_ns.expect(aluno_model)
    def put(self, id_aluno):
        """Atualizar um aluno pelo seu ID"""
        data = alunos_ns.payload
        alterar_informacoes_aluno(id_aluno, data)
        return {"message": "Aluno atualizado com êxito"}, 200

    def delete(self, id_aluno):
        """Excluir um aluno pelo seu ID"""
        deletar_aluno_por_id(id_aluno)
        return {"message": "Aluno excluído com êxito"}, 200
