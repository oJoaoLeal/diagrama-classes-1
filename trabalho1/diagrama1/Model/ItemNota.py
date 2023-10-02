class ItemNota:
    def __init__(self):
        self.__id_item = None
        self.__vr_unitario = None
        self.__quantidade = None
        self.__produto = None  # Associacao: Recebe um objeto de "Produto"
        self.__nota = None  # Associacao: Recebe um objeto de "Nota"

    def getId(self):
        return self.__id_item

    def getVrUnitario(self):
        return self.__vr_unitario

    def getQuantidade(self):
        return self.__quantidade

    def getProduto(self):
        return self.__produto

    def getNota(self):
        return self.__nota

    def setId(self, id_item):
        self.__id_item = id_item

    def setVrUnitario(self, vr_unitario):
        self.__vr_unitario = vr_unitario

    def setQuantidade(self, quantidade):
        self.__quantidade = quantidade

    def setProduto(self, produto):
        self.__produto = produto

    def setNota(self, nota):
        self.__nota = nota

    def __str__(self):
        return f"ID: {self.getId()}\nVrUnitário: {self.getVrUnitario()}\n" \
               f"Quantidade: {self.getQuantidade()}"
