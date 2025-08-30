# 🎬 Movie Recommendation System  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)  
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange?logo=jupyter)  
![ML](https://img.shields.io/badge/Machine%20Learning-Recommender%20System-green)  
![Dataset](https://img.shields.io/badge/Dataset-MovieLens-purple)  
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)  

A **machine learning-based movie recommender** that suggests movies based on user preferences, similarity in movie features, and collaborative filtering.  
Built using **MovieLens datasets**, this project combines **Content-Based Filtering** and **Collaborative Filtering** to generate smart, personalized recommendations.  



## 🚀 Features  

✅ **Content-Based Filtering** – Recommends movies similar to a given movie (based on title, genres, etc.)  
✅ **Collaborative Filtering** – Learns from user ratings and preferences to suggest movies  
✅ **Top-N Recommendations** – Generates top trending movies for exploration  
✅ **Genre-Based Filtering** – Lets users filter recommendations by genre  
✅ **Clean & Scalable Notebook Workflow** – Easy to follow and extend  
✅ **Ready for Streamlit Frontend** – Backend logic structured to integrate with a web app  



## 📂 Dataset  

We use the **MovieLens dataset** (`ml-latest-small`) which contains:  
- **movies.csv** → movie metadata (movieId, title, genres)  
- **ratings.csv** → user ratings (userId, movieId, rating, timestamp)  

🔗 [MovieLens Dataset](https://grouplens.org/datasets/movielens/latest/)  



## 🛠️ Tech Stack  

- **Python 3.x**  
- **Pandas** – Data manipulation  
- **NumPy** – Numerical computing  
- **Scikit-learn** – Content-based filtering (cosine similarity, TF-IDF)  
- **Scikit-surprise** – Collaborative filtering (SVD, KNNBaseline)  
- **Jupyter Notebook** – Development and experimentation  



## 📊 Recommendation Approaches  

1. **Content-Based Filtering**  
   - Extracts features like title and genres  
   - Uses **TF-IDF + Cosine Similarity** to recommend similar movies  

2. **Collaborative Filtering**  
   - Leverages user-item rating matrix  
   - Implemented with **SVD (Singular Value Decomposition)** using `scikit-surprise`  

3. **Hybrid System (Future Scope)**  
   - Combine content-based & collaborative methods for better personalization  



## 📸 Demo (Notebook Preview)  

```python
# Example usage
get_recommendations("The Dark Knight", top_n=10)
