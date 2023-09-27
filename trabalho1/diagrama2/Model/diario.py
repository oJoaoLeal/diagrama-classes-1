from Model.aluno import Aluno
from Model.turma import Turma

class Diario:

    def __init__(self) -> None:
        self.__v1 = 1.1
        self.__v2 = 1.1
        self.__vS = 1.1
        self.__vT = 1.1
        self.__faltas = 1
        self.__listaAluno = []
        self.__listaTurma = []

    def setV1(self, v1: float) -> None:
        self.__v1 = v1

    def getV1(self) -> float:
        return self.__v1
    
    def setV2(self, v2: float) -> None:
        self.__v2 = v2

    def getV2(self) -> float:
        return self.__v2
    
    def setVS(self, vS: float) -> None:
        self.__vS = vS
    
    def getVS(self) -> float:
        return self.__vS
    
    def setVT(self, vT: float) -> None:
        self.__vT = vT

    def getVT(self) -> float:
        return self.__vT
    
    def setFaltas(self, faltas: int) -> None:
        self.__faltas = faltas

    def getFaltas(self) -> int:
        return self.__faltas
    
    def setListaAluno(self, aluno) -> None:
        self.__listaAluno = aluno

    def addListaAluno(self, aluno) -> None:
        self.__listaAluno.append(aluno)

    def removerListaAluno(self, aluno) -> None:
        self.__listaAluno.remove(aluno)

    def getListaAluno(self) -> None:
        return self.__listaAluno
    
    def setListaTurma(self, turma) -> None:
        self.__listaTurma = turma

    def addListaTurma(self, turma) -> None:
        self.__listaTurma.append(turma)

    def removerListaTurma(self, turma) -> None:
        self.__listaTurma.remove(turma)

    def getListaTurma(self) -> None:
        return self.__listaTurma
    
