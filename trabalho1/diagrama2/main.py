from Model.pessoa import Pessoa
from Model.aluno import Aluno
from Model.professor import Professor
from Model.situacao import Situacao
from Model.diario import Diario
from Model.turma import Turma
from Model.instituicao import Instituicao
from Model.disciplina import Disciplina
from Model.curso import Curso

if __name__ == "__main__":
    # Criando Aluno
    aluno1 = Aluno()
    aluno1.setId(98765)
    aluno1.setNome("Eduardo")
    aluno1.setCpf("657.812.680-13")
    aluno1.setDataNascimento("25/05/2005")
    aluno1.setEmail("eduardo_uniacad@gmail.com")
    aluno1.setEndereco("Bom Pastor - Juiz de Fora")
    aluno1.setTelefone("(32) 984236701")
    aluno1.setIdentidade("MG - 78.193.578")
    aluno1.setMatricula("900045602")
    aluno1.setAnoInicio(2023)
    aluno1.setSemestreInicio(1)

    aluno2 = Aluno()
    aluno2.setId(1)
    aluno2.setNome("")
    aluno2.setCpf("")
    aluno2.setDataNascimento("")
    aluno2.setEmail("")
    aluno2.setEndereco("")
    aluno2.setTelefone("")
    aluno2.setIdentidade("")
    aluno2.setMatricula("")
    aluno2.setAnoInicio(2023)
    aluno2.setSemestreInicio(1)

    # Criando Professor 
    professor1 = Professor()
    professor1.setId(1)
    professor1.setNome("")
    professor1.setCpf("")
    professor1.setDataNascimento("")
    professor1.setEmail("")
    professor1.setEndereco("")
    professor1.setTelefone("")
    professor1.setIdentidade("")
    professor1.setMatricula("")
    professor1.setTitulacaoMaxima(1)



    