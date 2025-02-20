from pathlib import Path
from dotenv import load_dotenv
import os

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