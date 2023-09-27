from .Empresa import Empresa


class Nota:
    def __init__(self):
        self.__id_nota = 0
        self.__data = ''
        self.__numero = 0
        self.__empresa = ''
        self.__lista_participantes = []
        self.__lista_itens_nota = []

    def setEmpresa(self, empresa: Empresa):
        self.__empresa = empresa

    def getEmpresa(self):
        return self.__empresa

    def getIdNota(self):
        return self.__id_nota

    def setIdNota(self, id_nota):
        self.__id_nota = id_nota

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getNumero(self):
        return self.__numero

    def setNumero(self, numero):
        self.__numero = numero

    def getVrTotal(self):
        total = 0
        for item in self.getListaItemNota():
            total += item.getVrUnitario() * item.getQuantidade()
        return total

    def addItensNota(self, item):
        self.__lista_itens_nota.append(item)

    def getListaItemNota(self):
        return self.__lista_itens_nota

    def __str__(self):
        return f"ID: {self.getIdNota()}, Data: {self.getData()}, " \
               f"Número: {self.getNumero()}, VrTotal: R${self.getVrTotal()}"
