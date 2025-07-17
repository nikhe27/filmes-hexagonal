from infrastructure.database.repository.repository import MovieRepository

class SearchMovieUseCase:
    def __init__(self, repository: MovieRepository):
        self.repository = repository

    def execute(self, imdb_id: str):
        movie = self.repository.get_by_imdb_id(imdb_id)
        return movie
