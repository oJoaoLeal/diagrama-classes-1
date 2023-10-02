from datetime import date


class Participante:
    def __init__(self):
        self.__id = None
        self.__codigo = None
        self.__razao_social = None
        self.__cnpj = None
        self.__notas = []  # Associacao: Partipante com Nota

    def get_id(self):
        return self.__id

    def get_codigo(self):
        return self.__codigo

    def get_razaoSocial(self):
        return self.__razao_social

    def get_cnpj(self):
        return self.__cnpj

    def set_id(self, id):
        self.__id = id

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_razaoSocial(self, __razao_social):
        self.__razao_social = __razao_social

    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj

    def addNota(self, nota):
        self.__notas.append(nota)

    def getNotas(self):
        return self.__notas

    def __str__(self):
        return f"ID: {self.get_id()}\nCódigo Participante: {self.get_codigo()}\n" \
               f"Razão Social: {self.get_razaoSocial()}\nCNPJ: {self.get_cnpj()}"
