from domain.entities.review import Review

class Movie:
    def __init__(self, imdb_id: str):
        self.imdb_id = imdb_id
        self.reviews = []

    def add_review(self, user_opinion: str, user_rating: int):
        review = Review(user_opinion=user_opinion, user_rating=user_rating)
        self.reviews.append(review)