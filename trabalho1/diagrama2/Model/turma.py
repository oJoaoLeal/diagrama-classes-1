class Turma:

    def __init__(self) -> None:
        self.__id = 1
        self.__descricao = 1
        self.__ano = 1
        self.__semestre = 1
        self.__instituicao = ""
        self.__disciplina = ""
        self.__professor = ""
        self.__listaDiario = []

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
    
    def setInstituicao(self, instituicao) -> None:
        self.__instituicao = instituicao

    def getInstituicao(self) -> None:
        return self.__instituicao
    
    def setDisciplina(self, disciplina) -> None:
        self.__disciplina = disciplina

    def getDisciplina(self) -> None:
        return self.__disciplina
    
    def setProfessor(self, professor) -> None:
        self.__professor = professor

    def getProfessor(self) -> None:
        return self.__professor
    
    def setListaDiario(self, diario) -> None:
        self.__listaDiario = diario

    def addListaDiario(self, diario) -> None:
        self.__listaDiario.append(diario)

    def removerListaDiario(self, diario) -> None:
        self.__listaDiario.remove(diario)

    def getListaDiario(self) -> None:
        return self.__listaDiario
    
    def __str__(self) -> None:
        return f"ID: {self.getId()}\nDescrição: {self.getDescricao()}\n" \
               f"Ano: {self.getAno()}\nSemestre: {self.getSemestre()}\n" \
               f"Professor: {self.getProfessor()}"
    
    