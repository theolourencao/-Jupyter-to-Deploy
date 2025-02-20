from pathlib import Path
from dotenv import load_dotenv
import os
# importa as funções necessárias do SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Caminho absoluto para o .env
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

print(f"Carregando variáveis de: {env_path.resolve()}")

# Verifique se as variáveis foram carregadas
print(f"POSTGRES_USER: {os.getenv('POSTGRES_USER')}")
print(f"POSTGRES_PASSWORD: {os.getenv('POSTGRES_PASSWORD')}")
print(f"POSTGRES_DB: {os.getenv('POSTGRES_DB')}")
print(f"DB_HOST: {os.getenv('DB_HOST')}")
print(f"DB_PORT: {os.getenv('DB_PORT')}")

#cria as variáveis de ambiente
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_name = os.getenv('POSTGRES_DB')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')



# Constrói a URL de conexão do banco de dados usando as variáveis de ambiente.
DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

print(f"DATABASE_URL: {DATABASE_URL}")

# Cria um motor de banco de dados SQLAlchemy que gerencia as conexões à base de dados.
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões do SQLAlchemy que será usada para criar sessões.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Cria uma classe base declarativa para os modelos do SQLAlchemy.
Base = declarative_base()


# Define uma função geradora que fornece uma sessão de banco de dados e garante o fechamento da sessão.
def get_db():
    db = SessionLocal()  # Cria uma instância da sessão de banco de dados.
    try:
        yield db  # Fornece a sessão para a operação (utilizado em dependências do FastAPI).
    finally:
        db.close()  # Garante que a sessão seja fechada após o uso.
