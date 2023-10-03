from Model.pessoa import Pessoa


class Aluno(Pessoa):  # Classe Filho

    def __init__(self):
        super().__init__()
        self.__matricula = None
        self.__anoInicio = None
        self.__semestreInicio = None
        self.__listaSituacao = []
        self.__listaDiario = []

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula
    
    def setAnoInicio(self, anoInicio):
        self.__anoInicio = anoInicio

    def getAnoInicio(self):
        return self.__anoInicio
    
    def setSemestreInicio(self, semestreInicio):
        self.__semestreInicio = semestreInicio

    def getSemestreInicio(self):
        return self.__semestreInicio
    
    def setListaSituacao(self, situacao):
        self.__listaSituacao = situacao

    def addListaSituacao(self, situacao):
        self.__listaSituacao.append(situacao)

    def removerListaSituacao(self, situacao):
        self.__listaSituacao.remove(situacao)

    def getListaSituacao(self):

        return self.__listaSituacao
    
    def setListaDiario(self, diario):
        self.__listaDiario = diario

    def addListaDiario(self, diario):
        self.__listaDiario.append(diario)

    def removerListaDiario(self, diario):
        self.__listaDiario.remove(diario)

    def getListaDiario(self):
        return self.__listaDiario
    
    def __str__(self):
        return f"ID: {self.getId()}\nNome: {self.getNome()}\n" \
               f"CPF: {self.getCpf()}\nData de Nascimento: {self.getDataNascimento()}\n" \
               f"Email: {self.getEmail()}\nEndereço: {self.getEndereco()}\n" \
               f"Telefone: {self.getTelefone()}\nIdentidade: {self.getIdentidade()}\n" \
               f"Matricula: {self.getMatricula()}\nAno de Inicio: {self.getAnoInicio()}\n" \
               f"Semestre de inicio: {self.getSemestreInicio()}"

