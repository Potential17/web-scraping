import React from 'react';
import { Table } from 'reactstrap';

function MoviesList ({ movies }) {

    var colNames = ['Name', 'Year', 'IMDB Ratings', 'Metascores', 'Votes', 'Box Office Gross', 'Runtime(in minutes)', 'Genre']

    return (
        <div className="moviesList">
            <Table bordered responsive>
                <thead>
                    <tr>
                        {colNames.map((col, index) => <th key={index}>{col}</th>)}
                    </tr>
                </thead>
                <tbody>
                    {movies.map((movie, index) => 
                        <tr key={index}>
                            <th>{movie.name}</th>
                            <td>{movie.year}</td>
                            <td>{movie.imdb_ratings}</td>
                            <td>{movie.metascores}</td>
                            <td>{movie.movieVotes}</td>
                            <td>{movie.movieNumbers}</td>
                            <td>{movie.runtimes}</td>
                            <td>{movie.genres}</td>
                        </tr>
                    )}
                </tbody>
            </Table>
        </div>
    )
}

export default MoviesList;