import datetime

from models.Responsavel import Responsavel
from models.Pessoa import Pessoa
from models.Turma import Turma
from models.Matricula import Matricula
class Aluno(Pessoa):
    def __init__(self, nome:str, cpf:str, Data_nascimento:datetime, Pai:Responsavel, Mae:Responsavel, Responsaveis:list[Responsavel]):
        super().__init__(nome, cpf, Data_nascimento)
        self.pai = Pai
        self.mae = Mae
        self.responsaveis:list[Responsavel] = Responsaveis
        self.matriculas:list[Matricula] = []
    @property
    def matriculas(self):
        return self.__matriculas
    @matriculas.setter
    def matriculas(self, novas_matriculas:list[Matricula]):
        self.__matriculas = novas_matriculas
    @property
    def pai(self):
        return self.__pai
    @property
    def mae(self):
        return self.__mae
    @property
    def responsaveis(self):
        texto = "Vazio"
        if len(self.__responsaveis) > 0:
            texto = ""
        for r in self.__responsaveis:
            texto += r
        return texto
    @pai.setter
    def pai(self,pai:Responsavel):
        self.__pai = pai
    @mae.setter
    def mae(self, mae:Responsavel):
        self.__mae = mae
    @responsaveis.setter
    def responsaveis(self, responsaveis:list[Responsavel]):
        self.__responsaveis = responsaveis
    def add_responsaveis(self, responsavel:Responsavel):
        r = self.responsaveis
        r.append(responsavel)
        self.responsaveis =r 

    def remove_responsaveis(self, responsavel:Responsavel):
        r = self.responsaveis
        if len(r) <= 0:
            return False
        r.remove(responsavel)
        self.responsaveis=r
        return True
    def matricular(self, turma: Turma):
        turma.matricular(self)
    def _adicionar_matricula(self, matricula:Matricula):
        self.__matriculas.append(matricula)

    def _remover_matricula(self, matricula:Matricula):
        self.__matriculas.remove(matricula) 
    def __str__(self):
        nomes_resp= ""
        if len(self.__responsaveis) ==0:
            nomes_resp= "Nenhum"
        else:
            for r in self.__responsaveis:
                nomes_resp += r.nome
                if(r != self.__responsaveis[-1]):
                    nomes_resp += ", "
        pai_str = ""
        if (self.__pai !=None):
            pai_str= self.__pai.nome
        else:
            pai_str = "Não informado"
        mae_str=""
        if (self.__mae !=None):
            mae_str= self.__mae.nome
        else:
            mae_str = "Não informada"
 
        return (
            f"Aluno: {self.nome} | "
            f"CPF: {self.cpf} | "
            f"Pai: {pai_str} | "
            f"Mãe: {mae_str} | "
            f"Responsáveis: {nomes_resp} | "
            f"Matrículas: {len(self.__matriculas)}"
        )