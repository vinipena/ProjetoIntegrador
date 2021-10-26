from flask import Flask, render_template, url_for
app = Flask(__name__)

lista_membros =[('Vinicius','Estudando de Eng. da Computação'),
                ('Tiago','Estudante de Eng. da Comp. Prof de robotica'),
                ('Daniele','Descricao 3'),
                ('Debora','Descricao 4'),
                ('Marcio','Descricao 5'),
                ('Elizete','Descricao 6'),]
@app.route("/")
def hello_world():
    return render_template('index.html', lista_membros = lista_membros)
app.run();