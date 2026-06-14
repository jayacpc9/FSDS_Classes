import streamlit as st
import MovieRatings as movie_ratings
import ColumnNames as col_names

if "active_button" not in st.session_state:
    st.session_state.active_button = None


def handle_click(clicked_value):
    # Save the clicked button's value into Streamlit's persistent memory
    st.session_state.active_button = clicked_value
    print(f"""Click the button : {clicked_value}""")
    # st.write(f"""Click the button : {clicked_value}""")


def button_list_horizontal(buttons_list):
    # 1. Create a set of columns equal to the number of buttons
    # This forces them to sit horizontally side-by-side
    cols = st.columns(len(buttons_list))

    # 2. Loop through both the columns and the buttons simultaneously
    for col, button in zip(cols, buttons_list):
        with col:  # Target the specific column
            st.button(
                label=f"{button}",
                key=f"tab_btn_{button}",
                on_click=handle_click,
                args=(button,),
                use_container_width=True  # Makes buttons stretch to fill the column nicely
            )


def button_list(buttons_list):
    for button in buttons_list:
        # st.button(f"{button}")
        st.button(
            label=f"{button}",
            key=f"btn_{button}",  # A unique key prevents Streamlit duplicate errors
            on_click=handle_click,
            args=(button,)  # Pass the current item to the callback function
        )


st.title("Streamlit  : Movie Ratings  Demo")
st.write("""This is a sample app to demo using pandas and numpy""")
# movie_ratings.init_movie_df()

movie_genre = st.sidebar.selectbox("Filter by Genre : ", movie_ratings.get_all_genres())
print("movie_genre+"".lower() == ", movie_genre.lower())
selected_genre_text_color = "red"
st.sidebar.write(f"### The genre selected : :{selected_genre_text_color.lower()}[**{movie_genre.title()}**]")

st.write(f"### Most expensive :{selected_genre_text_color.lower()}[**{movie_genre}**] movie is : ",
         movie_ratings.get_most_expensive_movie(movie_genre))
st.write(f"### Least expensive :{selected_genre_text_color.lower()}[**{movie_genre}**] movie is : ",
         movie_ratings.get_least_expensive_movie(movie_genre))
tab_titles = ["Top 10 Movies", f"All {movie_genre} Movies", "Filter by Year"]

tab1, tab2, tab3 = st.tabs(tab_titles)
with tab1:
    st.write(f"## Top 10 movie : ")
    st.write("""by Audience Rating""")
    st.write(movie_ratings.get_top_ten_movies_by_ratings(movie_genre))
with tab2:
    all_movies_df = movie_ratings.get_all_movies_by_genre(movie_genre)
    st.subheader(f"All :{selected_genre_text_color.lower()}[**{movie_genre}**] movie : ")
    st.write(f"Total movies : {len(all_movies_df)}")
    st.write(all_movies_df)
with tab3:
    all_movies_df = movie_ratings.get_all_movies_by_genre(movie_genre)
    # all_movies_df.unique(col_names.YEAR)
    st.subheader(f"Filter by year : ")
    # st.write(f"Total movies : {len(all_movies_df)}")
    unique_year_list = all_movies_df[col_names.YEAR].unique().tolist()
    unique_year_list.sort()
    # print(type(unique_year_list))
    button_list_horizontal(unique_year_list)



    if st.session_state.active_button is not None:
        movies_by_year=all_movies_df[all_movies_df[col_names.YEAR] == st.session_state.active_button]
        # st.success(f"Total movies in {st.session_state.active_button} : {len(movies_by_year)}")
        st.write(f"Total movies in {st.session_state.active_button} : {len(movies_by_year)}")
        st.markdown("<hr style='border: 1px solid red; margin-top: 0;'/>", unsafe_allow_html=True)
        # st.markdown("---")
        # st.divider()
        st.write(movies_by_year)

    # st.write(f"clicked : {st.session_state.active_button }")
