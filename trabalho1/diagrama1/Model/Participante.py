class Participante:
    def __init__(self):
        self.__id_participante = 0
        self.__codigo_participante = 0
        self.__razao_social = ''
        self.__cnpj = 0
        # Cada participantes recebe uma nota
        self.__nota = None

    def setIdParticipante(self, id_participante):
        self.__id_participante = id_participante

    def getIdParticipante(self):
        return self.__id_participante

    def setCodigoParticipante(self, codigo_participante):
        self.__codigo_participante = codigo_participante

    def getCodigoParticipante(self):
        return self.__codigo_participante

    def setRazaoSocial(self, razao_social):
        self.__razao_social = razao_social

    def getRazaoSocial(self):
        return self.__razao_social

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj

    def getCnpj(self):
        return self.__cnpj

    def setNotaParticipante(self, nota):
        self.__nota = nota

    def getNotaParticipante(self):
        return self.__nota

    def __str__(self):
        return f"ID: {self.getIdParticipante()}\nCódigo Participante: {self.getCodigoParticipante()}\n" \
               f"Razão Social: {self.getRazaoSocial()}\nCNPJ: {self.getCnpj()}"
