from Model.pessoa import Pessoa


class Professor(Pessoa):  # Classe Filho

    def __init__(self):
        super().__init__()
        self.__matricula = None
        self.__titulacaoMaxima = None
        self.__listaTurma = []
        self.__listaCurso = []

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula
    
    def setTitulacaoMaxima(self, titulacaoMaxima):
        self.__titulacaoMaxima = titulacaoMaxima

    def getTitulacaoMaxima(self):
        return self.__titulacaoMaxima
    
    def setListaTurma(self, turma):
        self.__listaTurma = turma

    def addListaTurma(self, turma):
        self.__listaTurma.append(turma)

    def removerListaTurma(self, turma):
        self.__listaTurma.remove(turma)
   
    def getListaTurma(self):
        return self.__listaTurma
    
    def setListaCurso(self, curso):
        self.__listaCurso = curso

    def addListaCurso(self, curso):
        self.__listaCurso.append(curso)

    def removerListaCurso(self, curso):
        self.__listaCurso.remove(curso)

    def getListaCurso(self):
        return self.__listaCurso
    
    def __str__(self):
        return f"ID: {self.getId()}\nNome: {self.getNome()}\n" \
               f"CPF: {self.getCpf()}\nData de Nascimento: {self.getDataNascimento()}\n" \
               f"Email: {self.getEmail()}\nEndereço: {self.getEndereco()}\n" \
               f"Telefone: {self.getTelefone()}\nIdentidade: {self.getIdentidade()}\n" \
               f"Matricula: {self.getMatricula()}\nTitulação Maxima: {self.getTitulacaoMaxima()}"
    