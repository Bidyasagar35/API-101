import json
from urllib import parse, request
import webbrowser

API_KEY = "49210eeb38cf58974e581e3f44ed6ea7"
BASE_URL = "https://api.themoviedb.org/3"

# Search for a movie
def search_movie(title):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": title,
        "language": "en-US"
    }
    query_string = parse.urlencode(params)
    full_url = f"{url}?{query_string}"

    with request.urlopen(full_url) as response:
        data = json.loads(response.read().decode("utf-8"))

    movie = data["results"][0]  # First result                                                                                                                                                                                                                                                                            
    print(f"Title: {movie['title']}")
    print(f"Rating: {movie['vote_average']}/10")
    print(f"Release: {movie['release_date']}")
    print(f"Overview: {movie['overview'][:500]}...")
    print(f"Poster: https://image.tmdb.org/t/p/w500{movie['poster_path']}")
    poster_url = f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
    webbrowser.open(poster_url)

search_movie("Bahubali")