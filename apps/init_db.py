from config import app, db_serv
from turma.model_turma import Turma  # caminho relativo ao init_db.py
from professores.model_prof import Professor
from alunos.model_aluno import Aluno

with app.app_context():
    db_serv.create_all()
