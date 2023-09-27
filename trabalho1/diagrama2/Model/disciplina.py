from Model.turma import Turma
from Model.curso import Curso

class Disciplina:

    def __init__(self) -> None:
        self.__id = 1
        self.__descricao = ""
        self.__listaTurma = []
        self.__listaCurso = []

    def setId(self, id: int) -> None:
        self.__id = id

    def getId(self) -> int:
        return self.__id
    
    def setDescricao(self, descricao: str) -> None:
        self.__descricao = descricao

    def getDescricao(self) -> str:
        return self.__descricao
    
    def setListaTurma(self, turma) -> None:
        self.__listaTurma = turma

    def addListaTurma(self, turma) -> None:
        self.__listaTurma.append(turma)

    def removerListaTurma(self, turma) -> None:
        self.__listaTurma.remove(turma)

    def getListaTurma(self) -> None:
        return self.__listaTurma
    
    def setListaCurso(self, Curso) -> None:
        self.__listaCurso = Curso

    def addListaCurso(self, curso) -> None:
        self.__listaCurso.append(curso)

    def removerListaCurso(self, curso) -> None:
        self.__listaCurso.remove(curso)

    def getListaCurso(self) -> None:
        return self.__listaCurso
    
