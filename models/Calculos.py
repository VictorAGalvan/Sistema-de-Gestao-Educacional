
from abc import abstractmethod, ABC

#from models.Disciplina import Disciplina
#from models.Matricula import Matricula


class Calculo(ABC):
    @abstractmethod
    def calcular(self, disciplina: Disciplina, matricula: Matricula) -> float:
        pass

class Somatorio(Calculo):
    def calcular(self, disciplina: Disciplina, matricula: Matricula) -> float:
        soma_pesos = 0.0
        soma_notas = 0.0
        for avaliacao in disciplina.avaliacoes:
            for prova in avaliacao.prova:
                if prova.matricula == matricula:
                    soma_notas += prova.nota * avaliacao.peso
                    soma_pesos += avaliacao.peso
        if soma_pesos == 0:
            return 0.0
        return soma_notas

class MediaPonderada(Calculo):
    def calcular(self, disciplina: Disciplina, matricula: Matricula) -> float:
        soma_pesos = 0.0
        soma_notas = 0.0
        for avaliacao in disciplina.avaliacoes:
            for prova in avaliacao.prova:
                if prova.matricula == matricula:
                    soma_notas += prova.nota * avaliacao.peso
                    soma_pesos += avaliacao.peso
        if soma_pesos == 0:
            return 0.0
        return soma_notas / soma_pesos
 