class Instituicao:

    def __init__(self):
        self.__id = None
        self.__descricao = None
        self.__listaTurma = []

    def setId(self, id) :
        self.__id = id

    def getId(self):
        return self.__id
    
    def setDescricao(self, descricao):
        self.__descricao = descricao

    def getDescricao(self):
        return self.__descricao
    
    def setListaTurma(self, turma):
        self.__listaTurma = turma

    def addListaTurma(self, turma):
        self.__listaTurma.append(turma)

    def removerListaTurma(self, turma):
        self.__listaTurma.remove(turma)

    def getListaTurma(self):
        return self.__listaTurma
    
    def __str__(self):
        return f"ID: {self.getId()}\nDescrição: {self.getDescricao()}"

