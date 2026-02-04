from pydantic import BaseModel
from typing import Optional # isso faz que tenha parametros opcionais 

class UsuarioSchema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]
    
    # isso faz que a class de cima seja vista como um dicionário padrão de py
    class Config:
        from_attributes = True
        
class PedidoSchema(BaseModel):# Pedido schema tem que ter a mesma variavel de criar pedido no arq auth
    usuario: int
    
    class Config:
        from_attributes = True
        
class LoginSchema(BaseModel):
    email: str
    senha: str
    
    class Config:
        from_atributes = True
        
class ItemPedidoSchema(BaseModel):
    quantidade: int
    sabor: str
    tamanho: str
    preco_unitario: float
    
    class config:
        from_atributes = True