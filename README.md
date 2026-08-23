# API REST com FastAPI

API de estudos para autenticação de usuários e gerenciamento de pedidos, desenvolvida com FastAPI e SQLAlchemy.

## Sobre o projeto

O projeto implementa cadastro e login com tokens JWT, além de operações autenticadas para criar, consultar, alterar o estado e gerenciar os itens de pedidos. A estrutura do banco é versionada com Alembic.

## Funcionalidades

- criação de contas de usuário;
- autenticação com JWT e renovação de token;
- criação e consulta de pedidos;
- inclusão e remoção de itens;
- cancelamento e finalização de pedidos;
- documentação automática com Swagger e ReDoc.

## Tecnologias

- Python
- FastAPI e Uvicorn
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- Passlib e Python JOSE

## Estrutura

```text
fastapi-studies/
|-- main.py             # Inicialização da aplicação
|-- auth_routes.py      # Cadastro e autenticação
|-- order_routes.py     # Operações de pedidos
|-- models.py           # Modelos SQLAlchemy
|-- schemas.py          # Schemas Pydantic
|-- database.py         # Conexão com o banco
|-- dependencies.py     # Validação do token
`-- alembic/            # Migrações do banco de dados
```

## Como executar

Crie um ambiente virtual e instale as dependências:

```powershell
git clone https://github.com/orlandoconceicao/fastapi-studies.git
cd fastapi-studies
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Configure `DATABASE_URL`, `SECRET_KEY`, `ALGORITHM` e `ACCESS_TOKEN_EXPIRE_MINUTES` no ambiente. Em seguida, aplique as migrações e inicie a API:

```powershell
alembic upgrade head
uvicorn main:app --reload
```

O Swagger ficará disponível em `http://127.0.0.1:8000/docs` e o ReDoc em `http://127.0.0.1:8000/redoc`.

## Testes

O repositório ainda não possui uma suíte de testes automatizados.

## Autor

**Orlando Conceição Vilhalba de Almeida**

Desenvolvedor Backend em formação, com foco em Python, Django, Django REST Framework, PostgreSQL, APIs REST e Docker, utilizando React como tecnologia complementar para integração das aplicações.

GitHub: https://github.com/orlandoconceicao

LinkedIn: https://www.linkedin.com/in/orlando-concei%C3%A7%C3%A3o-582234315

Portfólio: https://orlandoconceicao.github.io/
