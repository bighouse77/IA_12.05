from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# Construindo uma classe base
Base = declarative_base()

class Aluno(Base):
    __tablename__ = "aluno"
    ra = Column(Integer, primary_key=True)
    nome = Column(String(50))
    nota = Column(Float)
    
def criarTabelaAluno(engine):
    Base.metadata.create_all(engine)