from flask import Flask, render_template, request, session, flash, redirect, url_for
from dao import VagaDao, EmpresaDao
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
empresa_dao =EmpresaDao(db)

@app.route('/')
def index():
    if session['usuario_logado']:
        mostra_botao = 'none'
    else:
        mostra_botao='inline'
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
    empregador = session.get('empresa')
    cidade = session.get('cidade')
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
    usuario = empresa_dao.buscar_por_id(request.form['usuario'])
    if usuario:
       if usuario.senha == request.form['senha']:
            session['usuario_logado'] =  usuario.usuario
            session['empresa'] = usuario.razao_social
            session['cidade_empresa'] =usuario.cidade
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
    empresa_dao.salvar(empresa)
    return redirect(url_for('index'))

@app.route('/vaga_view/<int:id>')
def vaga_view(id):
    vaga=vagas_dao.busca_por_id(id)
    return render_template('vaga_view.html', vaga=vaga)

app.run(debug=True)
