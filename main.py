# Esse código não é para ter aparência limpa, é justamente para mim aprender como se utiliza flask
# a ideia é criar um sistema e-commerce completo, com login, produtos e perfil para treinar



from flask import Flask, render_template, request, redirect, url_for
# render_template -> mostra HTML
# request -> pega dados do formulário
# redirect -> redireciona para outra rota
# url_for -> gera URL de uma rota
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from db import db
from models import Usuario
import hashlib # para criptografar coisas

# app vai ser o representante do Flask no código
app = Flask(__name__)
app.secret_key = 'LongaMarcha10' # Aqui o melhor é usar um dotenv para esconder melhor a chave
lm = LoginManager(app) # aqui o app serve de parametro para o LoginManager gerenciar
# aqui o banco de dados sqlite será criado e o config procurará o arquivo database.db
# se ele não existir, ele automaticamente o criará
lm.login_view = 'login' # Aqui diz que se o usuário não estivar logado, ele redireciona para login
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
db.init_app(app) # conectando banco ao Flask

def hash(txt):
    hash_obj = hashlib.sha256(txt.encode('utf-8'))
    return hash_obj.hexdigest()

@lm.user_loader # carrega usuário logado pelo id
def user_loader(id):
    usuario = db.session.query(Usuario).filter_by(id=id).first()
    return usuario

@app.route('/')
@login_required
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        senha = request.form['senhaForm']

        user = db.session.query(Usuario).filter_by(nome=nome, senha=hash(senha)).first()
        if not user:
            return 'Nome ou senha incorretos'

        login_user(user)
        return redirect(url_for('home'))

@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        senha = request.form['senhaForm']

        novo_usuario = Usuario(nome=nome, senha=hash(senha))
        db.session.add(novo_usuario)
        db.session.commit()

        login_user(novo_usuario)

        return redirect(url_for('home'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
# Aqui a gente diz para o python executar isso somente se esse arquivo for o principal
# O "debug=True" apeans ativa uma funcionalidade de auxílio ao dev caso haja bugs no código.
# Ao que parece, ao lançar o projeto para o público, o certo é tirar o debug. 
if __name__ == '__main__':
    with app.app_context(): # OBRIGATÓRIO: isso aqui é um indicativo para o SQLAlchemy saber qual app, banco e configuração rodar
        db.create_all() # aqui ele cria todas as tabelas no banco de dados
    app.run(debug=True)
