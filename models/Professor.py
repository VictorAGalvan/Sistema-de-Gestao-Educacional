from datetime import date

from models.Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome:str, cpf:str, Data_nascimento:date, formacao:str):
        super().__init__(nome, cpf, Data_nascimento)
        self.formacao = formacao
    @property
    def formacao(self):
        return self.__formacao
    @formacao.setter
    def formacao(self,formacao):
        self.__formacao = formacao
    def __str__(self):
        return (
            f"Professor: {self.nome} | "
            f"CPF: {self.cpf} | "
            f"Idade: {Pessoa.calcular_idade(self)} | "
            f"Formação: {self.formacao}"
        )
    def exibir_dados(self):
        print(f"Professor: {self.nome} | CPF: {self.cpf} | Idade: {Pessoa.calcular_idade(self)} | Formação: {self.formacao}")