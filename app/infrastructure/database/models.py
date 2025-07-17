from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class MovieModel(Base):
    __tablename__ = "movies"
    imdb_id = Column(String, primary_key=True, index=True)
    title = Column(String)
    year = Column(Integer)
    genre = Column(String)
    director = Column(String)
    actors = Column(String)
    imdb_rating = Column(String)
    plot = Column(String)
    reviews = relationship("ReviewModel", back_populates="movie", cascade="all, delete-orphan")

class ReviewModel(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String)
    opinion = Column(String)
    rating = Column(Integer)
    imdb_id = Column(String, ForeignKey("movies.imdb_id"))
    movie = relationship("MovieModel", back_populates="reviews")
