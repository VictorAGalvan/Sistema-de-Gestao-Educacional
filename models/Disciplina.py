

from datetime import date

#from models.Avaliacao import Avaliacao
#from models.Aluno import Aluno
#from models.Calculos import Calculo
#from models.Matricula import Matricula

class Disciplina:
    def __init__(self, nome: str, professor, avaliacoes: list, calculo:Calculo):
        self.nome = nome
        self.professor = professor
        self.avaliacoes = avaliacoes
        self.calculo = calculo
        
    @property
    def calculo(self) -> Calculo:
        return self.__calculo

    @calculo.setter
    def calculo(self, nova: Calculo):
        self.__calculo = nova
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        self.__nome = novo_nome

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, novo_professor):
        self.__professor = novo_professor


    @property
    def avaliacoes(self):
        return self.__avaliacoes

    @avaliacoes.setter
    def avaliacoes(self, novas_avaliacoes: list):
        self.__avaliacoes = novas_avaliacoes

    
    def adicionar_avaliacao(self,avaliacao:Avaliacao) -> bool:
        if not avaliacao in self.avaliacoes:
            self.__avaliacoes.append(avaliacao)
            return True
        else:
            print("Avaliação já existe e não pode ser adicionada")
            return False
    def get_media_turma(self) -> float:
        soma =0
        cont = 0
        for a in self.avaliacoes:
            for p in a.prova:
                cont += 1
                soma += p.nota
        return soma/cont
    def get_avaliacoes_aluno(self, matricula:Matricula) -> list[Avaliacao]:
        avaliacoes:list[Avaliacao] = []
        for a in self.avaliacoes:
            for p in a.prova:
                if p.matricula == matricula:
                    avaliacoes.append(a)
        return avaliacoes
    def __eq__(self, other):
        return self.__nome == other.__nome and self.__professor == other.__professor

    def __hash__(self):
        return hash(self.__nome)

    def __str__(self):
        prof_nome = ""
        if self.__professor != None:
            prof_nome = self.__professor.nome
        else:
            prof_nome = "Sem professor"
        return (
            f"Disciplina: {self.__nome} | "
            f"Professor: {prof_nome} | "
            f"Avaliações: {len(self.__avaliacoes)}"
        )