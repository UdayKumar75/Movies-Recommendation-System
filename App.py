import streamlit as st
import pickle as pkl
import pandas as pd
import requests
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    dist = similarity[movie_index]
    movies_lists = sorted(list(enumerate(dist)), reverse = True, key = lambda x:x[1])[1:6]

    recommendations = []
    recommended_movies_posters = []
    for i in movies_lists:
        movie_id = movies.iloc[i[0]].movie_id
        recommendations.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommendations, recommended_movies_posters

movies_list = pkl.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)


similarity = pkl.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System")

option = st.selectbox(
    "Which movie do you want to recommend?",
    movies['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(option)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

#8265bd1679663a7ea12ac168da84d2e8

#https://api.themoviedb.org/3/movie/{movie_id}?api_key=<<api_keY>>&language=en-US