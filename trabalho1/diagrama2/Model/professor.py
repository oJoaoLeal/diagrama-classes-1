from Model.pessoa import Pessoa

class Professor(Pessoa): # Classe Filho

    def __init__(self) -> None:
        super().__init__()
        self.__matricula = ""
        self.__titulacaoMaxima = 1
        self.__listaTurma = []
        self.__listaCurso = []

    def setMatricula(self, matricula: str) -> None:
        self.__matricula = matricula

    def getMatricula(self) -> str:
        return self.__matricula
    
    def setTitulacaoMaxima(self, titulacaoMaxima: int) -> None:
        self.__titulacaoMaxima = titulacaoMaxima

    def getTitulacaoMaxima(self) -> int:
        return self.__titulacaoMaxima
    
    def setListaTurma(self, turma) -> None:
        self.__listaTurma = turma

    def addListaTurma(self, turma) -> None:
        self.__listaTurma.append(turma)

    def removerListaTurma(self, turma) -> None:
        self.__listaTurma.remove(turma)

    def getListaTurma(self) -> None:
        return self.__listaTurma
    
    def setListaCurso(self, curso) -> None:
        self.__listaCurso = curso

    def addListaCurso(self, curso) -> None:
        self.__listaCurso.append(curso)

    def removerListaCurso(self, curso) -> None:
        self.__listaCurso.remove(curso)

    def getListaCurso(self) -> None:
        return self.__listaCurso
    
    def __str__(self) -> None:
        return f"ID: {self.getId()}\nNome: {self.getNome()}\n" \
               f"CPF: {self.getCpf()}\nData de Nascimento: {self.getDataNascimento()}\n" \
               f"Email: {self.getEmail()}\nEndereço: {self.getEndereco()}\n" \
               f"Telefone: {self.getTelefone()}\nIdentidade: {self.getIdentidade()}\n" \
               f"Matricula: {self.getMatricula()}\nTitulação Maxima: {self.getTitulacaoMaxima()}\n" \
               f"Turma(s): {self.getListaTurma()}\nCurso(s): {self.getListaCurso()}"
    