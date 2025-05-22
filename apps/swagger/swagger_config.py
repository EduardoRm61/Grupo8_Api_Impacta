from . import api
from swagger.namespace.turma_namespace import turma_ns
from swagger.namespace.aluno_namespace import alunos_ns
from swagger.namespace.professor_namespace import professor_ns
def configure_swagger(app):
    api.add_namespace(turma_ns, path="/Turma")
    api.add_namespace(alunos_ns, path="/alunos")
    api.add_namespace(professor_ns, path="/professores")
    api.mask_swagger = False