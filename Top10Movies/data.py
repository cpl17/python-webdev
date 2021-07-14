import requests 
from collections import namedtuple
import pprint

APIKEY = "1fd1e88cda34e0219d47cfb2b0c57245"
APIREAD = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxZmQxZTg4Y2RhMzRlMDIxOWQ0N2NmYjJiMGM1NzI0NSIsInN1YiI6IjYwMjU1YTEwNmEzNDQ4MDAzZDEyZjUzMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zptZo1oYD9YNf_EF1b77VYmhFwjZvh8ZA-eL9g93yvA"

SEARCHURL = "https://api.themoviedb.org/3/search/movie"
IMAGEURL = "https://image.tmdb.org/t/p/original"
DETAILSURL = "https://api.themoviedb.org/3/movie/"


def get_selection_options(title):

    params = {
            "api_key": APIKEY,
            "query": title
        }


    response = requests.get(url=SEARCHURL,params=params)
    data = response.json()

    MovieBasic = namedtuple("Movie","title, year, id")

    movies_to_select = []

    for movie in data["results"]:
        title = movie["original_title"]
        year = movie["release_date"]
        movie_id = movie["id"]
        movies_to_select.append(MovieBasic._make([title,year,movie_id]))

    return movies_to_select


def get_movie_details(movie_id):

    

    params = {
        "api_key":APIKEY
    }

    response = requests.get(url = f"{DETAILSURL}{movie_id}", params=params)
    data = response.json()

    MovieDetails = namedtuple("Movie","title, image_url, year, description")

    title =  data["original_title"]
    imgage_url = IMAGEURL + data["poster_path"]
    year = data['release_date'].split("-")[0]
    description = data["overview"]

    return MovieDetails._make([title,imgage_url,year,description])











