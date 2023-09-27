class ItemNota:
    def __init__(self):
        self.__id_item_nota = 0
        self.__vr_unitario = 0
        self.__quantidade = 0
        self.__lista_produtos = []

    def setIdItemNota(self, id_item_nota):
        self.__id_item_nota = id_item_nota

    def getIdItemNota(self):
        return self.__id_item_nota

    def setVrUnitario(self, vr_unitario):
        self.__vr_unitario = vr_unitario

    def getVrUnitario(self):
        return self.__vr_unitario * self.__quantidade

    def getQuantidade(self):
        return self.__quantidade

    def addProduto(self, produto):
        self.__lista_produtos.append(produto)

    def listarProdutos(self):
        return self.__lista_produtos

    def __str__(self):
        return f"ID: {self.getIdItemNota()}, VrUnitário: {self.getVrUnitario()}, Quantidade: {self.getQuantidade()}"
