from decimal import Decimal
from datetime import date


class Empresa:

    def __init__(self):
        self.__codigo = None
        self.__id = None
        self.__razao_social = None
        self.__endereco = None
        self.__cnpj = None
        self.__notas = []  # Associacao: Empresa recebe uma lista de "Nota"

    def getId(self):
        return self.__id

    def getCodigo(self):
        return self.__codigo

    def getRazaoSocial(self):
        return self.__razao_social

    def getEndereco(self):
        return self.__endereco

    def getCnpj(self):
        return self.__cnpj

    def setId(self, id):
        self.__id = id

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setRazaoSocial(self, razao_social):
        self.__razao_social = razao_social

    def setEndereco(self, endereco):
        self.__endereco = endereco

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    def addNota(self, nota):
        self.__notas.append(nota)

    def getNotas(self):
        return self.__notas

    def __str__(self):
        return f"Código: {self.getCodigo()}\nID Empresa: {self.getId()}\n"\
               f"Razão Social: {self.getRazaoSocial()}\nEndereço: {self.getEndereco()}\nCNPJ: {self.getCnpj()}"
