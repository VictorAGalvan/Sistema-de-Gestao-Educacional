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
        self.__cpf = cpf
        
    @Dtnascimento.setter
    def Dtnascimento(self, novo_Dtnascimento:date):
        self.__Dtnascimento = novo_Dtnascimento
    def calcular_idade(self):
        idade =0
        hoje = date.today()
        ano = self.Dtnasicmento.year
        mes = self.Dtnasicmento.month
        dia = self.Dtnasicmento.day
        idade = hoje.year - ano
        if(dia<hoje.day and mes <hoje.month):
            idade -=1
        return idade

    def validar_cpf(self, cpf:str):
        cpf = cpf.replace(".", "").replace("-", "")
        if len(cpf) != 11:
            return False
        if not cpf.isdigit():
            return False
        soma =0
        for i in range(9):
            soma += int(cpf[i]) *(10-i)
        digito1 = (soma*10)%11
        if digito1 == 10:
            digito1 = 0
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) *(11-i)
        digito2 = (soma*10)%11
        if digito2 == 10:
            digito2 = 0
        igual = True
        for i in range(11):
            if cpf[0] != cpf[i]:
                igual = False
                break
        if (digito1 == int(cpf[9])) and digito2 == int(cpf[10]) and igual:
            return True
        else:
            return False
