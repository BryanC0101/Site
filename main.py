# Esse código não é para ter aparência limpa, é justamente para mim aprender como se utiliza flask
# a ideia é criar um sistema e-commerce completo, com login, produtos e perfil para treinar



from flask import Flask 

# app vai ser o representante do Flask no código
app = Flask(__name__)

# Aqui a gente diz para o python executar isso somente se esse arquivo
# for o principal
if __name__ == '__main__':
    app.run()