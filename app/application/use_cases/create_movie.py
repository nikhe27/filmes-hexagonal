from domain.entities.movie import Movie
from infrastructure.database.repository.repository import MovieRepository

class CreateMovieUseCase:
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def execute(self, imdb_id: str, user_opinion: str, user_rating: int):
        movie = Movie(imdb_id=imdb_id)
        movie.fetch_data_from_omdb()
        movie.add_review(user_opinion=user_opinion, user_rating=user_rating)
        self.repository.save(movie)
        return movie
