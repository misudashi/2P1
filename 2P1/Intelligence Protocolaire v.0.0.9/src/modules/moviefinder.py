from pydorks import GoogleSearch

def search(movie_name: str) -> str:
    movie = GoogleSearch.search(results_len=1, intext=movie_name + " movie", site='drive.google.com')
    return "".join(movie[0].split('&')[0]) if len(movie) == 1 else False


