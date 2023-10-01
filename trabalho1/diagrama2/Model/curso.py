from Model.professor import Professor

class Curso:

    def __init__(self) -> None:
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
    
    def setListaProfessor(self, professor) -> None:
        self.__listaProfessor = professor

    def addListaProfessor(self, professor) -> None:
        self.__listaProfessor.append(professor)

    def removerListaProfessor(self, professor) -> None:
        self.__listaProfessor.remove(professor)

    def getListaProfessor(self) -> None:
        return self.__listaProfessor
    
    def setListaDisciplina(self, disciplina) -> None:
        self.__listaDisciplina = disciplina

    def addListaDisciplina(self, disciplina) -> None:
        self.__listaDisciplina.append(disciplina)

    def removerListaDisciplina(self, disciplina) -> None:
        self.__listaDisciplina.remove(disciplina)

    def getListaDisciplina(self) -> None:
        return self.__listaDisciplina
    
    def __str__(self) -> None:
        return f"ID: {self.getId()}\nDescrição: {self.getDescricao()}\n" \
               f"Professor(es): {self.getListaProfessor()}\nDisciplina(s): {self.getListaDisciplina()}"