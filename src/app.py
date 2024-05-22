import streamlit as st
import pickle
import pandas as pd
import requests

api_key = 'd9f397a605c439a3b316dc3492e286c2'


movies_dict = pickle.load(open('movies.pkl', 'rb')) # open the file in read mode
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6] 

    recommend_movies = []
    recomended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)  
        #fetch poster from API
        poster = fetch_poster(movie_id)
        recomended_movies_posters.append(poster)

    return recommend_movies, recomended_movies_posters


if st.button('Recommend'):
    st.write('You have selected:', selected_movie_name)
    recommendations, posters = recommend(selected_movie_name)
    st.write('Recommendations are : ')

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])

    with col2:
        st.text(recommendations[1])
        st.image(posters[1])

    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])

    with col5:
        st.text(recommendations[4])
        st.image(posters[4])



    
