from Model.pessoa import Pessoa

class Professor(Pessoa):

    def __init__(self) -> None:
        super().__init__()
        self.__matricula = ""
        self.__titulacaoMaxima = 1

    def setMatricula(self, matricula: str) -> None:
        self.__matricula = matricula

    def getMatricula(self) -> str:
        return self.__matricula
    
    def setTitulacaoMaxima(self, titulacaoMaxima: int) -> None:
        self.__titulacaoMaxima = titulacaoMaxima

    def getTitulacaoMaxima(self) -> int:
        return self.__titulacaoMaxima