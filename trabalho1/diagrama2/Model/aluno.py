from Model.pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self) -> None:
        super().__init__()
        self.__matricula = ""
        self.__anoInicio = 1
        self.__semestreInicio = 1
        self.__listaSituacao = []

    def setMatricula(self, matricula: str) -> None:
        self.__matricula = matricula

    def getMatricula(self) -> str:
        return self.__matricula
    
    def setAnoInicio(self, anoInicio: int) -> None:
        self.__anoInicio = anoInicio

    def getAnoInicio(self) -> int:
        return self.__anoInicio
    
    def setSemestreInicio(self, semestreInicio: int) -> None:
        self.__semestreInicio = semestreInicio

    def getSemestreInicio(self) -> int:
        return self.__semestreInicio
    
    def setListaSituacao(self, situacao) -> None:
        self.__listaSituacao = situacao

    def addListaSituacao(self, situacao) -> None:
        self.__listaSituacao.append(situacao)

    def removerListaSituacao(self, situacao) -> None:
        self.__listaSituacao.remove(situacao)

    def getListaSituacao(self) -> None:
        return self.__listaSituacao