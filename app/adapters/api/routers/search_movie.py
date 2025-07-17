from fastapi import APIRouter, HTTPException
from application.use_cases.search_movie_use_case import SearchMovieUseCase
from infrastructure.database.repository import MovieRepository
from adapters.api.schemas.movie_schema import MovieResponse

router = APIRouter()

@router.get("/search-movie", response_model=MovieResponse)
def search_movie(imdb_id: str):
    use_case = SearchMovieUseCase(MovieRepository())
    movie = use_case.execute(imdb_id=imdb_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Filme não encontrado.")
    return MovieResponse.from_entity(movie)
