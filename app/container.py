from infrastructure.database.repository.repository import MovieRepository
from infrastructure.database.database import SessionLocal

def get_movie_repository():
    db = SessionLocal()
    return MovieRepository(db)
