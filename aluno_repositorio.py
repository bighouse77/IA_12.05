from sqlalchemy import *
from sqlalchemy.orm import *

from aluno import Aluno

class AlunoRepositorio:
    
    def __init__(self, engine):
        self.engine = engine
        
        
    def criaAluno(self, novoAluno):
        # Criar um objeto "sessão"
        sessionConfig = sessionmaker(self.engine)
        session = sessionConfig()
        
        session.add(Aluno(ra = int(novoAluno['ra']),
                          nome = novoAluno['nome'],
                          nota = float(novoAluno['nota']))
        )
        session.commit()
        
        
    def lerAlunos(self):
        sessionConfig = sessionmaker(self.engine)
        session = sessionConfig()
        
        todosAlunos = session.query(Aluno).all()
        
        listaJson = []
        
        for aluno in todosAlunos:
            listaJson.append({"ra": aluno.ra,
                              "nome": aluno.nome,
                              "nota": aluno.nota
                              })
        return listaJson
    
    
    def lerAlunoPorRA(self, raProcurado):
        sessionConfig = sessionmaker(self.engine)
        session = sessionConfig()
        
        aluno = session.query(Aluno).filter_by(ra = raProcurado).first()
        
        if aluno == None:
            return None
        
        return {"ra": aluno.ra,
                "nome": aluno.nome,
                "nota": aluno.nota
                }
        
        
    def atualizaAluno(self, alunoAtualizado):
        sessionConfig = sessionmaker(self.engine)
        session = sessionConfig()
        
        aluno = session.query(Aluno).filter_by(ra = alunoAtualizado['ra']).first()
        
        if aluno == None:
            return None
        
        aluno.nome = alunoAtualizado['nome']
        aluno.nota = alunoAtualizado['nota']
        
        session.add(aluno)
        
    
        session.commit()
        
        
    def removeAluno(self, raRemovido):
        sessionConfig = sessionmaker(self.engine)
        session = sessionConfig()
        
        aluno = session.query(Aluno).filter_by(ra = raRemovido).first()
        
        if aluno == None:
            return None
        
        session.delete(aluno)
        session.commit()