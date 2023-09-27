from Model.pessoa import Pessoa
from Model.aluno import Aluno
from Model.professor import Professor
from Model.situacao import Situacao
from Model.diario import Diario
from Model.turma import Turma
from Model.instituicao import Instituicao
from Model.disciplina import Disciplina
from Model.curso import Curso

eduardo = Aluno()
eduardo.setNome("Eduardo")
eduardo.setMatricula("900045809")
eduardo.setAnoInicio(2023)
eduardo.setDataNascimento("25/05/2005")

print(eduardo.getNome())
print(eduardo.getMatricula())
print(eduardo.getAnoInicio())
print(eduardo.getDataNascimento())