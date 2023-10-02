from Model.pessoa import Pessoa

class Aluno(Pessoa): # Classe Filho

    def __init__(self) -> None:
        super().__init__()
        self.__matricula = ""
        self.__anoInicio = 1
        self.__semestreInicio = 1
        self.__listaSituacao = []
        self.__listaDiario = []

    def setMatricula(self, matricula: str) -> None:
        self.__matricula = matricula

    def getMatricula(self) -> str:
        return self.__matricula
    
    def setAnoInicio(self, anoInicio: int) -> None:
        self.__anoInicio = anoInicio

    def getAnoInicio(self) -> int:
        return self.__anoInicio
    
    def setSemestreInicio(self, semestreInicio: int) -> None:
        self.__semestreInicio = semestreInicio

    def getSemestreInicio(self) -> int:
        return self.__semestreInicio
    
    def setListaSituacao(self, situacao) -> None:
        self.__listaSituacao = situacao

    def addListaSituacao(self, situacao) -> None:
        self.__listaSituacao.append(situacao)

    def removerListaSituacao(self, situacao) -> None:
        self.__listaSituacao.remove(situacao)

    def getListaSituacao(self) -> None:
        return self.__listaSituacao
    
    def setListaDiario(self, diario) -> None:
        self.__listaDiario = diario

    def addListaDiario(self, diario) -> None:
        self.__listaDiario.append(diario)

    def removerListaDiario(self, diario) -> None:
        self.__listaDiario.remove(diario)

    def getListaDiario(self) -> None:
        return self.__listaDiario
    
    def __str__(self) -> None:
        return f"ID: {self.getId()}\nNome: {self.getNome()}\n" \
               f"CPF: {self.getCpf()}\nData de Nascimento: {self.getDataNascimento()}\n" \
               f"Email: {self.getEmail()}\nEndereço: {self.getEndereco()}\n" \
               f"Telefone: {self.getTelefone()}\nIdentidade: {self.getIdentidade()}\n" \
               f"Matricula: {self.getMatricula()}\nAno de Inicio: {self.getAnoInicio()}\n" \
               f"Semestre de inicio: {self.getSemestreInicio()}\nSituação(ões): {self.getListaSituacao()}\n" \
               f"Diário(s): {self.getListaDiario()}\n"