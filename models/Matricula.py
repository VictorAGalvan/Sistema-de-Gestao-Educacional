from datetime import date

from models.Status import StatusAndamento


class Matricula():
    def __init__(self, turma:Turma, data:date, codigo:str, aluno :Aluno):
        self.turma = turma
        self.data= data
        self.codigo= codigo
        self.aluno = aluno
        self.status = StatusAndamento(self)
        self.notas_finais: dict[Disciplina, float] = {}
    @property
    def turma(self):
        return self.__turma
    @property
    def data(self):
        return self.__data
    @property
    def codigo(self):
        return self.__codigo
    @turma.setter
    def turma(self, turma:Turma):
        self.__turma = turma
    @data.setter
    def data(self, data:date):
        self.__data = data
    @codigo.setter
    def codigo(self, codigo:str):
        self.__codigo = codigo
    @property
    def aluno(self):
        return self.__aluno
    @aluno.setter
    def aluno(self, novo_aluno):
        self.__aluno = novo_aluno
    @property
    def status(self):
        return self.__status
    @property
    def notas_finais(self):
        return self.__notas_finais
    @status.setter
    def status(self,novo_status):
        self.__status = novo_status
    @notas_finais.setter
    def notas_finais(self, novo_notas_finais):
        self.__notas_finais = novo_notas_finais
    def cancelar(self):
        self.__status.cancelar()
 
    def concluir(self):
        self.__status.concluir()

    def calcular_nota_final(self, disciplina):
        nota = disciplina.calculo.calcular(disciplina, self)
        self.__notas_finais[disciplina] = nota
        return nota
    def __eq__(self, other):
        return self.__codigo == other.__codigo

    def __str__(self):
        aluno_nome = ""
        if self.__aluno is not None:
            aluno_nome = self.__aluno.nome
        
        else :
             aluno_nome = "?"
        turma_sala = ""
        if self.__turma is not None:
            turma_sala =self.__turma.sala
        else :
            turma_sala = "?"

        return (
            f"Matrícula [{self.__codigo}] | "
            f"Aluno: {aluno_nome} | "
            f"Sala: {turma_sala} | "
            f"Data: {self.__data.strftime('%d/%m/%Y')} | "
            f"Status: {self.__status}"
        )