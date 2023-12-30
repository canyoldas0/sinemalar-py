from fastapi import FastAPI
from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests
from enum import Enum
from urllib.parse import urljoin


app = FastAPI()


class MovieType(Enum):
    InTheaters = "vizyondakiler"
    ComingSoon = "gelecek-filmler"


class Movie(BaseModel):
    title: str
    time: str
    movie_type: str


baseUrl = "https://www.paribucineverse.com/"


def getMovieListFor(movieType: MovieType):
    response = requests.get(baseUrl.join(movieType.value))
    movies_list = []  # List to store movie objects
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        specific_div = soup.find("div", id="movieListRow")

        if specific_div:
            # Get the contents inside the <div> (can be tags, strings, etc.)

            movie_divs = specific_div.find_all("div", {"data-movie-title": True})

            for movie_div in movie_divs:
                # Extract the value of the 'movie-name' attribute
                movie_name = movie_div.get("data-movie-title")

                movie_info = movie_div.find("div", class_="movie-info")

                movie_time = movie_info.find("p", class_="movie-time mb-0")
                movie_type = movie_info.find("p", class_="movie-type mb-0")

                print(movie_time.text)
                print(movie_type.text)
                print(movie_name)
    else:
        return []
