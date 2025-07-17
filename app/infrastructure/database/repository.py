from domain.entities.movie import Movie
from domain.entities.review import Review
from infrastructure.database.database import SessionLocal, MovieModel, ReviewModel


class MovieRepository:
    def save(self, movie: Movie):
        session = SessionLocal()
        try:
            movie_model = MovieModel(
                imdb_id=movie.imdb_id,
                title=movie.title,
                year=movie.year,
                genre=movie.genre,
                director=movie.director
            )
            session.add(movie_model)
            session.flush()  # Garante que o ID seja gerado

            for r in movie.reviews:
                review_model = ReviewModel(
                    opinion=r.user_opinion,
                    rating=r.user_rating,
                    movie_id=movie_model.id
                )
                session.add(review_model)

            session.commit()
        finally:
            session.close()

    def get_by_imdb_id(self, imdb_id: str) -> Movie:
        session = SessionLocal()
        try:
            movie_model = session.query(MovieModel).filter_by(imdb_id=imdb_id).first()
            if not movie_model:
                return None

            movie = Movie(imdb_id=movie_model.imdb_id)
            movie.title = movie_model.title
            movie.year = movie_model.year
            movie.genre = movie_model.genre
            movie.director = movie_model.director

            for r in movie_model.reviews:
                review = Review(user_opinion=r.opinion, user_rating=r.rating)
                movie.reviews.append(review)

            return movie
        finally:
            session.close()