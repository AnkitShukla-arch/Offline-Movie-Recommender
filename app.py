# app.py
import streamlit as st
import pandas as pd
from recommender import load_data, train_model

# Set page title
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

st.title("🎥 Movie Recommendation System")
st.write("Select a movie to get similar movie recommendations.")

# Load dataset
data = load_data('data/ml-100k/u.data')
algo, predictions, rmse = train_model(data)

# Load movie names
movie_titles = pd.read_csv('data/ml-100k/u.item', sep='|', encoding='latin-1', header=None, usecols=[0, 1], names=['movieId', 'title'])

# Let user pick a movie
selected_movie = st.selectbox("Pick a movie:", movie_titles['title'].values)

if st.button("Recommend"):
    movie_id = movie_titles[movie_titles['title'] == selected_movie]['movieId'].values[0]

    # Find users who rated this movie highly
    similar_movies = []
    for _, row in movie_titles.iterrows():
        if row['title'] == selected_movie:
            continue
        pred = algo.predict('user1', row['movieId'])  # fake user for similarity
        similar_movies.append((row['title'], pred.est))
    
    # Sort by predicted rating
    similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    top_5 = similar_movies[:5]

    st.subheader("🎯 Top 5 Recommendations:")
    for title, score in top_5:
        st.write(f"**{title}** — Predicted rating: {score:.2f}")
