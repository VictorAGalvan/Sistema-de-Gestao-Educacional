from models.Pessoa import Pessoa

class Responsavel(Pessoa):
    def __init__(self, nome, cpf, Data_nascimento):
        super().__init__(nome, cpf, Data_nascimento)
        

    def exibir_dados(self):
        print(f"Responsável: {self.nome} | CPF: {self.cpf} | Idade: {Pessoa.calcular_idade(self)}")
    def __str__(self):
        return f"Responsável: {self.nome} | CPF: {self.cpf} | Idade: {Pessoa.calcular_idade(self)}"