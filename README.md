# Movie-Recommendation-Using-Machine-Leaning-And-NLP
This is a streamlit web application that can recommend various kinds of similar movies based on an user interest. here is a demo,
link:https://movie-recommendation-saurav.streamlit.app


About Project :
1️⃣ Project Title
Movie Recommendation System 🎥🍿

2️⃣ Project Description
A web application that recommends movies based on a selected movie.
Uses Machine Learning to find similarity between movies.
Fetches movie posters dynamically using The Movie Database (TMDb) API.
Built with Python and Streamlit for interactive UI.
3️⃣ Key Features
Search or select a movie from the database.
Provides top 5 movie recommendations with posters.
Handles missing posters with placeholder images.
Smooth and interactive Streamlit interface.
4️⃣ Technologies Used
Python – Programming language
Pandas – For data manipulation
Pickle – For loading precomputed similarity matrix
Requests – For fetching data from TMDb API
Streamlit – For building the web app
gdown – To download files from Google Drive

5️⃣ How It Works
Load movie list and similarity matrix.
User selects a movie.
Compute similarity scores and recommend top 5 similar movies.
Fetch posters from TMDb API.
Display recommendations in a responsive Streamlit layout.

6️⃣ Installation
git clone <repo_link>
cd <repo_folder>
pip install -r requirements.txt
streamlit run app.py

7️⃣  Future Improvements
Include genre-based filtering.
Add user ratings for more personalized recommendations.
Improve poster loading speed using caching.
