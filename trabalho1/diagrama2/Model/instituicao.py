from Model.turma import Turma

class Instituicao:

    def __init__(self) -> None:
        self.__id = 1
        self.__descricao = ""
        self.__listaTurma = []

    def setId(self, id: int) -> None:
        self.__id = id

    def getId(self) -> int:
        return self.__id
    
    def setDescricao(self, descricao: str) -> None:
        self.__descricao = descricao

    def getDescricao(self) -> str:
        return self.__descricao
    
    def setListaTurma(self, turma: Turma()) -> None:
        self.__listaTurma = turma

    def addListaTurma(self, turma: Turma()) -> None:
        self.__listaTurma.append(turma)

    def removerListaTurma(self, turma: Turma()) -> None:
        self.__listaTurma.remove(turma)

    def getListaTurma(self) -> None:
        return self.__listaTurma