# Aqui o arquivo models.py será utilizado como tabela para o banco de dados
# Também é usado pela organização e facilitação de manutenção

from db import db
from flask_login import UserMixin # adiciona funções de login ao usuário

class Usuario(UserMixin, db.Model): # Aqui se cria o model (tabela) com o nome da classe Usuário 
    __tablename__ = 'usuarios' # Aqui é a definição real do nome da tablea: "usuarios"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(30), unique=True)
    senha = db.Column(db.String())
