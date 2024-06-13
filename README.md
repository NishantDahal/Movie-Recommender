# Movie-Recommender
<a href="https://huggingface.co/spaces/NishantD/Movie_Recommender"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Model_Card-Huggingface-orange"></a>

This project implements a movie recommender system using TMDB movie data and includes an exploratory data analysis (EDA) of the dataset.

## **Dataset**
The movie data used for this project was downloaded from the TMDB Movie Metadata dataset on Kaggle.

## **Deployed Model**
This project also includes a deployed model on Hugging Face: [Movie Recommender](https://huggingface.co/spaces/NishantD/Movie_Recommender)

## **Getting Started**
This recommender system uses Python libraries. To run the application locally, you'll need to set up a virtual environment. Here are the instructions for creating a virtual environment:

### **Using pip**
1. Open your terminal or command prompt.
2. Install venv if you haven't already: `python -m ensurepip install venv`
3. Create a virtual environment named `movie_rec_env`: `python -m venv movie_rec_env`
4. Activate the virtual environment:
   - **Windows:** `movie_rec_env\Scripts\activate`
   - **macOS/Linux:** `source movie_rec_env/bin/activate`

### **Using conda**
1. Open your terminal or command prompt.
2. Create a virtual environment named `movie_rec_env`: `conda create -n movie_rec_env python=3.x` (Replace `3.x` with your desired Python version)
3. Activate the virtual environment: `conda activate movie_rec_env`

### **Installing Dependencies**
1. Once your virtual environment is activated, navigate to the project directory in your terminal.
2. Install the required libraries listed in `requirements.txt`: `pip install -r requirements.txt`

### **Running the Application**
1. After installing the dependencies, run the application using: `streamlit run app.py`
2. This will start the movie recommender system. You'll be able to interact with the application to receive movie recommendations based on your preferences.

## **Project Structure**
- **app.py:** The main application file containing the Streamlit code for the movie recommender system.
- **train.ipynb:** Jupyter notebook containing the code for training the recommendation model.
- **mini-projecteda.ipynb:** Jupyter notebook containing the exploratory data analysis (EDA) of the TMDB movie dataset.
- **movies.pkl:** Pickle file containing the movies data.
- **similarity.pkl:** Pickle file containing the similarity matrix.
- **requirements.txt:** A file listing the required Python libraries.

## **How It Works**
- **Loading Data:** The application loads movie data and a similarity matrix from precomputed pickle files.
- **User Input:** Users can select a movie from a dropdown menu.
- **Recommendations:** Upon clicking the 'Recommend' button, the system fetches and displays the top 5 movie recommendations along with their posters using the TMDB API.

## **Training the Model**
The training process is detailed in the `train.ipynb` Jupyter notebook. Below is a summary of the steps involved:

1. **Data Loading:** The TMDB movie and credits data are loaded and merged on the 'title' column.
2. **Data Cleaning:**
   - Dropping rows with missing values.
   - Extracting relevant columns: movie_id, title, overview, genres, keywords, cast, crew.
   - Converting genres, keywords, cast, and crew from string to list format for better manipulation.
3. **Data Preparation:**
   - Extracting the top 3 actors for the cast.
   - Extracting the director from the crew.
   - Converting the overview into a list of words.
   - Removing spaces and converting to lowercase for uniformity.
4. **Feature Engineering:**
   - Combining overview, genres, keywords, cast, and crew into a single 'tags' column.
   - Converting 'tags' into a single string.
   - Applying stemming to reduce words to their root form.
5. **Vectorization:** Using CountVectorizer to convert text data into numerical data (vectors) with a maximum of 5000 features and removing English stop words.
6. **Similarity Calculation:** Computing cosine similarity between movie vectors to measure similarity.
7. **Recommendation Function:** Creating a function to recommend movies based on cosine similarity.
8. **Model Saving:** Saving the processed movie data and similarity matrix using pickle.

## **Running the Training Notebook**
1. Ensure you have Jupyter Notebook installed and your virtual environment activated.
2. Open the `train.ipynb` file in Jupyter Notebook.
3. Run the notebook cells to train the model and save the outputs.

## **Exploratory Data Analysis (EDA)**
The EDA process is detailed in the `mini-projecteda.ipynb` Jupyter notebook. Below is a summary of the steps involved:

1. **Data Loading:** The TMDB movie and credits data are loaded into Pandas DataFrames.
2. **Data Examination:**
   - Viewing the first few rows of the datasets.
   - Checking for missing values and duplicates.
   - Descriptive statistics of the datasets.
3. **Data Cleaning:**
   - Dropping unnecessary columns.
   - Handling missing values and duplicates.
   - Converting data types for consistency.
4. **Feature Engineering:**
   - Extracting lead actor and crew size.
   - Binning budget values.
   - Calculating profit from revenue and budget.
   - Extracting genre and production company names.
5. **Data Visualization:**
   - Bar plots for top 10 movies by cast and crew size.
   - Distribution plots for budgets and revenues.
   - Scatter plots for profit vs. budget.
   - Line plots for the number of movies released per year.
   - Heatmap for correlation matrix of numerical columns.
   - Pair plots for numerical columns.
6. **Insights:**
   - Distribution of movie genres and production companies.
   - Analysis of top revenue and profit-generating movies.
   - Analysis of vote count and popularity by production company.

## **Running the EDA Notebook**
1. Ensure you have Jupyter Notebook installed and your virtual environment activated.
2. Open the `mini-projecteda.ipynb` file in Jupyter Notebook.
3. Run the notebook cells to perform the exploratory data analysis and visualize the insights.

## **API Key**
Make sure to replace the placeholder `api_key` in `app.py` with your actual TMDB API key.

Enjoy your movie recommendations and data exploration!
