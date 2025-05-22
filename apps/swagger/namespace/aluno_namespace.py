from flask_restx import Namespace, Resource, fields
from alunos.model_aluno import procurar_aluno_por_id, criar_novo_aluno, deletar_aluno_por_id, alterar_informacoes_aluno, aluno_ja_existe, deletar_alunos, med

alunos_ns = Namespace("alunos", description="Operações realizadas aos alunos")

aluno_model = alunos_ns.model("Aluno",{
    "nome": fields.String(required=True, description="Nome do aluno"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (YYYY/MM/DD)"),
    "nota_primeiro_semestre": fields.Float(required=True, description="Nota do primeiro semestre"),
    "nota_segundo_semestre": fields.Float(required=True, description="Nota do segundo semestre"),
    "turma_id": fields.Integer(required=True, description="ID da turma associada"),
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