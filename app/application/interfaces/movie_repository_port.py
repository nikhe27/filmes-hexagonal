from abc import ABC, abstractmethod
from domain.entities.movie import Movie
from domain.entities.review import Review

class MovieRepositoryPort(ABC):
    @abstractmethod
    def get_by_imdb_id(self, imdb_id: str) -> Movie | None:
        pass

    @abstractmethod
    def save(self, movie: Movie) -> None:
        pass
