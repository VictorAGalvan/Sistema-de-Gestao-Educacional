
#from models.Avaliacao import Avaliacao

class Prova():
    def __init__(self, matricula:Matricula, avaliacao:Avaliacao, nota:float):
        self.__avaliacao = avaliacao
        self.__matricula =matricula
        self.__nota = nota

    @property
    def avaliacao(self):
        return self.__avaliacao
    @avaliacao.setter
    def avaliacao(self, nova_avaliacao):
        self.__avaliacao = nova_avaliacao
    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula


    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        self.__nota = nota      
    def __eq__(self, other):
        return self.__matricula == other.__matricula and self.__avaliacao == other.__avaliacao

    def __str__(self):

        return (
            f"Prova | Aluno: {self.__matricula.aluno.nome} | "
            f"Nota: {self.__nota:.1f}"
        )