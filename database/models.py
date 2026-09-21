from database import database

class Usuario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    id_telegram = database.Column(database.Integer, unique=True)
    nome = database.Column(database.String)
    cpf = database.Column(database.Integer)
