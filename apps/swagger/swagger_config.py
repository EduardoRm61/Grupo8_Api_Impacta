from . import api
from apps.swagger.namespaces.aluno_namespace import alunos_ns
from apps.swagger.namespaces.prof_namespace import professor_ns
from apps.swagger.namespaces.turma_namespace import turma_ns


def configure_swagger(app):
    api.init_app(app)
    api.add_namespace(alunos_ns, path="/alunos")
    api.add_namespace(professor_ns, path="/professores")
    api.add_namespace(turma_ns, path="/turmas")
    api.mask_swagger = False