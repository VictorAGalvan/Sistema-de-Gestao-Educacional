
from abc import ABC, abstractmethod




class StatusMatricula(ABC):


    def __init__(self, matricula: Matricula):
        self._matricula = matricula

    @abstractmethod
    def cancelar(self):
        pass

    @abstractmethod
    def concluir(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
    def __eq__(self, other):
        return type(self) == type(other)

class StatusAndamento(StatusMatricula):

    def cancelar(self):
        print("Matrícula cancelada.")
        self._matricula.status = StatusCancelado(self._matricula)

    def concluir(self):
        print("Matrícula concluída com sucesso.")
        self._matricula.status = StatusConcluido(self._matricula)

    def __str__(self):
        return "Em Andamento"


class StatusCancelado(StatusMatricula):
    def cancelar(self):
        print("A matrícula já está cancelada.")

    def concluir(self):
        print("Não é possível concluir uma matrícula cancelada.")

    def __str__(self):
        return "Cancelado"

class StatusConcluido(StatusMatricula):


    def cancelar(self):
        print("Não é possível cancelar uma matrícula já concluída.")

    def concluir(self):
        print("A matrícula já está concluída.")

    def __str__(self):
        return "Concluído"
