import csv
import requests
from bs4 import BeautifulSoup
# import pandas as pd
# import numpy as np
import re
import json






def scrapper(searchquery):
    
    response = requests.get('https://www.imdb.com/search/title/?title='+searchquery+'&start=1&ref_=adv_nxt')
    movies = []

    page_html = BeautifulSoup(response.text, 'html.parser')

    mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

    # Extract data from individual movie container
    for container in mv_containers:
        movie_data = {}
        
        # If the movie has Metascore, then extract:
        if container.find('div', class_ = 'ratings-metascore') is not None:
            
            # The name
            movie_data['name'] = container.h3.a.text
           
            # The year
            year = container.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
            a = re.search(r"[0-9]{1}.+[0-9]", year).group(0)
            movie_data['year'] = a

            # The IMDB rating
            imdb = float(container.strong.text)
            movie_data['imdb_ratings'] = imdb
            
            # The Metascore
            m_score = container.find('span', class_ = 'metascore').text
            movie_data['metascores'] = m_score.strip()
            
            # The number of votes and gross
            movieNumbers = container.find_all("span", attrs={"name": "nv"})
            
            if len(movieNumbers) == 2:
                movie_data['movieVotes'] = movieNumbers[0].text
                movie_data['movieNumbers'] = movieNumbers[1].text
                
            elif len(movieNumbers) == 1:
                movie_data['movieVotes'] = movieNumbers[0].text
                movie_data['movieNumbers'] = None
                
            else:
                movie_data['movieVotes'] = None
                movie_data['movieNumbers'] = None
                
                
            # runtime
            runtime = container.p.find('span', class_ = 'runtime').text
            pl = runtime.split(" ", 1)
            movie_data['runtimes']=pl[0]
            
            #Genre
            genre = container.p.find('span', class_ = 'genre').text.strip()
            ab = genre.split(",")
            movie_data['genres'] = ab
            movie_data_keys = list(movie_data.keys())
            
            # appending the scraped data to the list
            movies.append(movie_data)

    return movies





