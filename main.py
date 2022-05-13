from sqlalchemy import *
from aluno import Aluno, criarTabelaAluno
from aluno_repositorio import AlunoRepositorio

engine = create_engine('sqlite:///aula.db', echo=True)

criarTabelaAluno(engine)

alunoRepositorio = AlunoRepositorio(engine)

'''
alunoRepositorio.criaAluno({"ra": 103817, 
                            "nome": "Luizinho",
                           "nota": 3
                            })
'''


print(alunoRepositorio.lerAlunos())


'''
print(alunoRepositorio.lerAlunoPorRA(102476))
'''

'''
alunoRepositorio.atualizaAluno({"ra": 102476,
                               "nome": "Maurício",
                               "nota": 3.5
                               })
'''

'''
alunoRepositorio.removeAluno(103817)
'''