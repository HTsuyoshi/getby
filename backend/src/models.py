from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)

class Sentimento(Base):
    __tablename__ = 'sentimento'
    id_sentimento = Column(Integer, primary_key=True, index=True)
    sentimento = Column(String)

class Sentimento_usuario(Base):
    __tablename__ = 'sentimento_usuario'
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), primary_key=True)
    id_sentimento = Column(Integer, ForeignKey('sentimento.id_sentimento'), primary_key=True)

class Sugestao(Base):
    __tablename__ = 'sugestao'
    id_sugestao = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    id_sentimento = Column(Integer, ForeignKey('sentimento.id_sentimento'))
    sugestao = Column(String)
    feedback = Column(Integer)

class Usuario_sugestao(Base):
    __tablename__ = 'usuario_sugestao'
    id_usuario = Column(Integer, ForeignKey('usuario.id_usuario'), primary_key=True)
    id_sugestao = Column(Integer, ForeignKey('sugestao.id_sugestao'), primary_key=True)
    feedback = Column(Integer)
