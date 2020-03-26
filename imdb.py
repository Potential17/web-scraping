import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re

pages = [51]
for i in range(1,198):
      pages.append(pages[i-1] + 50)
pages = [str(i) for i in pages]


names = []
years = []
imdb_ratings = []
metascores = []
movieVotes = []
movieGross = []
runtimes = []
genres = []

for page in pages:
    response = requests.get('http://www.imdb.com/search/title?release_date=2018-01-01,2019-10-31&sort=num_votes,desc&start=' + page +
        '&ref_=adv_nxt')

    page_html = BeautifulSoup(response.text, 'html.parser')

    mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

# Extract data from individual movie container
    for container in mv_containers:
        # If the movie has Metascore, then extract:
        if container.find('div', class_ = 'ratings-metascore') is not None:
            # The name
            name = container.h3.a.text
            names.append(name)
            # The year
            year = container.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
            a = re.search(r"[0-9]{1}.+[0-9]", year).group(0)
            years.append(a)

            # The IMDB rating
            imdb = float(container.strong.text)
            imdb_ratings.append(imdb)
            # The Metascore
            m_score = container.find('span', class_ = 'metascore').text
            metascores.append(int(m_score))
            # The number of votes and gross
            movieNumbers = container.find_all("span", attrs={"name": "nv"})
            if len(movieNumbers) == 2:
            	movieVotes.append(movieNumbers[0].text)
            	movieGross.append(movieNumbers[1].text)
            elif len(movieNumbers) == 1:
            	movieVotes.append(movieNumbers[0].text)
            	movieGross.append(np.nan)
            else:
            	movieVotes.append(np.nan)
            	movieGross.append(np.nan)
            # runtime
            runtime = container.p.find('span', class_ = 'runtime').text
            pl = runtime.split(" ", 1)
            runtimes.append(pl[0])
            #Genre
            genre = container.p.find('span', class_ = 'genre').text
            ab = genre.split(",", 1)
            genres.append(ab[0])

test_df = pd.DataFrame({'movie': names,
'year': years,
'imdb': imdb_ratings,
'metascore': metascores,
'votes': movieVotes,
'gross': movieGross,
'runtime (mins)': runtimes,
'Genre': genres
    })

test_df.to_csv('imdb.csv', index = False, encoding = 'utf-8')
