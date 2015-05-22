"""This module defines the Video and Movie classes."""

# The video class contains the title, duration and release date of a video.
class Video():
    """The Video class provides a way to store video related information."""
    def __init__(self, video_title, video_release_date, video_duration):
        self.title = video_title
        self.release_date = video_release_date
        self.duration = video_duration

# The movie class contains the storyline, poster image, and Youtube trailer URL.
# It also inherits the title and duration from the Video class.
class Movie(Video):
    """This Movie class provides a way to store movie related information."""

    def __init__(self, video_title, video_release_date, video_duration, movie_storyline,
                 movie_poster_image_url, movie_youtube_trailer_url):
        Video.__init__(self, video_title, video_release_date, video_duration)
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_youtube_trailer_url
