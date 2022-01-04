import pandas
from argparse import ArgumentParser
import sys 

def best_movies(movies_path, ratings_path):
    """This function takes two arguments and merges them to find the average ratings for movies.
    
    Args:
        movie_path (path to movies csv)
        rating_path (path to ratings csv)
    
    Returns:
        Average movie ratings from highest to lowest."""
    result = pandas.merge(pandas.read_csv(movies_path), pandas.read_csv(ratings_path), left_on = "movie id", right_on= "item id", how = "inner")
    mov_rate = result[["movie title", "rating"]].groupby(["movie title"]).mean("rating")
    my_series = mov_rate.squeeze()
    return my_series.sort_values(ascending=False)
    
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: the parsed command-line arguments as a namespace with
        variables movie_csv and rating_csv.
    """
    parser = ArgumentParser()
    parser.add_argument("movie_csv", help="CSV containing movie data")
    parser.add_argument("rating_csv", help="CSV containing ratings")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    movies = best_movies(args.movie_csv, args.rating_csv)
    print(movies.head())