from abc import ABC, abstractmethod
from app.domain.entities.movie import Movie

class OmdbProviderPort(ABC):
    @abstractmethod
    def fetch_movie(self, imdb_id: str) -> Movie:
        pass
