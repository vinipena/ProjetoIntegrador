from flask import Flask, render_template, request, session, flash, redirect, url_for
from dao import VagaDao
from models import Empresa, Vaga
from flask_mysqldb import MySQL

app = Flask('__name__')
app.secret_key ='itapevagas'
app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "d29m1192"
app.config['MYSQL_DB'] = "itapevagas"
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)

vagas_dao = VagaDao(db)

empresa1 = Empresa('Empresa X','0001','X Company','Itapevi','empresax','empresax')


usuarios = {empresa1.usuario: empresa1,}

@app.route('/')
def index():
    lista_vagas = vagas_dao.listar()
    return render_template('index.html', titulo='Itapevagas', vagas=lista_vagas)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
       #query string que redireciona após login para a rota de "novo.html" 
       return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Nova vaga' )

@app.route('/criar', methods=['POST',])
def criar():
    titulo = request.form['titulo_vaga']
    empregador = usuarios.get(empresa1.razao_social)
    cidade = usuarios.get(empresa1.cidade)
    salario = request.form['salario']
    beneficios = request.form['beneficios']
    descricao_vaga = request.form['descricao_vaga']
    carga_horaria = request.form['carga_horaria']
    vaga = Vaga(empregador,cidade,titulo, descricao_vaga,carga_horaria, salario, beneficios,)
    #lista_vagas.append(vaga)
    vagas_dao.salvar(vaga)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima  )

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] =  usuario.usuario
            flash(usuario.razao_social + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)

    else :
        flash('Não logado, tente de novo!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado')
    return redirect(url_for('index'))

@app.route('/novo_usuario')
def novo_usuario():
    return render_template('novo_usuario.html', titulo='Nova Empresa' )

@app.route('/criar_empresa', methods=['POST',])
def criar_empresa():
    razao_social = request.form['razao_social']
    cnpj = request.form['cnpj']
    cidade = request.form['cidade']
    nome_fantasia = request.form['nome_fantasia']
    usuario = request.form['usuario']
    senha = request.form['senha']
    empresa = Empresa(razao_social, cnpj, nome_fantasia, cidade, usuario, senha,)
    lista_usuarios.append({empresa.usuario, empresa})
    usuarios = dict(lista_usuarios)
    return redirect(url_for('index'))

app.run(debug=True)
