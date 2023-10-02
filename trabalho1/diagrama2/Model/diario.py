class Diario:

    def __init__(self) -> None:
        self.__v1 = 1
        self.__v2 = 1
        self.__vS = 1
        self.__vT = 1
        self.__faltas = 1
        self.__aluno = ""
        self.__turma = ""

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
    
    def setAluno(self, aluno) -> None:
        self.__aluno = aluno

    def getAluno(self) -> None:
        return self.__aluno
    
    def setTurma(self, turma) -> None:
        self.__turma = turma

    def getTurma(self) -> None:
        return self.__turma
    
    def __str__(self) -> None:
        return f"V1: {self.getV1()}\nV2: {self.getV2()}\n" \
               f"VS: {self.getVS()}\nVT: {self.getVT()}\n" \
               f"Faltas: {self.getFaltas()}\nAluno: {self.getAluno()}\n" \
               f"Turma: {self.getTurma()}"

    
