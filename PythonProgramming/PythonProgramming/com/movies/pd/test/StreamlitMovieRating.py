import streamlit as st
import MovieRatings as movie_ratings
import ColumnNames as col_names

st.title("Streamlit  : Movie Ratings  Demo")
st.write("""This is a sample app to demo using pandas and numpy""")
# movie_ratings.init_movie_df()

movie_genre = st.sidebar.selectbox("Filter by Genre : ", movie_ratings.get_all_genres())
print("movie_genre+"".lower() == ", movie_genre.lower())
selected_genre_text_color = "red"
st.sidebar.write(f"### The genre selected : :{selected_genre_text_color.lower()}[**{movie_genre.title()}**]")

st.write(f"### Most expensive :{selected_genre_text_color.lower()}[**{movie_genre}**] movie is : ",movie_ratings.get_most_expensive_movie(movie_genre))
st.write(f"### Least expensive :{selected_genre_text_color.lower()}[**{movie_genre}**] movie is : ",movie_ratings.get_least_expensive_movie(movie_genre))
tab_titles=["Top 10 Movies", f"All {movie_genre} Movies"]

tab1, tab2 =st.tabs(tab_titles)
with tab1:
    st.write(f"## Top 10 movie : ")
    st.write("""by Audience Rating""")
    st.write(movie_ratings.get_top_ten_movies_by_ratings(movie_genre))
with tab2:
    all_movies_df=movie_ratings.get_all_movies_by_genre(movie_genre)
    st.subheader(f"All :{selected_genre_text_color.lower()}[**{movie_genre}**] movie : ")
    st.write(f"Total movies : {len(all_movies_df)}")
    st.write(all_movies_df)


