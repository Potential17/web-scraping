import './App.css';
import React from 'react';
import SearchField from "react-search-field";
import MoviesList from './MoviesList';

var movies = [{'name': 'Harry Potter', 'year': 2018, 'imdb_ratings': 7.5, 'metascores': 67, 'movieVotes': '1,23,242', 'movieNumbers': '$13.8M', 'runtimes': 105, 'genres': 'Comedy'}, {'name': 'Harry Potter', 'year': 2018, 'imdb_ratings': 7.5, 'metascores': 67, 'movieVotes': '1,23,242', 'movieNumbers': '$13.8M', 'runtimes': 105, 'genres': 'Comedy'}]

function search(txt) {
  console.log(txt);
  movies = [];
}

function App() {
  return (
    <div className="app">
      <h3>Search A Movie!</h3>
      <SearchField
        placeholder="Search..."
        onEnter = {search}
        onSearchClick = {search}
      />
      <MoviesList movies={movies} />
    </div>
  );
}

export default App;
