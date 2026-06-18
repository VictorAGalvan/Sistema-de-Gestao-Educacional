from datetime import date


from models.Matricula import Matricula


class Avaliacao():
    def __init__(self, data:date, peso:int, provas:dict[Matricula,Prova]):
        self.__data = data
        self.__peso = peso
        self.__prova:dict[Matricula, Prova] = provas
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: date):
        self.__data = data
    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso: int):
        self.__peso = peso
    @property
    def prova(self):
        return self.__prova
    @prova.setter
    def prova(self, novas_provas:list[Prova]):
        self.__prova = novas_provas

    def __eq__(self, other):
        return self.__data == other.__data and self.__peso == other.__peso

    def __str__(self):
        return (
            f"Avaliação | Data: {self.__data.strftime('%d/%m/%Y')} | "
            f"Peso: {self.__peso} | "
            f"Provas: {len(self.__prova)}"
        )