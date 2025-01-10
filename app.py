import pickle
import streamlit as st
import requests

st.header("Movie Recommendation System Using Machine Learning")

movies = pickle.load(open('artificats/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artificats/similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movie_list
)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/movie_id?language=en-US"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_moview_name = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_moview_name.append(movies.iloc[i[0]].title)
    return recommended_moview_name, recommended_movies_poster
if st.button('Show recommendation'):
    recommended_moview_name, recommended_movies_poster = recommend(selected_movie)