from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils.types import ChoiceType

db = create_engine("sqlite:///banco.db")

# Conexão do banco
Base = declarative_base()

# Base do banco de dados

# Usuários
class Usuario(Base): # O nome da tabela normalmente vai ser o nome da class tudo lower com um s no fin
    __tablename__ = "usuarios"
    
    # Restrições sql
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)
    
    # Tudo que precisa para criar um user
    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
    
# Pedidos
class Pedido(Base):
    __tablename__ = "pedidos"
    
    # Tupla
    #STATUS_PEDIDOS = (
        #(chave, valor),
    #    ("PENDENTE", "PENDENTE"),
    #    ("CALNCELADO", "CANCELADO")
    #    ("FINALIZADO", "FINALIZADO")
    #)
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) # pendente, cancelado, finalizado
    usuario = Column("usuario",  ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    itens = relationship(
        "ItemPedido",
        back_populates="pedido_rel",
        cascade="all, delete",
        lazy="joined"
    )
    
    def __init__(self, usuario, status="PENDENTE", preco=0): # Quando o banco de dados for criado nao vai ter preço ainda e nem status por issocoloca usuario="pendente e preco+0"
        self.usuario = usuario
        self.status = status
        self.preco = preco
        
    def calcular_preco(self):
        # percorrer todos os itens de pedido
        # somar todos os precos dde todos os itens dospedidos 
        # editar no campo "preco" o valor final do preco do pedido
        #preco_pedido = 0
        #for item in self.itens:
        #    preco_item = item.preco_unitario * item.quantidade
        #    preco_pedido += preco_item
        # isso tudo e a mesma coisa que essa linha de baixo
        self.preco = sum(item.preco_unitario * item.quantidade for item in self.itens)
    
# Itens de pedido
class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    
    ## talvez crie tupla de sabor ou em outro arq e de tamanhos tambem depois puxa aqui
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))
    pedido_rel = relationship(
        "Pedido",
        back_populates="itens"
    )
        
    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido


# Executar e criar os metodos do seu banco

# Criar migração: alembic revision --autogenerate -m "Alterar banco de dados"
# Executar a migração: alembic upgrade head