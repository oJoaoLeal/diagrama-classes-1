class Situacao:

    def __init__(self) -> None:
        self.__situacao = 1
        self.__anoSemestre = 1
        self.__listaAluno = []

    def setSituacao(self, situacao: int) -> None:
        self.__situacao = situacao

    def getSituacao(self) -> int:
        return self.__situacao
    
    def setAnoSemestre(self, anoSemestre: int) -> None:
        self.__anoSemestre = anoSemestre

    def getAnoSemestre(self) -> int:
        return self.__anoSemestre
    
    def setListaAluno(self, aluno) -> None:
        self.__listaAluno = aluno

    def addListaAluno(self, aluno) -> None:
        self.__listaAluno.append(aluno)

    def removerListaAluno(self, aluno) -> None:
        self.__listaAluno.remove(aluno)

    def getListaAluno(self) -> None:
        return self.__listaAluno
    
    def __str__(self) -> None:
        return f"Situação: {self.getSituacao()}\nAno e Semestre: {self.getAnoSemestre()}\n" \
               f"Aluno(s): {self.getListaAluno()}"