class Situacao:

    def __init__(self):
        self.__situacao = None
        self.__anoSemestre = None
        self.__listaAluno = []

    def setSituacao(self, situacao):
        self.__situacao = situacao

    def getSituacao(self):
        return self.__situacao
    
    def setAnoSemestre(self, anoSemestre):
        self.__anoSemestre = anoSemestre

    def getAnoSemestre(self):
        return self.__anoSemestre
    
    def setListaAluno(self, aluno):
        self.__listaAluno = aluno

    def addListaAluno(self, aluno):
        self.__listaAluno.append(aluno)

    def removerListaAluno(self, aluno):
        self.__listaAluno.remove(aluno)

    def getListaAluno(self):
        return self.__listaAluno
    
    def __str__(self):
        return f"Situação: {self.getSituacao()}\nAnoSemestre: {self.getAnoSemestre()}"

