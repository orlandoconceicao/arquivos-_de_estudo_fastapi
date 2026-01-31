from fastapi import Depends, HTTPException
from models import db
from sqlalchemy.orm import sessionmaker, Session
from models import Usuario
from jose import jwt, JWTError
from main import SECRET_KEY, ALGORITHM, oauth2_schema

def pegar_sessao():
    try: #try tenta fazer oque tem abaixo #mas assim voce pode forçar ele fechar independente se der erro na outra funcao
        Session = sessionmaker(bind=db)
        session = Session()
        yield session # Quase igual o return mas ele não encerra a sessao
        # Se o try der errado usa para executar outra coisa nao sendo nosso caso
        #except:
        # Se a funçao que estamos colocando essa funçao der erro ele para no yield 
    finally: # executa independente do que acontecer ele fecha a sessao
        session.close() # com o yield pode encerrar a sessao com o session.close()

# Tudo que precisa para criar um token
def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)):
    try: 
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_usuario = int(dic_info.get("sub"))
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso negado, verifique a validade do token")
    # verificar se o token e valido, sendo token valido tem que extrair o id do usuario do token
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Acesso inválido")
    return usuario

# OAuth2 - access-Token: bearer => que passa que o token tem que ir e vir pela header