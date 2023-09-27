from Model.pessoa import Pessoa
from Model.turma import Turma
from Model.curso import Curso

class Professor(Pessoa): # Classe Filho

    def __init__(self) -> None:
        super().__init__()
        self.__matricula = ""
        self.__titulacaoMaxima = 1
        self.__listaTurma = []
        self.__listaCurso = []

    def setMatricula(self, matricula: str) -> None:
        self.__matricula = matricula

    def getMatricula(self) -> str:
        return self.__matricula
    
    def setTitulacaoMaxima(self, titulacaoMaxima: int) -> None:
        self.__titulacaoMaxima = titulacaoMaxima

    def getTitulacaoMaxima(self) -> int:
        return self.__titulacaoMaxima
    
    def setListaTurma(self, turma: Turma()) -> None:
        self.__listaTurma = turma

    def addListaTurma(self, turma: Turma()) -> None:
        self.__listaTurma.append(turma)

    def removerListaTurma(self, turma: Turma()) -> None:
        self.__listaTurma.remove(turma)

    def getListaTurma(self) -> None:
        return self.__listaTurma
    
    def setListaCurso(self, Curso: Curso()) -> None:
        self.__listaCurso = Curso

    def addListaCurso(self, curso: Curso()) -> None:
        self.__listaCurso.append(curso)

    def removerListaCurso(self, curso: Curso()) -> None:
        self.__listaCurso.remove(curso)

    def getListaCurso(self) -> None:
        return self.__listaCurso
    