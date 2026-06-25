from abc import ABC, abstractmethod
from datetime import date

class Pessoa(ABC):
    def __init__(self, nome:str, cpf:str, Data_nascimento:date):
        self.nome = nome
        self.cpf = cpf
        self.Dtnascimento = Data_nascimento
    @property
    def nome(self):
        return self.__nome
    @property
    def cpf(self):
        return self.__cpf
    @property
    def Dtnascimento(self):
        return self.__Dtnascimento
    @nome.setter
    def nome(self,nome:str):
        self.__nome = nome
    @cpf.setter
    def cpf(self,cpf:str):
        if (not self.validar_cpf(cpf)):
            raise Exception("Erro cpf inválido")
    
        self.__cpf = cpf
      
        
    @Dtnascimento.setter
    def Dtnascimento(self, novo_Dtnascimento:date):
        self.__Dtnascimento = novo_Dtnascimento
    def calcular_idade(self):
        idade =0
        hoje = date.today()
        ano = self.Dtnascimento.year
        mes = self.Dtnascimento.month
        dia = self.Dtnascimento.day
        idade = hoje.year - ano
        if(mes<hoje.month or  (mes == hoje.month and dia > hoje.day)):
            idade -=1
        return idade


    @staticmethod
    def validar_cpf(cpf: str): 
        cpf = cpf.replace(".", "").replace("-", "")
        if len(cpf) != 11 or not cpf.isdigit():
            return False

       
        if len(set(cpf)) == 1:
            return False

        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        digito1 = (soma * 10) % 11
        if digito1 == 10:
            digito1 = 0

        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        digito2 = (soma * 10) % 11
        if digito2 == 10:
            digito2 = 0

        return digito1 == int(cpf[9]) and digito2 == int(cpf[10])