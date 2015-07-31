# Movie class from which movie objects are created
class Movie():
    def __init__(self, movie_title, movie_review, poster_image, trailer_youtube, movie_rating):
        self.title = movie_title
        self.review = movie_review
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = movie_rating
