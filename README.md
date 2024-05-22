# Movie-Recommender
<a href="https://huggingface.co/spaces/NishantD/Movie_Recommender"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Model_Card-Huggingface-orange"></a> 



This project implements a movie recommender system using TMDB movie data. 

**Dataset:**

The movie data used for this project was downloaded from the [TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) dataset on Kaggle.

**Deployed Model:**

This project also includes a deployed model on Hugging Face: [Movie Recommender](https://huggingface.co/spaces/NishantD/Movie_Recommender)

**Getting Started**

This recommender system uses Python libraries. To run the application locally, you'll need to set up a virtual environment. Here are the instructions for creating a virtual environment:

**Using pip:**

1. Open your terminal or command prompt.
2. Install `venv` if you haven't already: `python -m ensurepip install venv`
3. Create a virtual environment named `movie_rec_env`: `python -m venv movie_rec_env`
4. Activate the virtual environment:
    - Windows: `movie_rec_env\Scripts\activate`
    - macOS/Linux: `source movie_rec_env/bin/activate`

**Using conda:**

1. Open your terminal or command prompt.
2. Create a virtual environment named `movie_rec_env`: `conda create -n movie_rec_env python=3.x` (Replace `3.x` with your desired Python version)
3. Activate the virtual environment: `conda activate movie_rec_env`

**Installing Dependencies:**

1. Once your virtual environment is activated, navigate to the project directory in your terminal.
2. Install the required libraries listed in `requirements.txt`: `pip install -r requirements.txt`

**Running the Application:**

1. After installing the dependencies, run the application using: `python app.py`

This will start the movie recommender system. You'll be able to interact with the application to receive movie recommendations based on your preferences.
