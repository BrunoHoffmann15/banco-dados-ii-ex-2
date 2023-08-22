from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    sexo = Column(String)    


class Cartao(Base):
    __tablename__ = 'cartoes'

    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    cvv = Column(Integer)
    validade = Column(String)
    nome_no_cartao = Column(String)
    client_id = Column(Integer, ForeignKey('clientes.id'))
