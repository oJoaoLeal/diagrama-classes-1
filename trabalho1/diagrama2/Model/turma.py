class Turma:

    def __init__(self):
        self.__id = None
        self.__descricao = None
        self.__ano = None
        self.__semestre = None
        self.__instituicao = None
        self.__disciplina = None
        self.__professor = None
        self.__listaDiario = []

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id
    
    def setDescricao(self, descricao):
        self.__descricao = descricao

    def getDescricao(self):
        return self.__descricao
    
    def setAno(self, ano):
        self.__ano = ano

    def getAno(self):
        return self.__ano

    def setSemestre(self, semestre):
        self.__semestre = semestre

    def getSemestre(self):
        return self.__semestre
    
    def setInstituicao(self, instituicao):
        self.__instituicao = instituicao

    def getInstituicao(self):
        return self.__instituicao
    
    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina

    def getDisciplina(self):
        return self.__disciplina
    
    def setProfessor(self, professor):
        self.__professor = professor

    def getProfessor(self):
        return self.__professor
    
    def setListaDiario(self, diario):
        self.__listaDiario = diario

    def addListaDiario(self, diario):
        self.__listaDiario.append(diario)

    def removerListaDiario(self, diario):
        self.__listaDiario.remove(diario)

    def getListaDiario(self):
        return self.__listaDiario
    
    def __str__(self):
        return f"ID: {self.getId()}\nDescrição: {self.getDescricao()}\n" \
               f"Ano: {self.getAno()}\nSemestre: {self.getSemestre()}"
    
    