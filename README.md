# 🎬 Movies Recommendation System

[🔗 View Notebook](https://github.com/UdayKumar75/Movies-Recommendation-System/blob/main/Movies%20Recommendation%20System.ipynb)

A simple content-based movie recommendation system that suggests similar movies based on user input using cosine similarity and NLP techniques.

---

## 📌 Overview

This project is a **content-based recommendation system** built using Python and Jupyter Notebook. It recommends movies based on textual similarity of movie metadata such as genres, keywords, cast, and crew using **Natural Language Processing** techniques and **cosine similarity**.

---

## ⚙️ Features

- Suggests top 5 similar movies based on selected movie
- Uses `cosine similarity` to measure content closeness
- Built using a cleaned dataset from **TMDB** (The Movie Database)
- Processes and combines genres, keywords, cast, and crew into a single "tags" feature
- Provides accurate and relevant movie suggestions

---

## 🛠️ Tech Stack

- **Python**  
- **Jupyter Notebook**
- **Libraries:** Pandas, NumPy, Scikit-learn (TfidfVectorizer), NLTK
- **NLP Techniques:** Tokenization, Stemming, Stopword Removal, TF-IDF
- **Similarity Metric:** Cosine Similarity

---

## 📈 How It Works

1. **Data Loading:** Uses a preprocessed dataset of popular movies.
2. **Feature Engineering:** Combines multiple content features (`genres`, `keywords`, `cast`, `crew`) into a unified `tags` column.
3. **Text Preprocessing:** Applies NLP techniques to clean and standardize the tags.
4. **Vectorization:** Converts text into numerical vectors using `TfidfVectorizer`.
5. **Similarity Calculation:** Uses `cosine similarity` to find the most similar movies based on the vector representation.
6. **Recommendation:** Returns the top 5 most similar movies for any given input.

---

## ✅ Sample Output

Input: `Inception`  
Output:  
- Interstellar  
- The Prestige  
- The Matrix  
- Shutter Island  
- Memento  

---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/UdayKumar75/Movies-Recommendation-System.git
   ```
2. Open the Jupyter Notebook:
   ```bash
   cd Movies-Recommendation-System
   jupyter notebook
   ```
3. Run the notebook: `Movies Recommendation System.ipynb`

---

## 📂 Dataset

- Source: [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)  
- Includes metadata like genres, cast, crew, and keywords

---

## 💡 Future Improvements

- Deploy as a web app using **Streamlit** or **Flask**
- Add collaborative filtering model
- Integrate with real-time APIs (e.g., TMDB API)
- Add user rating functionality

---

## 🙋‍♂️ Author

**Uday Kumar**  
[LinkedIn](https://www.linkedin.com/in/uday-kumar-contact)

---

⭐ If you found this useful, give it a star!  
