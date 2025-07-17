from fastapi import APIRouter, HTTPException
from application.use_cases.create_movie_use_case import CreateMovieUseCase
from infrastructure.database.repository import MovieRepository
from adapters.api.schemas.movie_schema import MovieCreateRequest, MovieResponse

router = APIRouter()

@router.post("/create-movie", response_model=MovieResponse)
def create_movie(movie_request: MovieCreateRequest):
    use_case = CreateMovieUseCase(MovieRepository())
    try:
        movie = use_case.execute(
            imdb_id=movie_request.imdb_id,
            user_opinion=movie_request.user_opinion,
            user_rating=movie_request.user_rating
        )
        return MovieResponse.from_entity(movie)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
