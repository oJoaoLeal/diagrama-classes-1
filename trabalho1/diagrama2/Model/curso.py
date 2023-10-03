class Curso:

    def __init__(self):
        self.__id = None
        self.__descricao = None
        self.__listaProfessor = []
        self.__listaDisciplina = []

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id
    
    def setDescricao(self, descricao):
        self.__descricao = descricao

    def getDescricao(self):
        return self.__descricao
    
    def setListaProfessor(self, professor):
        self.__listaProfessor = professor

    def addListaProfessor(self, professor):
        self.__listaProfessor.append(professor)

    def removerListaProfessor(self, professor):
        self.__listaProfessor.remove(professor)


    def getListaProfessor(self):
        return self.__listaProfessor
    
    def setListaDisciplina(self, disciplina):
        self.__listaDisciplina = disciplina

    def addListaDisciplina(self, disciplina):
        self.__listaDisciplina.append(disciplina)

    def removerListaDisciplina(self, disciplina):
        self.__listaDisciplina.remove(disciplina)

    def getListaDisciplina(self):
        return self.__listaDisciplina
    
    def __str__(self):
        return f"ID: {self.getId()}\nDescrição: {self.getDescricao()}"

