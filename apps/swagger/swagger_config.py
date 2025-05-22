from . import api
from swagger.namespace.turma_namespace import turma_ns

def configure_swagger(app):
    api.add_namespace(turma_ns, path="/Turma")
    api.mask_swagger = False