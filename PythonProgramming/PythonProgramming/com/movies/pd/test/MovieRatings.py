import pandas as pd
import numpy as np

import Configuration as config
import ColumnNames as colnames

movie_rating_df = pd.read_csv(config.movie_rating_file)


def init_movie_df():
    global movie_rating_df
    movie_rating_df = pd.read_csv(config.movie_rating_file)
    print("init_movie_df : ", movie_rating_df)
    print("init_movie_df : ", movie_rating_df.columns)


def update_column_names():
    if (movie_rating_df is not None and not movie_rating_df.empty):
        print("movie_rating_df is not empty :::: ")
        movie_rating_df.columns = [colnames.FILM, colnames.GENRE, colnames.CRITIC_RATING, colnames.AUDIENCE_RATING,
                                   colnames.BUDGET_MILLIONS, colnames.YEAR]
        print("=== Updated columns names == \n", movie_rating_df.columns)
    else:
        print("movie_rating_df is empty :::: ")


def print_details():
    print("Max Year = ", movie_rating_df[colnames.YEAR].max())
    print("Min Year = ", movie_rating_df[colnames.YEAR].min())
    print("Most Expensive = ", movie_rating_df[colnames.BUDGET_MILLIONS].max())
    print("Least Expensive = ", movie_rating_df[colnames.BUDGET_MILLIONS].min())


def get_all_genres():
    # get all the unique Genre from the given csv file.
    # target_genres = movie_rating_df[colnames.GENRE].cat.categories.to_list()
    target_genres = movie_rating_df[colnames.GENRE].unique().tolist()
    # print(target_genres)
    return target_genres


def get_most_expensive_movie(movie_genre):
    # method accepts a movie genre and returns a df containg the most expensive movie.
    pd.set_option("display.expand_frame_repr", False)
    # get the Genres list
    genres_df = movie_rating_df[movie_rating_df[colnames.GENRE] == movie_genre]
    max_budget = genres_df[colnames.BUDGET_MILLIONS].max()
    most_expensive_movie = genres_df.loc[genres_df[colnames.BUDGET_MILLIONS] == max_budget]
    print(type(most_expensive_movie))
    # print(most_expensive_movie,end='\n')
    return most_expensive_movie


def get_least_expensive_movie(movie_genre):
    # method accepts a movie genre and returns a df containg the most expensive movie.
    pd.set_option("display.expand_frame_repr", False)
    # get the Genres list
    genres_df = movie_rating_df[movie_rating_df[colnames.GENRE] == movie_genre]
    min_budget = genres_df[colnames.BUDGET_MILLIONS].min()
    least_expensive_movie = genres_df.loc[genres_df[colnames.BUDGET_MILLIONS] == min_budget]
    print(type(least_expensive_movie))
    # print(most_expensive_movie,end='\n')
    return least_expensive_movie


def get_top_ten_movies_by_ratings(movie_genre):
    pd.set_option("display.expand_frame_repr", False)
    top_ten_movies_df = movie_rating_df.nlargest(10, colnames.AUDIENCE_RATING, keep='all')
    print(top_ten_movies_df)
    return top_ten_movies_df

def get_all_movies_by_genre(movie_genre):
    all_movies = movie_rating_df[movie_rating_df.Genre == movie_genre]
    return all_movies


movie_list = []


def list_all_movies_by_genre(genre):
    # for loop to request all the most expensive movies by the category
    for genre in all_genre:
        most_expensive_movie = get_most_expensive_movie(genre)
        records_hash = most_expensive_movie.to_dict(orient="records")
        movie_list.append(records_hash[0])  # adding the dictionary to the list
        print("records_hash : ",records_hash[0])



##############################################
## To test the working of all the functions ##
##############################################

init_movie_df()
update_column_names()
print_details()

all_genre = get_all_genres()

print("All Unique Genres ::: ", all_genre)
genre = 'Adventure'
most_expensive_movie = get_most_expensive_movie(movie_genre=genre)
print("most_expensive_movie = ", type(most_expensive_movie))

print(f"Most expensive {genre} Film is = ", most_expensive_movie[colnames.FILM].item().strip())
print(f"Least expensive {genre} Film is = ", get_least_expensive_movie(movie_genre=genre))
print(f"Top 10 movies {genre} : ", get_top_ten_movies_by_ratings(movie_genre=genre))

# filter to sort all final result by one of the available categories
sort_by = colnames.BUDGET_MILLIONS
movie_list.sort(key=lambda movie: movie[sort_by])

# iterate the list of dictionary items.
for movie in movie_list:
    for key, val in movie.items():
        print(f"{key} : {val}")
    print()

# print the details in a neat format
print(f"{'Year':<6} |{'GENRE':<12} | {'BUDGET':<6} | {'FILM'}")
print("-" * 60)
for movie in movie_list:
    print(f"{movie['Year']:<6} |{movie['Genre']:<12} | ${movie['BudgetMillions']:<5}M | {movie['Film'].strip()}")

all_movies_df = get_all_movies_by_genre(genre)
print("all movies by gener : ",all_movies_df)
print("type of all movies df : ",type(all_movies_df))
print(f"Filter by year : ",all_movies_df[colnames.YEAR].unique().tolist())