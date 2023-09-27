class Turma:

    def __init__(self) -> None:
        self.__id = 1
        self.__descricao = 1
        self.__ano = 1
        self.__semestre = 1

    def setId(self, id: int) -> None:
        self.__id = id

    def getId(self) -> int:
        return self.__id
    
    def setDescricao(self, descricao: int) -> None:
        self.__descricao = descricao

    def getDescricao(self) -> int:
        return self.__descricao
    
    def setAno(self, ano: int) -> None:
        self.__ano = ano

    def getAno(self) -> int:
        return self.__ano

    def setSemestre(self, semestre: int) -> None:
        self.__semestre = semestre

    def getSemestre(self) -> int:
        return self.__semestre