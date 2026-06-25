#from models.Disciplina import Disciplina


class Grade():
    def __init__(self, competencias:int, disciplinas:list[Disciplina]):
        self.disciplinas: list[Disciplina] = disciplinas
        self.competencias = competencias
    @property
    def disciplinas(self):
        return self.__disciplinas
    @disciplinas.setter
    def disciplinas(self, discplinas):
        self.__disciplinas = discplinas 
    @property
    def competencias(self):
        return self.__competencias
    @competencias.setter
    def competencias(self, outro):
        self.__competencias = outro 
    def adicionar_disciplina(self,disciplina:Disciplina):
        d = self.disciplinas
        d.append(disciplina)
        self.disciplinas = d
    def remover_disciplina(self,disciplina:Disciplina):
        d = self.disciplinas
        d.remove(disciplina)
        self.disciplinas = d
    def __eq__(self, other):
        return self.__competencias == other.__competencias and self.__disciplinas == other.__disciplinas

    def __str__(self):
        nomes = ""
        if(len(self.__disciplinas) == 0 ):
            nomes ="Nenhuma"
        else:
            for d in self.__disciplinas:
                nomes += d.nome
                if(d != self.__disciplinas[-1]):
                    nomes += ", "
        return ( 
            f"Grade | Disciplinas ({len(self.__disciplinas)}): {nomes}"
        )