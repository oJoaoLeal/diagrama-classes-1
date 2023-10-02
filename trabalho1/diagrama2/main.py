from datetime import datetime
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
    aluno1.setNome("Eduardo das Flores")
    aluno1.setCpf("657.812.680-13")
    aluno1.setDataNascimento(datetime(day=25,month=5,year=2005,hour=12,minute=15))
    aluno1.setEmail("eduardo_uniacad@gmail.com")
    aluno1.setEndereco("Bom Pastor - Juiz de Fora")
    aluno1.setTelefone("(32) 984236701")
    aluno1.setIdentidade("MG - 78.193.578")
    aluno1.setMatricula("900045602")
    aluno1.setAnoInicio(2023)
    aluno1.setSemestreInicio(1)

    aluno2 = Aluno()
    aluno2.setId(98653)
    aluno2.setNome("José das Couves")
    aluno2.setCpf("018.575.639-17")
    aluno2.setDataNascimento(datetime(day=18,month=10,year=2004,hour=4,minute=7))
    aluno2.setEmail("josecouves@gmail.com")
    aluno2.setEndereco("Centro - Juiz de Fora")
    aluno2.setTelefone("(32) 988880110")
    aluno2.setIdentidade("MG - 14.852.963")
    aluno2.setMatricula("900035996")
    aluno2.setAnoInicio(2020)
    aluno2.setSemestreInicio(2)

    # Criando Professor 
    professor1 = Professor()
    professor1.setId(55875)
    professor1.setNome("Girafales Ramos")
    professor1.setCpf("235.426.112-65")
    professor1.setDataNascimento(datetime(day=4,month=7,year=1980,hour=18,minute=45))
    professor1.setEmail("giraramos@yahoo.com.br")
    professor1.setEndereco("MG - Benfica")
    professor1.setTelefone("(32) 999887054")
    professor1.setIdentidade("MG - 7.852.274")
    professor1.setMatricula("12575235")
    professor1.setTitulacaoMaxima(1)

    professor2 = Professor()
    professor2.setId(55665)
    professor2.setNome("Cinthia Teixeira")
    professor2.setCpf("933.127.985-00")
    professor2.setDataNascimento(datetime(day=27,month=1,year=1975,hour=22,minute=10))
    professor2.setEmail("cintei@gmail.com")
    professor2.setEndereco("MG - Lima Duarte")
    professor2.setTelefone("32 991753021")
    professor2.setIdentidade("MG - 8.444.333")
    professor2.setMatricula("12575400")
    professor2.setTitulacaoMaxima(2)

    # Criando Situação
    situacao1 = Situacao()
    situacao1.setSituacao(1)
    situacao1.setAnoSemestre(2023)
    situacao1.addListaAluno(aluno1.getNome())

    situacao2 = Situacao()
    situacao2.setSituacao(2)
    situacao2.setAnoSemestre(2022)
    situacao2.addListaAluno(aluno2.getNome())

    # Criando Turma
    turma1 = Turma()
    turma1.setId(1)
    turma1.setDescricao(1)
    turma1.setAno(2023)
    turma1.setSemestre(1)
    turma1.setProfessor(professor1.getNome())

    turma2 = Turma()
    turma2.setId(2)
    turma2.setDescricao(2)
    turma2.setAno(2022)
    turma2.setSemestre(2)
    turma2.setProfessor(professor2.getNome())

    # Criando Diário
    diario1 = Diario()
    diario1.setV1(85)
    diario1.setV2(70)
    diario1.setVS(0)
    diario1.setVT(0)
    diario1.setFaltas(5)
    diario1.setAluno(aluno1.getNome())
    diario1.setTurma(turma1.getId())

    diario2 = Diario()
    diario2.setV1(90)
    diario2.setV2(60)
    diario2.setVS(0)
    diario2.setVT(0)
    diario2.setFaltas(7)
    diario2.setAluno(aluno2.getNome())
    diario2.setTurma(turma2.getId())

    # Criando Instituição
    instituicao1 = Instituicao()
    instituicao1.setId(1)
    instituicao1.setDescricao('Escola Maria')
    instituicao1.addListaTurma(turma1.getId())

    instituicao2 = Instituicao()
    instituicao2.setId(2)
    instituicao2.setDescricao('Escola João')
    instituicao2.addListaTurma(turma2.getId())

    # Criando Curso
    curso1 = Curso()
    curso1.setId('1')
    curso1.setDescricao('BSI')
    curso1.addListaProfessor(professor1.getNome())

    curso2 = Curso()
    curso2.setId('2')
    curso2.setDescricao('BES')
    curso2.addListaProfessor(professor2.getNome())

    # Criando Disciplina
    disciplina1 = Disciplina()
    disciplina1.setDescricao("Algoritmos")
    disciplina1.setCurso(curso1.getDescricao())
    disciplina1.addListaTurma(turma1.getId())

    disciplina2 = Disciplina()
    disciplina2.setDescricao("Cálculo")
    disciplina2.setCurso(curso2.getDescricao())
    disciplina2.addListaTurma(turma2.getId())
        
    
    # Situações e Diários dos Alunos:
    aluno1.addListaSituacao(situacao1.getSituacao())
    aluno1.addListaDiario(diario1.getTurma())

    aluno2.addListaSituacao(situacao2.getSituacao())
    aluno2.addListaDiario(diario2.getTurma())

    # Turmas e Cursos Professores:
    professor1.addListaTurma(turma1.getId())
    professor1.addListaCurso(curso1.getDescricao())

    professor2.addListaTurma(turma2.getId())
    professor2.addListaCurso(curso2.getDescricao())

    # Instituições, disciplinas e diários das turmas:
    turma1.setInstituicao(instituicao1)
    turma1.setDisciplina(disciplina1)
    turma1.addListaDiario(diario1)

    turma2.setInstituicao(instituicao2)
    turma2.setDisciplina(disciplina2)
    turma2.addListaDiario(diario2)
 
    # Disciplinas dos cursos
    curso1.addListaDisciplina(disciplina1.getDescricao())
    curso2.addListaDisciplina(disciplina2.getDescricao())
    

    print("1) Aluno:")
    print(aluno1.__str__())
    print('------------------')
    print("2) Aluno:")
    print(aluno2.__str__())

    print()
    print("1) Professor:")
    print(professor1.__str__())
    print('------------------')
    print("2) Professor:")
    print(professor2.__str__())

    print()
    print("1) Situação:")
    print(situacao1.__str__())
    print('------------------')
    print("2) Situação:")
    print(situacao2.__str__())

    print()
    print("1) Turma:")
    print(turma1.__str__())
    print('------------------')
    print("2) Turma:")
    print(turma2.__str__())

    print()
    print("1) Diário:")
    print(diario1.__str__())
    print('------------------')
    print("2) Diário:")
    print(diario2.__str__())

    print()
    print("1) Instituição:")
    print(instituicao1.__str__())
    print('------------------')
    print("2) Instituição:")
    print(instituicao2.__str__())

    print()
    print("1) Curso:")
    print(curso1.__str__())
    print('------------------')
    print("2) Curso:")
    print(curso2.__str__())

    print()
    print("1) Disciplina:")
    print(disciplina1.__str__())
    print('------------------')
    print("2) Disciplina:")
    print(disciplina2.__str__())