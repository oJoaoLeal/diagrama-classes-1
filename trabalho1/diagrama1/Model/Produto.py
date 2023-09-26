class Produto:
    def __init__(self):
        self.__id_produto = 0
        self.__codigo_produto = 0
        self.__descricao = ''
        self.item_nota_lista = []

    def setIdProduto(self, id_produto):
        self.__id_produto = id_produto

    def getIdProduto(self):
        return self.__id_produto

    def setCodigoProduto(self, codigo_produto):
        self.__codigo_produto = codigo_produto

    def getCodigoProduto(self):
        return self.__codigo_produto

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def getDescricao(self):
        return self.__descricao

