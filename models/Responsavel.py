from models.Pessoa import Pessoa

class Responsavel(Pessoa):
    def __init__(self, nome, cpf, Data_nascimento):
        super().__init__(nome, cpf, Data_nascimento)
        

    def exibir_dados(self):
        print("Responsável: {self.nome} | CPF: {self.cpf}")
    def __str__(self):
        return f"Responsável: {self.nome} | CPF: {self.cpf}"