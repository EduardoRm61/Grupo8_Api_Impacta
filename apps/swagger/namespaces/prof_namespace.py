from flask_restx import Namespace, Resource, fields
from professores.model_prof import criar_novo_professor, alterar_informacoes_professor, deletar_professor_por_id

professor_ns = Namespace("professores", description="Operações relacionadas aos professores")

professor_model = professor_ns.model("Professor", {
    "nome": fields.String(required=True, description="Nome do Professor"),
    "idade": fields.String(required=True, description="Idade do Professor"),
    "materia": fields.Float(required=True, description="Materia"),
    "obs": fields.Integer(required=True, description="Colocar alguma observação adicional"),
})

professor_output_model = professor_ns.model("ProfessrorOutput", {
    "id": fields.Integer(description="ID do Professor"),
    "nome": fields.String(description="Nome do professor"),
    "idade": fields.Integer(description="Idade do aluno"),
    "materia": fields.Float(description="Materia que o professor leciona"),
    "obs": fields.Integer(description="Colocar alguma observação adicional"),
})



    @professor_ns.expect(professor_model)
    def post(self):
        """Cria um novo professor"""
        data = professor_ns.payload
        response, status_code = criar_novo_professor(data)
        return response, status_code



    @professor_ns.expect(professor_model)
    def put(self, id_professor):
        """Atualiza um professor pelo ID"""
        data = professor_ns.payload
        alterar_informacoes_professor(id_professor, data)
        return data, 200

    def delete(self, id_professor):
        """Exclui um professor pelo ID"""
        deletar_professor_por_id(id_professor)
        return {"message": "Professor deletado com sucesso"}, 200