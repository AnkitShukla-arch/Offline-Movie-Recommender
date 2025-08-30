# 🎬 Movie & Web Series Recommender System  

A machine learning project that recommends **movies** and **web series** based on user input and past ratings.  
The system uses **content-based filtering** and **collaborative filtering** to generate personalized recommendations.  

---

## 🚀 Features  

### 🎥 Movie Recommender  
- Search a movie title → get **top 10 similar movies**  
- **Content-based filtering** → uses genres, metadata, and similarity  
- **Collaborative filtering** → based on MovieLens ratings (using `scikit-surprise`)  
- **Top-N recommendation system** → shows highest-rated movies  
- **Trending movies** section  

### 📺 Web Series Recommender  
- Works the same way as the movie recommender  
- Provides **content-based** recommendations for series  

---

## 📂 Dataset  

- **MovieLens (ml-latest-small)** → Movies and ratings dataset  
  🔗 [Download MovieLens Dataset](https://grouplens.org/datasets/movielens/)  

---

## ⚙️ Installation  

--> pip install -r requirements.txt
--> pip install scikit-learn
--> pip install pandas
--> pip install scikit-surprise
--> pip install numpy
--> pip install matplotlib

## git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

## python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows



