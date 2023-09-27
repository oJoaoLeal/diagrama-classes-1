from Model.diario import Diario
from Model.professor import Professor
from Model.instituicao import Instituicao
from Model.disciplina import Disciplina

class Turma:

    def __init__(self) -> None:
        self.__id = 1
        self.__descricao = 1
        self.__ano = 1
        self.__semestre = 1
        self.__listaDiario = []
        self.__listaProfessor = []
        self.__listaInstituicao = []
        self.__listaDisciplina = []

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
    
    def setListaDiario(self, diario) -> None:
        self.__listaDiario = diario

    def addListaDiario(self, diario) -> None:
        self.__listaDiario.append(diario)

    def removerListaDiario(self, diario) -> None:
        self.__listaDiario.remove(diario)

    def getListaDiario(self) -> None:
        return self.__listaDiario
    
    def setListaProfessor(self, professor) -> None:
        self.__listaProfessor = professor

    def addListaProfessor(self, professor) -> None:
        self.__listaProfessor.append(professor)

    def removerListaProfessor(self, professor) -> None:
        self.__listaProfessor.remove(professor)

    def getListaProfessor(self) -> None:
        return self.__listaProfessor
    
    def setListaInstituicao(self, instituicao) -> None:
        self.__listaInstituicao = instituicao

    def addListaInstituicao(self, instituicao) -> None:
        self.__listaInstituicao.append(instituicao)

    def removerListaInstituiao(self, instituicao) -> None:
        self.__listaInstituicao.remove(instituicao)

    def getListaInstituicao(self) -> None:
        return self.__listaInstituicao
    
    def setListaDisciplina(self, disciplina) -> None:
        self.__listaDisciplina = disciplina

    def addListaDisciplina(self, disciplina) -> None:
        self.__listaDisciplina.append(disciplina)

    def removerListaDisciplina(self, disciplina) -> None:
        self.__listaDisciplina.remove(disciplina)

    def getListaDisciplina(self) -> None:
        return self.__listaDisciplina