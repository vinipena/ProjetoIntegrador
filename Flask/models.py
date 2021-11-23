class Empresa:
    def __init__(self,razao_social,cnpj, nome_fantasia,cidade, usuario, senha):
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.nome_fantasia = nome_fantasia
        self.cidade = cidade
        self.usuario = usuario
        self.senha = senha
 
class Vaga:
    def __init__(self, titulo, empregador, cidade, descricao_vaga, salario, beneficios, id=None ):
        self.titulo = titulo
        self.empregador = empregador
        self.cidade = cidade
        self.descricao_vaga = descricao_vaga
        self.salario = salario
        self.beneficios = beneficios