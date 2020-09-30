import React from 'react';
import { Table } from 'reactstrap';

class MoviesList extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            list: props.movies,
            colNames: ['Name', 'Year', 'IMDB Ratings', 'Metascores', 'Votes', 'Box Office Gross', 'Runtime(in minutes)', 'Genre']
        };
    }

    componentWillReceiveProps(nextProps) {
        console.log('mounted');
        this.setState({list: nextProps.movies})
    }

    render () {
        return (
            <div className="moviesList" key={this.state.list}>
                <Table bordered responsive>
                    <thead>
                        <tr>
                            {this.state.colNames.map((col, index) => <th key={index}>{col}</th>)}
                        </tr>
                    </thead>
                    <tbody>
                        {this.state.list.map((movie, index) => 
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
}

export default MoviesList;