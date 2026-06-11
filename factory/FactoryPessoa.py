from datetime import date

from models.Professor import Professor
from models.Responsavel import Responsavel
from models.Aluno import Aluno


class FactoryPessoa():
    @staticmethod
    def criar_pessoa(tipo_pessoa:str,nome:str, cpf:str,Dtnascimento:date, **kwargs):
        pessoa = None
        if(tipo_pessoa == "aluno"):
            pessoa = Aluno(nome,cpf,Dtnascimento,kwargs.get("Pai"),kwargs.get("Mãe"), kwargs.get("Responsaveis"))
        elif tipo_pessoa == "responsavel": 
            pessoa = Responsavel(nome,cpf,Dtnascimento)
        elif tipo_pessoa == "professor":
            pessoa = Professor(nome,cpf,Dtnascimento, kwargs.get("formacao"))
        return pessoa

