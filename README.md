# API REST com FastAPI

Projeto backend desenvolvido para praticar e consolidar a construção de APIs REST modernas com **FastAPI**, utilizando **PostgreSQL**, **SQLAlchemy**, **Alembic** e boas práticas de organização de código.  

---

## Links do Projeto
- **API em produção (Swagger):** [Visualizar Documentação](https://fastapi-studies.onrender.com/docs)
- **Repositório GitHub:** [Acessar Código](https://github.com)

---

## Objetivo do projeto
Este projeto tem como objetivo fortalecer conhecimentos em:
- [x] Desenvolvimento de APIs REST com FastAPI
- [x] Criação de endpoints (**GET, POST, PUT, DELETE**)
- [x] Integração com banco de dados **PostgreSQL**
- [x] Versionamento do banco com **Alembic** (migrações)
- [x] Validação e tipagem de dados com **Pydantic**
- [x] Organização profissional de projetos backend
- [x] Uso de documentação automática (**Swagger / Redoc**)
- [x] Testes manuais diretamente pela API

---

## Decisões técnicas
> "A escolha das tecnologias focou em performance, segurança e escalabilidade da aplicação."

| Nome | Tecnologia |
|------|------------|
| API  | FastAPI    |
| DB   | PostgreSQL |
| ORM  | SQLAlchemy |
| Migrações | Alembic |

---

## Tecnologias utilizadas
- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy
- PostgreSQL
- Alembic

---

## Estrutura do projeto
```text
app/
 ├── main.py          # Ponto de entrada da aplicação
 ├── database.py      # Conexão com o banco de dados
 ├── models/          # Models SQLAlchemy
 ├── schemas/         # Schemas Pydantic
 ├── routes/          # Rotas/endpoints da API
 └── __init__.py
```

---

## Banco de dados (PostgreSQL)
O projeto utiliza **PostgreSQL** como banco de dados principal.  
A conexão é feita através de uma URL no formato:  
`postgresql://usuario:senha@host:porta/nome_do_banco`  

### Migrações com Alembic
Todo o controle de criação e atualização do banco é feito com Alembic.  

1. Gere a migração:  
```bash
alembic revision --autogenerate -m "descricao da migracao"
```

2. Aplique no banco:  
```bash
alembic upgrade head
```

---

## Como executar o projeto localmente

1. **Clone o repositório**  
```bash
git clone https://github.com
cd fastapi-studies
```

2. **Ambiente Virtual**  
Linux/Mac:  
`python -m venv venv && source venv/bin/activate`  

Windows:  
`python -m venv venv && venv\Scripts\activate`  

3. **Dependências e Execução**  
```bash
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

---

## Status do projeto
- [x] API funcional  
- [x] Banco de dados integrado  
- [x] Migrações configuradas  
- [x] Documentação automática  
- [x] Deploy em produção  

---

## Autor
**Orlando Conceição Vilhalba de Almeida**

Desenvolvedor Backend em formação, com foco em Python, APIs REST, FastAPI e bancos de dados relacionais.

GitHub: [orlandoconceicao](https://github.com/orlandoconceicao)
