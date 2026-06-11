from datetime import date

from models.Matricula import Matricula
#from models.Grade import Grade


class Turma():
    def __init__(self, sala:str,quantidade:int, alunos:list[Matricula], grade:Grade):
        self.sala = sala
        self.quantidade = quantidade
        self.alunos = alunos
        self.grade = grade
    @property
    def sala(self):
        return self.__sala

    @sala.setter
    def sala(self, sala):
        self.__sala = sala

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def alunos(self):
        return self.__alunos

    @alunos.setter
    def alunos(self, alunos):
        self.__alunos = alunos

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade
    
    def _adicionar_matricula(self, matricula):
        self.__alunos.append(matricula)

    def remover_matricula(self, matricula:Matricula):
        matricula.aluno._remover_matricula(matricula)
        self.__alunos.remove(matricula) 
       
    def matricular(self, aluno):
        if(self.esta_cheia()):
            return
        
        m = Matricula(aluno=aluno, turma=self, data=date.today(), codigo=str(date.today().year) + " CC-01") # n gero o código
        self.__alunos.append(m)
        aluno._adicionar_matricula(m) 
        return m
    def esta_cheia(self) ->bool:
        if (len(self.alunos)< self.quantidade):
            return False
        return True
    def __eq__(self, other):
        return self.__sala == other.__sala and self.__grade == other.__grade

    def __str__(self):
        return (
            f"Turma | Sala: {self.__sala} | "
            f"Alunos: {len(self.__alunos)}/{self.__quantidade} | "

        )
