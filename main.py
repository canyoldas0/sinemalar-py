from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests
from enum import Enum
from urllib.parse import urljoin
from fastapi import FastAPI

app = FastAPI()

class MovieType(Enum):
    InTheaters = "vizyondakiler"
    ComingSoon = "gelecek-filmler"


class Movie(BaseModel):
    title: str


base_url = "https://www.paribucineverse.com/"


def movie(content):
    movie_name = content.get("data-movie-title")

    return Movie(title=movie_name)


def getMovieListFor(movieType: MovieType):
    url = urljoin(base_url, movieType.value)
    print(url)
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        specific_div = soup.find("div", id="movieListRow")

        if specific_div:
            # Get the contents inside the <div> (can be tags, strings, etc.)
            movie_divs = specific_div.find_all("div", {"data-movie-title": True})
            movies = map(movie, movie_divs)
            return list(movies)
    else:
        return


getMovieListFor(MovieType.ComingSoon)
