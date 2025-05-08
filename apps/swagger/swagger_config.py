from . import api
from apps.swagger.namespaces.aluno_namespace import alunos_ns
from apps.swagger.namespaces.prof_namespace import professor_ns
from apps.swagger.namespaces.turma_namespace import turma_ns


def configure_swagger(app):
    api.init_app(app)
<<<<<<< HEAD
    api.add_namespace(alunos_ns, path="/alunos") 
    #api.add_namespace(professores_ns, path="/professores")
    #api.add_namespace(turmas_ns, path="/turmas")
=======
    api.add_namespace(alunos_ns, path="/alunos")
    api.add_namespace(professor_ns, path="/professores")
    api.add_namespace(turma_ns, path="/Turmas")
>>>>>>> 4c368fd7c5d23faba1a3cdc4434ea1e5a189c634
    api.mask_swagger = False