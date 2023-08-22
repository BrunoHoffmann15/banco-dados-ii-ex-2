from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definição da classe de modelo Cliente
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
    
# Configuração da conexão com o banco de dados (SQLite no exemplo)
engine = create_engine('sqlite:///clientes.db')

# Criação da tabela no banco de dados
Base.metadata.create_all(engine)

# Criação de uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Inserção de um novo cliente
#novo_cliente = Cliente(nome='Joao', idade=35, sexo='Masculino')
#session.add(novo_cliente)
#session.commit()

# Consulta de todos os clientes
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f"ID: {cliente.id}, Nome: {cliente.nome}, Idade: {cliente.idade}, Sexo: {cliente.sexo}")

# Fechamento da sessão
session.close()
