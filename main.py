# Esse código não é para ter aparência limpa, é justamente para mim aprender como se utiliza flask
# a ideia é criar um sistema e-commerce completo, com login, produtos e perfil para treinar



from flask import Flask 

# app vai ser o representante do Flask no código
app = Flask(__name__)


# aqui se estabelece a rota principal, ou seha, a home.
# o "index" é uma função de resposta da rota, que retornará a mensagem "Olá, Mundo!".
@app.route('/')
def index():
    return 'Olá, Mundo!'

# Aqui a gente diz para o python executar isso somente se esse arquivo for o principal
# O "debug=True" apeans ativa uma funcionalidade de auxílio ao dev caso haja bugs no código.
# Ao que parece, ao lançar o projeto para o público, o certo é tirar o debug. 
if __name__ == '__main__':
    app.run(debug=True)
