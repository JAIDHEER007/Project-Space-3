import requests
import urllib.parse
import json

class MovieDatabase:
    url = 'https://moviesdatabase.p.rapidapi.com/titles/search/title/{title}'
    headers = {
        'X-RapidAPI-Key': '<LOL Do u think this is true>dhsvauaasu23984y21ebw28evuev', 
        'X-RapidAPI-Host': 'moviesdatabase.p.rapidapi.com'
    }
    params = {
        'exact': True,
        'titleType': 'movie',
        'limit':1
    }

    def __make_request(title):
        response = requests.get(MovieDatabase.url.format(title = urllib.parse.quote(title)), 
                                params = MovieDatabase.params, 
                                headers = MovieDatabase.headers)
        
        return json.loads(response.text) if response.status_code == 200 else {}


    def __init__(self, movies):
        self.__movies = movies
    
    def perform(self) -> list:
        recomended_movies = []

        for movie in self.__movies:
            response = MovieDatabase.__make_request(movie[1])
            url = None
            try: 
                url = response['results'][0]['primaryImage']['url']
            except Exception: pass
            recomended_movies.append([movie, url])

        return recomended_movies



