import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import json
import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True

# pages = [51]
# for i in range(1,198):
#       pages.append(pages[i-1] + 50)
# pages = [str(i) for i in pages]


# names = []
# years = []
# imdb_ratings = []
# metascores = []
# movieVotes = []
# movieGross = []
# runtimes = []
# genres = []

movies = []

# for page in pages:
response = requests.get('http://www.imdb.com/search/title?release_date=2018-01-01,2019-10-31&sort=num_votes,desc&start=1&ref_=adv_nxt')

page_html = BeautifulSoup(response.text, 'html.parser')

mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

# Extract data from individual movie container
for container in mv_containers:
    movie_data = {}
    # If the movie has Metascore, then extract:
    if container.find('div', class_ = 'ratings-metascore') is not None:
        # The name
        movie_data['name'] = container.h3.a.text
        # names.append(name)
        # The year
        year = container.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
        a = re.search(r"[0-9]{1}.+[0-9]", year).group(0)
        # years.append(a)
        movie_data['year'] = a

        # The IMDB rating
        imdb = float(container.strong.text)
        # imdb_ratings.append(imdb)
        movie_data['imdb_ratings'] = imdb
        # The Metascore
        m_score = container.find('span', class_ = 'metascore').text
        # metascores.append(int(m_score))
        movie_data['metascores'] = m_score.strip()
        # The number of votes and gross
        movieNumbers = container.find_all("span", attrs={"name": "nv"})
        if len(movieNumbers) == 2:
            # movieVotes.append(movieNumbers[0].text)
            movie_data['movieVotes'] = movieNumbers[0].text
            # movieGross.append(movieNumbers[1].text)
            movie_data['movieNumbers'] = movieNumbers[1].text
        elif len(movieNumbers) == 1:
            # movieVotes.append(movieNumbers[0].text)
            # movieGross.append(None)
            # movieVotes.append(movieNumbers[0].text)
            movie_data['movieVotes'] = movieNumbers[0].text
            # movieGross.append(movieNumbers[1].text)
            movie_data['movieNumbers'] = None
        else:
            movie_data['movieVotes'] = None
            movie_data['movieNumbers'] = None
        # runtime
        runtime = container.p.find('span', class_ = 'runtime').text
        pl = runtime.split(" ", 1)
        # runtimes.append(pl[0])
        movie_data['runtimes']=pl[0]
        #Genre
        genre = container.p.find('span', class_ = 'genre').text.strip()
        ab = genre.split(",")
        # genres.append(ab[0])
        movie_data['genres'] = ab
        movie_data_keys = list(movie_data.keys())
        movies.append(movie_data)

# test_df = pd.DataFrame({'movie': names,
# 'year': years,
# 'imdb': imdb_ratings,
# 'metascore': metascores,
# 'votes': movieVotes,
# 'gross': movieGross,
# 'runtime (mins)': runtimes,
# 'Genre': genres
#     })

# test_df.to_csv('imdb.csv', index = False, encoding = 'utf-8')

# filename = 'movies.csv'
# with open(filename, 'w', newline='') as f: 
#     w = csv.DictWriter(f,movie_data_keys) 
#     w.writeheader() 
#     for movie in movies: 
#         w.writerow(movie) 

# with open('movies.json', 'w') as fout:
#     json.dump(movies , fout)






@app.route('/', methods=['GET'])
def home():
    return ''' A prototype API for scraping movie data from imdb pages'''

@app.route('/api/v1/resources/movies/all', methods=['GET'])
def api_all():
    return jsonify(movies)


app.run()