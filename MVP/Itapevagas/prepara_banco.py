from flask_mysqldb import MySQLdb
print('Conectando...')
conn = MySQLdb.connect(user='root', passwd='d29m1192', host='127.0.0.1', port=3306)

# Descomente se quiser desfazer o banco...
conn.cursor().execute("DROP DATABASE `itapevagas`;")
conn.commit()

criar_tabelas = '''SET NAMES utf8;
    CREATE DATABASE `itapevagas` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `itapevagas`;
    CREATE TABLE `tbl_vaga` (
    `idvaga` int NOT NULL AUTO_INCREMENT,
    `idempresa` int COLLATE utf8_bin NULL,
    `cidadeempresa` varchar(45) COLLATE utf8_bin NULL,
    `tituloVaga` varchar(45) COLLATE utf8_bin NOT NULL,
    `descricao` varchar(45) DEFAULT NULL,
    `cargaHoraria` varchar(20)  NULL,
    `salario` varchar(40) COLLATE utf8_bin NOT NULL,
    `beneficio` varchar(45) DEFAULT NULL,
    PRIMARY KEY (`idVaga`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
    CREATE TABLE `empresa` (
    `idEmpresa` int(11) NOT NULL AUTO_INCREMENT,
    `razaosocial` varchar(50) COLLATE utf8_bin NOT NULL,
    `cpfcnpj` varchar(20)COLLATE utf8_bin NOT NULL,
    `emailcontato` varchar(50) COLLATE utf8_bin NOT NULL,
    `nomefantasia` varchar(20)COLLATE utf8_bin  NULL,
    `inscricaoestadual` varchar(40) COLLATE utf8_bin  NULL,
    `cidadeempresa` varchar(45) COLLATE utf8_bin NOT NULL,
    `usuario` varchar(45) COLLATE utf8_bin NOT NULL,
    `senha` varchar(45) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`idEmpresa`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabelas)

# inserindo usuarios
cursor = conn.cursor()
cursor.execute(
      'INSERT INTO itapevagas.empresa (idEmpresa, razaoSocial, cpfCnpj, emailContato, nomeFantasia, inscricaoEstadual, cidadeEmpresa,usuario, senha)'
      ' VALUES ( %s, %s, %s, %s,%s, %s, %s,%s,%s)',
      (1, 'empresa Y', 1234, 'empresay@empresay.com','Ycompany',1223, 'Itapevi-SP','empresay','empresay')
      )

cursor.execute('select * from itapevagas.empresa')
print(' -------------  Empresas:  -------------')
for empresas in cursor.fetchall():
    print(empresas[1])

# inserindo jogos
cursor.execute(
      'INSERT INTO itapevagas.tbl_vaga (idVaga, idEmpresa, cidadeEmpresa,tituloVaga, descricao, cargaHoraria,salario,beneficio)'
      'VALUES (%s,  %s,  %s, %s,%s, %s, %s, %s)',
      (1, 1, 'Itapevi-SP', ' Auxiliar de Escritório', 'Auxiliar na rotina administrativa', '40h semanais','1500','VT e VR' ),
      )

cursor.execute('select * from itapevagas.tbl_vaga')
print(' -------------  Vagas:  -------------')
for vaga in cursor.fetchall():
    print(vaga[1])

# commitando senão nada tem efeito
conn.commit()
cursor.close()