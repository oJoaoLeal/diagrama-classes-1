from Model.professor import Professor
from Model.disciplina import Disciplina

class Curso:

    def __init__(self) -> None:
        self.__professor = Professor()
        self.__id = 1
        self.__descricao = ""
        self.__listaProfessor = []
        self.__listaDisciplina = []

    def setId(self, id: int) -> None:
        self.__id = id

    def getId(self) -> int:
        return self.__id
    
    def setDescricao(self, descricao: str) -> None:
        self.__descricao = descricao

    def getDescricao(self) -> str:
        return self.__descricao
    
    def setListaProfessor(self, professor: Professor()) -> None:
        self.__listaProfessor = professor

    def addListaProfessor(self, professor: Professor()) -> None:
        self.__listaProfessor.append(professor)

    def removerListaProfessor(self, professor: Professor()) -> None:
        self.__listaProfessor.remove(professor)

    def getListaProfessor(self) -> None:
        return self.__listaProfessor
    
    def setListaDisciplina(self, disciplina: Disciplina()) -> None:
        self.__listaDisciplina = disciplina

    def addListaDisciplina(self, disciplina: Disciplina()) -> None:
        self.__listaDisciplina.append(disciplina)

    def removerListaDisciplina(self, disciplina: Disciplina()) -> None:
        self.__listaDisciplina.remove(disciplina)

    def getListaDisciplina(self) -> None:
        return self.__listaDisciplina