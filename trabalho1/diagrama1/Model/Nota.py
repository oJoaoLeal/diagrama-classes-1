class Nota:
    def __init__(self):
        self.__id = None
        self.__data = None
        self.__numero = None
        self.__empresa = None  # Associacao: Nota recebe um objeto de "Empresa"
        self.__participante = None  # Associacao: Nota recebe um objeto de "Participante"
        self.__itensNota = []  # Associacao: Nota recebe uma lista de "ItemNota"

    def getId(self):
        return self.__id

    def getData(self):
        return self.__data

    def getNumero(self):
        return self.__numero

    def getEmpresa(self):
        return self.__empresa

    def getParticipante(self):
        return self.__participante

    def setId(self, id):
        self.__id = id

    def setData(self, data):
        self.__data = data

    def setNumero(self, numero):
        self.__numero = numero

    def setEmpresa(self, empresa):
        self.__empresa = empresa

    def setParticipante(self, participante):
        self.__participante = participante

    def addItensNota(self, item):
        self.__itensNota.append(item)

    def getListaItensNota(self):
        return self.__itensNota

    def getVrTotal(self):
        total = 0
        for item in self.__itensNota:
            total += item.getVrUnitario() * item.getQuantidade()
        return total

    def __str__(self):
        data_formatada = self.getData().strftime("%d/%m/%Y")
        return f"ID: {self.getId()}\nData: {data_formatada}\n" \
               f"Número: {self.getNumero()}\n"
