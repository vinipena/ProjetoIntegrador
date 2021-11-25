class Empresa:
    def __init__(self,razao_social,cnpj,e_mail, nome_fantasia,insc_estadual,cidade, usuario, senha, id=None):
        self.id = id
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.e_mail=e_mail
        self.nome_fantasia = nome_fantasia
        self.insc_estadual =insc_estadual
        self.cidade = cidade
        self.usuario = usuario
        self.senha = senha
 
class Vaga:
    def __init__(self, empregador, cidade, tituloVaga,descricao, cargaHoraria, salario, beneficio, id=None ):
        self.id =id
        self.empregador = empregador
        self.cidade = cidade
        self.tituloVaga = tituloVaga
        self.descricao = descricao
        self.cargaHoraria = cargaHoraria
        self.salario = salario
        self.beneficio = beneficio