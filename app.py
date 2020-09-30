import flask
from flask import request, jsonify,redirect,url_for

from imdb import scrapper


app = flask.Flask(__name__)
app.config["DEBUG"] = True



# Route for the home page 

@app.route('/', methods=['GET'])
def home():
    return ''' A prototype API for scraping movie data from imdb pages'''


# this route returns the search results which matched the searchquery
@app.route('/api/v1/resources/movies/<string:searchquery>', methods=['GET','POST'])
def searchresults(searchquery):
    movies = scrapper(searchquery)
    return jsonify(movies)


if __name__ == "__main__": 
    app.run()