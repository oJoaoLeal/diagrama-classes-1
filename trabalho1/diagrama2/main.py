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
    aluno1.setDataNascimento('25/5/2023')
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

    aluno2.setDataNascimento("15/08/2020")
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
    professor1.setDataNascimento("25/05/2023")
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
    professor2.setDataNascimento("25/05/2023")
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

    situacao2 = Situacao()
    situacao2.setSituacao(2)
    situacao2.setAnoSemestre(2022)

    # Criando Turma
    turma1 = Turma()
    turma1.setId(1)
    turma1.setDescricao(1)
    turma1.setAno(2023)
    turma1.setSemestre(1)

    turma2 = Turma()
    turma2.setId(2)
    turma2.setDescricao(2)
    turma2.setAno(2022)
    turma2.setSemestre(2)

    # Criando Diário
    diario1 = Diario()
    diario1.setV1(85)
    diario1.setV2(70)
    diario1.setVS(0)
    diario1.setVT(0)
    diario1.setFaltas(5)

    diario2 = Diario()
    diario2.setV1(90)
    diario2.setV2(60)
    diario2.setVS(0)
    diario2.setVT(0)
    diario2.setFaltas(7)

    # Criando Instituição
    instituicao1 = Instituicao()
    instituicao1.setId(1)
    instituicao1.setDescricao('Escola Maria')

    instituicao2 = Instituicao()
    instituicao2.setId(2)
    instituicao2.setDescricao('Escola João')

    # Criando Curso
    curso1 = Curso()
    curso1.setId(1)
    curso1.setDescricao('BSI')

    curso2 = Curso()
    curso2.setId(2)
    curso2.setDescricao('BES')

    # Criando Disciplina
    disciplina1 = Disciplina()
    disciplina1.setDescricao("Algoritmos")

    disciplina2 = Disciplina()
    disciplina2.setDescricao("Cálculo")

    # Associação: Aluno recebe lista de objetos de Diário e Situação
    aluno1.addListaDiario(diario1)
    aluno1.addListaSituacao(situacao1)

    aluno2.addListaDiario(diario2)
    aluno2.addListaSituacao(situacao2)

    # Associação: Situação recebe lista de objetos de Aluno
    situacao1.addListaAluno(aluno1)

    situacao2.addListaAluno(aluno2)

    # Associação: Professor recebe lista de objetos Turma e Curso
    professor1.addListaTurma(turma1)
    professor1.addListaCurso(curso1)

    professor2.addListaTurma(turma2)
    professor2.addListaCurso(curso2)

    # Associação: Diário recebe objetos de Aluno e Turma
    diario1.setAluno(aluno1)
    diario1.setTurma(turma1)

    diario2.setAluno(aluno2)
    diario2.setTurma(turma2)

    # Associação: Turma recebe lista objetos de Diário e recebe objetos
    # de Professor, Disciplina e Instituição
    turma1.addListaDiario(diario1)
    turma1.setProfessor(professor1)
    turma1.setDisciplina(disciplina1)
    turma1.setInstituicao(instituicao1)

    turma2.addListaDiario(diario2)
    turma2.setProfessor(professor2)
    turma2.setDisciplina(disciplina2)
    turma2.setInstituicao(instituicao2)

    # Associação: Instituição recebe lista objetos de Turma
    instituicao1.addListaTurma(turma1)
    
    instituicao2.addListaTurma(turma2)

    # Associação: Disciplina recebe lista objetos de Turma e recebe objetos
    # de Curso
    disciplina1.addListaTurma(turma1)
    disciplina1.setCurso(curso1)

    disciplina2.addListaTurma(turma2)
    disciplina2.setCurso(curso2)
    
    # Associação: Curso recebe lista objetos de Disciplina e Professor
    curso1.addListaDisciplina(disciplina1)
    curso1.addListaProfessor(professor1)

    curso2.addListaDisciplina(disciplina2)
    curso2.addListaProfessor(professor2)

    # Print
    print("1) Aluno:")
    print(aluno1.__str__())
    print("------------------")
    print("Situação do Aluno 1:")
    for situacao in aluno1.getListaSituacao():
        print(situacao)
    print("------------------")
    print("Diário do Aluno 1:")
    for diario in aluno1.getListaDiario():
        print(diario)
    print("------------------")
    print()
    print("2) Aluno:")
    print(aluno2.__str__())
    print("------------------")
    print("Situação do Aluno 2:")
    for situacao in aluno2.getListaSituacao():
        print(situacao)
    print("------------------")
    print("Diário do Aluno 2:")
    for diario in aluno2.getListaDiario():
        print(diario)
    print("------------------")
    ############################################
    print()
    print("1) Situação:")
    print(situacao1.__str__())
    print("------------------")
    print("Aluno da Situação 1:")
    for aluno in situacao1.getListaAluno():
        print(aluno)
    print("------------------")
    print()
    print("2) Situação:")
    print(situacao2.__str__())
    print("------------------")
    print("Aluno da Situação 2:")
    for aluno in situacao2.getListaAluno():
        print(aluno)
    print("------------------")
    ############################################
    print()
    print("1) Professor:")
    print(professor1.__str__())
    print('------------------')
    print("Turma(s) do Professor 1:")
    for turma in professor1.getListaTurma():
        print(turma)
    print("------------------")
    print("Curso(s) do Professor 1:")
    for curso in professor1.getListaCurso():
        print(curso)
    print("------------------")
    print()
    print("2) Professor:")
    print(professor2.__str__())
    print('------------------')
    print("Turma(s) do Professor 2:")
    for turma in professor2.getListaTurma():
        print(turma)
    print("------------------")
    print("Curso(s) do Professor 2:")
    for curso in professor2.getListaCurso():
        print(curso)
    print("------------------")
    ############################################
    print()
    print("1) Diário:")
    print(diario1.__str__())
    print('------------------')
    print("Aluno do Diário 1:")
    print(aluno1.getNome())
    print('------------------')
    print("Turma do Diário 1:")
    print(turma1.getId())
    print('------------------')
    print()
    print("2) Diário:")
    print(diario2.__str__())
    print('------------------')
    print("Aluno do Diário 2:")
    print(aluno2.getNome())
    print('------------------')
    print("Turma do Diário 2:")
    print(turma2.getId())
    print('------------------')
    ############################################
    print()
    print("1) Turma:")
    print(turma1.__str__())
    print('------------------')
    print("Diários(s) da Turma 1:")
    for diario in turma1.getListaDiario():
        print(diario)
    print('------------------')
    print("Instituição da Turma 1:")
    print(instituicao1.getDescricao())
    print('------------------')
    print("Disciplina da Turma 1:")
    print(disciplina1.getDescricao())
    print('------------------')
    print("Professor da Turma 1:")
    print(professor1.getNome())
    print('------------------')
    print()
    print("2) Turma:")
    print(turma2.__str__())
    print('------------------')
    print("Diários(s) da Turma 2:")
    for diario in turma2.getListaDiario():
        print(diario)
    print('------------------')
    print("Instituição da Turma 2:")
    print(instituicao2.getDescricao())
    print('------------------')
    print("Disciplina da Turma 2:")
    print(disciplina2.getDescricao())
    print('------------------')
    print("Professor da Turma 2:")
    print(professor2.getNome())
    print('------------------')
    ############################################
    print()
    print("1) Instituição:")
    print(instituicao1.__str__())
    print('------------------')
    print("Turma(s) da Instituição 1:")
    for turma in instituicao1.getListaTurma():
        print(turma)
    print('------------------')
    print()
    print("2) Instituição:")
    print(instituicao2.__str__())
    print('------------------')
    print("Turma(s) da Instituição 2:")
    for turma in instituicao2.getListaTurma():
        print(turma)
    ############################################
    print()
    print("1) Disciplina:")
    print(disciplina1.__str__())
    print('------------------')
    print("Turma(s) da Disciplina 1:")
    for turma in disciplina1.getListaTurma():
        print(turma)
    print('------------------')
    print("Curso da Disciplina 1:")
    print(curso1.getDescricao())
    print('------------------')
    print()
    print("2) Disciplina:")
    print(disciplina2.__str__())
    print('------------------')
    print("Turma(s) da Disciplina 2:")
    for turma in disciplina2.getListaTurma():
        print(turma)
    print('------------------')
    print("Curso da Disciplina 2:")
    print(curso2.getDescricao())

    print()
    print("1) Curso:")
    print(curso1.__str__())
    print('------------------')
    print("Disciplina(s) do Curso 1:")
    for disciplina in curso1.getListaDisciplina():
        print(disciplina)
    print('------------------')
    print("Professor(es) do Curso 1:")
    for professor in curso1.getListaProfessor():
        print(professor)
    print()
    print("2) Curso:")
    print(curso2.__str__())
    print('------------------')
    print("Disciplina(s) do Curso 2:")
    for disciplina in curso2.getListaDisciplina():
        print(disciplina)
    print('------------------')
    print("Professor(es) do Curso 2:")
    for professor in curso2.getListaProfessor():
        print(professor)
