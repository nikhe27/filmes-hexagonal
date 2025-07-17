from application.interfaces.movie_repository_port import MovieRepositoryPort
from domain.entities.movie import Movie
from domain.entities.review import Review
from infrastructure.database.database import SessionLocal
from infrastructure.database.models import MovieModel, ReviewModel

class MovieRepository(MovieRepositoryPort):
    def get_movie_by_imdb_id(self, imdb_id: str) -> Movie | None:
        db = SessionLocal()
        try:
            db_movie = db.query(MovieModel).filter_by(imdb_id=imdb_id).first()
            if not db_movie:
                return None
            return Movie(
                imdb_id=db_movie.imdb_id,
                title=db_movie.title,
                year=db_movie.year,
                genre=db_movie.genre,
                director=db_movie.director,
                actors=db_movie.actors.split(",") if db_movie.actors else [],
                imdb_rating=db_movie.imdb_rating,
                plot=db_movie.plot,
                reviews=[
                    Review(user=r.user, opinion=r.opinion, rating=r.rating)
                    for r in db_movie.reviews
                ]
            )
        finally:
            db.close()

    def save_movie(self, movie: Movie):
        db = SessionLocal()
        try:
            db_movie = db.query(MovieModel).filter_by(imdb_id=movie.imdb_id).first()
            if not db_movie:
                db_movie = MovieModel(imdb_id=movie.imdb_id)

            db_movie.title = movie.title
            db_movie.year = movie.year
            db_movie.genre = movie.genre
            db_movie.director = movie.director
            db_movie.actors = ",".join(movie.actors)
            db_movie.imdb_rating = movie.imdb_rating
            db_movie.plot = movie.plot

            db.query(ReviewModel).filter_by(imdb_id=movie.imdb_id).delete()
            db_movie.reviews = [
                ReviewModel(user=r.user, opinion=r.opinion, rating=r.rating)
                for r in movie.reviews
            ]

            db.add(db_movie)
            db.commit()
        finally:
            db.close()
