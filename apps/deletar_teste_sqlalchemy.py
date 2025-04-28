from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Teste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    

print("SQLAlchemy parece estar funcionando!")