import pickle
import streamlit as st
import requests
import pandas as pd
import os
import gdown
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# -------------------
# Helper functions
# -------------------

session = requests.Session()
retry = Retry(connect=3, backoff_factor=2)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=dac548a0b2305fb8d480ab0c5706e198&language=en-US"
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie_id {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Poster+Unavailable"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies_name = []
    recommended_movies_poster = []
    
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]]['movie_id']
        recommended_movies_name.append(movies.iloc[i[0]].title)
        poster = fetch_poster(movie_id)
        recommended_movies_poster.append(poster)
        
    return recommended_movies_name, recommended_movies_poster

# -------------------
# Streamlit App
# -------------------

st.header("🎥 Movie 🍿 Recommendation System Using Machine Learning")

os.makedirs("artificats", exist_ok=True)

# Google Drive file IDs
MOVIE_CSV_ID = "1dO3JgjqjsjsJVkV6tzrWbqK5aTM2UV9i"
SIMILARITY_ID = "1K26kNl2FRDjiZszawcdGzt-dKJ6Ohu7w"

movie_csv_path = "artificats/movie_list.csv"
similarity_path = "artificats/similarity.pkl"

# Download CSV if not exists
if not os.path.exists(movie_csv_path):
    with st.spinner("Downloading movie_list.csv..."):
        url_csv = f"https://drive.google.com/uc?id={MOVIE_CSV_ID}"
        gdown.download(url_csv, movie_csv_path, quiet=False)

# Download similarity if not exists
if not os.path.exists(similarity_path):
    with st.spinner("Downloading similarity.pkl..."):
        url_sim = f"https://drive.google.com/uc?id={SIMILARITY_ID}"
        gdown.download(url_sim, similarity_path, quiet=False)

# Load movie list
try:
    movies = pd.read_csv(movie_csv_path)
except Exception as e:
    st.error(f"Error loading movie_list.csv: {e}")
    st.stop()

# Load similarity
try:
    with open(similarity_path, "rb") as f:
        similarity = pickle.load(f)
except Exception as e:
    st.error(f"Error loading similarity.pkl: {e}")
    st.stop()

# Movie selection
movies_list = movies['title'].values
selected_movie = st.selectbox(
    'Type or select a movie to get recommendation',
    movies_list
)

if st.button('SHOW RECOMMENDATION'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        col.text(recommended_movies_name[i])
        if recommended_movies_poster[i]:
            col.image(recommended_movies_poster[i])
