class Pessoa: # Classe Pai

    def __init__(self):
        self.__id = None
        self.__nome = None
        self.__cpf = None
        self.__dataNascimento = None
        self.__email = None
        self.__endereco = None
        self.__telefone = None
        self.__identidade = None

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id
    
    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def setCpf(self, cpf):
        self.__cpf = cpf

    def getCpf(self):
        return self.__cpf
    
    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    def getDataNascimento(self):
        return self.__dataNascimento
    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email
    
    def setEndereco(self, endereco):
        self.__endereco = endereco

    def getEndereco(self):
        return self.__endereco

    def setTelefone(self, telefone):
        self.__telefone = telefone

    def getTelefone(self):
        return self.__telefone
    
    def setIdentidade(self, identidade):
        self.__identidade = identidade

    def getIdentidade(self):
        return self.__identidade

    def __str__(self):
        return f"ID: {self.getId()}\nNome: {self.getNome()}\n" \
               f"CPF: {self.getCpf()}\nData de Nascimento: {self.getDataNascimento()}\n" \
               f"Email: {self.getEmail()}\nEndereço: {self.getEndereco()}\n" \
               f"Telefone: {self.getTelefone()}\nIdentidade: {self.getIdentidade()}"
