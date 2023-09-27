class Empresa:

    def __init__(self):
        self.__codigo = -1
        self.__id_empresa = -1
        self.__razao_social = ''
        self.__endereco = ''
        self.__cnpj = ''
        self.__lista_notas = []

    def setIdEmpresa(self, id_empresa):
        self.__id_empresa = id_empresa

    def getIdEmpresa(self):
        return self.__id_empresa

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getRazaoSocial(self):
        return self.__razao_social

    def setRazaoSocial(self, razao_social):
        self.__razao_social = razao_social

    def getEndereco(self):
        return self.__endereco

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def getCnpj(self):
        return self.__cnpj

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    def addNota(self, nota):
        self.__lista_notas.append(nota)

    def getNotas(self):
        return self.__lista_notas

    def __str__(self):
        return f"Código: {self.getCodigo()}\nID Empresa: {self.getIdEmpresa()}\n"\
               f"Razão Social: {self.getRazaoSocial()}\nEndereço: {self.getEndereco()}\nCNPJ: {self.getCnpj()}"
