import './App.css';
import React, { useState } from 'react';
import SearchField from "react-search-field";
import MoviesList from './MoviesList';

let movies = [{'name': 'Harry Potter', 'year': 2018, 'imdb_ratings': 7.5, 'metascores': 67, 'movieVotes': '1,23,242', 'movieNumbers': '$13.8M', 'runtimes': 105, 'genres': 'Comedy'}, {'name': 'Harry Potter', 'year': 2018, 'imdb_ratings': 7.5, 'metascores': 67, 'movieVotes': '1,23,242', 'movieNumbers': '$13.8M', 'runtimes': 105, 'genres': 'Comedy'}]

function search(txt) {
  console.log(txt);
  var request = new XMLHttpRequest();
  request.open('GET', 'http://127.0.0.1:5000/api/v1/resources/movies/'+txt, false);
  request.send(null);

  if (request.status === 200) {
    return JSON.parse(request.responseText)
  } else {
    return []
  }
  
}

function App() {

  const [bool, setBool] = useState(true)

  return (
    <div className="app">
      <h3>Search A Movie!</h3>
      <SearchField
        placeholder="Search..."
        onEnter = {(text) => {
          movies = search(text);
          setBool(!bool)}
        }
        onSearchClick = {(text) => {
          search(text);
          setBool(!bool)}
        }
      />
      <MoviesList movies={movies} />
    </div>
  );
}

export default App;
