from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import settings
from infrastructure.database.models import MovieModel, ReviewModel  # Certifique-se de que models.py existe

# URL do banco vinda do .env via config.py
DATABASE_URL = settings.DATABASE_URL 

# Cria o engine e a sessão
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# Função que cria as tabelas no banco
def init_db():
    Base.metadata.create_all(bind=engine)

