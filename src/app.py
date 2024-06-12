# Importing the necessary libraries
import streamlit as st
import pickle
import pandas as pd
import requests

# API key for the movie database

api_key = 'd9f397a605c439a3b316dc3492e286c2'

# Load the movies data


movies_dict = pickle.load(open('movies.pkl', 'rb')) # open the file in read mode
movies = pd.DataFrame(movies_dict)

# Create the web app
st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)

# Load the similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Function to fetch the poster of the movie
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}') # fetch the data from the API
    data = response.json() # convert the data into json format
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path'] # return the poster path

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0] # get the index of the movie
    distances = similarity[movie_index] # get the similarity of the movie
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  # sort the movies based on similarity

    recommend_movies = [] # list to store recommended movies
    recomended_movies_posters = [] # list to store recommended movies posters
 
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id # get the movie id
        recommend_movies.append(movies.iloc[i[0]].title)   # append the movie title to the list
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



    
