class Diario:

    def __init__(self):
        self.__v1 = None
        self.__v2 = None
        self.__vS = None
        self.__vT = None
        self.__faltas = None
        self.__aluno = None
        self.__turma = None

    def setV1(self, v1) :
        self.__v1 = v1

    def getV1(self):
        return self.__v1
    
    def setV2(self, v2):
        self.__v2 = v2

    def getV2(self):
        return self.__v2
    
    def setVS(self, vS):
        self.__vS = vS
    
    def getVS(self):
        return self.__vS
    
    def setVT(self, vT):
        self.__vT = vT

    def getVT(self):
        return self.__vT
    
    def setFaltas(self, faltas):
        self.__faltas = faltas

    def getFaltas(self):
        return self.__faltas
    
    def setAluno(self, aluno):
        self.__aluno = aluno


    def getAluno(self):
        return self.__aluno
    
    def setTurma(self, turma):
        self.__turma = turma

    def getTurma(self):
        return self.__turma
    
    def __str__(self):
        return f"V1: {self.getV1()}\nV2: {self.getV2()}\n" \
               f"VS: {self.getVS()}\nVT: {self.getVT()}\n" \
               f"Faltas: {self.getFaltas()}"

    
