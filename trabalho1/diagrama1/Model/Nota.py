class Nota:
    def __init__(self):
        self.__id_nota = 0
        self.__data = ''
        self.__numero = 0
        # Cada Nota recebe uma Empresa
        self.__empresa = ''
        self.__lista_participantes = []
        self.__lista_itens_nota = []

    def setEmpresa(self, empresa):
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
        pass

    def addParticipante(self, participante):
        return self.__lista_participantes.append(participante)

    def getParticipantes(self):
        return self.__lista_participantes

    def addItensNota(self, item):
        self.__lista_itens_nota.append(item)

    def getListaItensNota(self):
        return self.__lista_itens_nota

    def __str__(self):
        return f"ID: {self.getIdNota()}\nData: {self.getData()}\n" \
               f"Número: {self.getNumero()}\nVrTotal: R${self.getVrTotal()}"
