from models import Empresa, Vaga

SQL_DELETA_VAGA = 'delete from tbl_vaga where id = %i'
SQL_VAGA_POR_ID = 'SELECT idVaga,tituloVaga, descricao, cargaHoraria,salario,beneficio from tbl_vaga where idVaga = %s'
SQL_EMPRESA_POR_ID = 'SELECT idEmpresa, razaoSocial, cpfCnpj, emailContato, nomeFantasia, inscricaoEstadual, cidadeEmpresa,usuario, senha from empresa where usuario = %s'
SQL_ATUALIZA_VAGA = 'UPDATE tbl_vaga SET tituloVaga=%s, descricao=%s, cargaHoraria=%s, salario=%s, beneficio=%s where id = %s'
SQL_BUSCA_VAGAS = 'SELECT idVaga, tituloVaga, descricao, cargaHoraria, salario, beneficio from tbl_vaga'
SQL_CRIA_VAGA = 'INSERT into tbl_vaga (idEmpresa, cidadeempresa, tituloVaga, descricao, cargaHoraria,salario,beneficio) values (%s, %s, %s, %s, %s)'
SQL_CRIA_EMPRESA = 'INSERT into empresa (idEmpresa, razaoSocial, cpfCnpj, emailContato,  cidadeEmpresa,usuario, senha) values (%s, %s, %s, %s, %s,%s, %s)'
SQL_ATUALIZA_EMPRESA = 'UPDATE empresa SET razaoSocial=%s, cpfCnpj=%s, emailContato=%s,  cidadeEmpresa=%s,usuario=%s, senha=%s where id = %s'

class VagaDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, tbl_vaga):
        cursor = self.__db.connection.cursor()

        if (tbl_vaga.id):
            cursor.execute(SQL_ATUALIZA_VAGA, ( tbl_vaga.idVaga,tbl_vaga.tituloVaga, tbl_vaga.descricao, tbl_vaga.cargaHoraria, tbl_vaga.salario, tbl_vaga.beneficio))
        else:

            cursor.execute(SQL_CRIA_VAGA, (tbl_vaga.tituloVaga, tbl_vaga.descricao, tbl_vaga.cargaHoraria, tbl_vaga.salario, tbl_vaga.beneficio))
            tbl_vaga.idVaga= cursor.lastrowid
        self.__db.connection.commit()
        return tbl_vaga

    def listar(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_BUSCA_VAGAS)
        vagas = traduz_vagas(cursor.fetchall())
        return vagas

    def busca_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_VAGA_POR_ID, (id,))
        tupla = cursor.fetchone()
        return Vaga(tupla[1], tupla[1], tupla[1],tupla[2] ,tupla[3], tupla[4],tupla[5], id=tupla[0])

    def deletar(self, id):
        self.__db.connection.cursor().execute(SQL_DELETA_VAGA, (id, ))
        self.__db.connection.commit()


class EmpresaDao:
    def __init__(self, db):
        self.__db = db

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_EMPRESA_POR_ID, (id,))
        dados = cursor.fetchone()
        empresa = traduz_empresa(dados) if dados else None
        return empresa

    def salvar(self, empresa):
        cursor = self.__db.connection.cursor()

        if (empresa.id):
            cursor.execute(SQL_ATUALIZA_EMPRESA, (empresa.razaosocial, empresa.cpfcnpj, empresa.emailcontato, empresa.cidadeempresa, empresa.usuario,  empresa.senha, empresa.idEmpresa))
        else:
            cursor.execute(SQL_CRIA_EMPRESA, (empresa.razaosocial, empresa.cpfcnpj, empresa.emailcontato, empresa.cidadeempresa, empresa.usuario,  empresa.senha))
            empresa.idEmpresa= cursor.lastrowid
        self.__db.connection.commit()
        return empresa


def traduz_vagas(vagas):
    def cria_vaga_com_tupla(tupla):
        return Vaga(tupla[1], tupla[1], tupla[1],tupla[2] ,tupla[3], tupla[4],tupla[5], id=tupla[0])
    return list(map(cria_vaga_com_tupla, vagas))


def traduz_empresa(tupla):
    return Empresa( tupla[1],tupla[2] ,tupla[3], tupla[4],tupla[5],tupla[6],tupla[7],tupla[8])