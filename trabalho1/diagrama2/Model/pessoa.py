from datetime import datetime

class Pessoa: # Classe Pai

    def __init__(self) -> None:
        self.__id = 1
        self.__nome = ""
        self.__cpf = ""
        self.__dataNascimento = ""
        self.__email = ""
        self.__endereco = ""
        self.__telefone = ""
        self.__identidade = ""

    def setId(self, id: int) -> None:
        self.__id = id

    def getId(self) -> int:
        return self.__id
    
    def setNome(self, nome: str) -> None:
        self.__nome = nome

    def getNome(self) -> str:
        return self.__nome
    
    def setCpf(self, cpf: str) -> None:
        self.__cpf = cpf

    def getCpf(self) -> str:
        return self.__cpf
    
    def setDataNascimento(self, dataNascimento: datetime) -> None:
        self.__dataNascimento = dataNascimento

    def getDataNascimento(self) -> datetime:
        return self.__dataNascimento
    
    def setEmail(self, email: str) -> None:
        self.__email = email

    def getEmail(self) -> str:
        return self.__email
    
    def setEndereco(self, endereco: str) -> None:
        self.__endereco = endereco

    def getEndereco(self) -> str:
        return self.__endereco

    def setTelefone(self, telefone: str) -> None:
        self.__telefone = telefone

    def getTelefone(self) -> str:
        return self.__telefone
    
    def setIdentidade(self, identidade: str) -> None:
        self.__identidade = identidade

    def getIdentidade(self) -> str:
        return self.__identidade
    
    def __str__(self) -> None:
        return f"ID: {self.getId()}\nNome: {self.getNome()}\n" \
               f"CPF: {self.getCpf()}\nData de Nascimento: {self.getDataNascimento()}\n" \
               f"Email: {self.getEmail()}\nEndereço: {self.getEndereco()}\n" \
               f"Telefone: {self.getTelefone()}\nIdentidade: {self.getIdentidade()}"