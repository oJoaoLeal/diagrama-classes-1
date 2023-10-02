from datetime import date


class Produto:
    def __init__(self):
        self.__id = None
        self.__codigo = None
        self.__descricao = None
        self.__itensNota = []  # Associacao: recebe uma lista de "ItemNota"

    def getId(self):
        return self.__id

    def getCodigo(self):
        return self.__codigo

    def getDescricao(self):
        return self.__descricao

    def setId(self, id):
        self.__id = id

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def addNota(self, nota):
        self.__itensNota.append(nota)

    def getNotas(self):
        return self.__itensNota

    def __str__(self):
        return f"ID: {self.getId()}\nCódigo: {self.getCodigo()}\n" \
               f"Descrição: {self.getDescricao()}"
