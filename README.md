# 🎥 YouTube Video Recommendation System (Content-Based Filtering)

This project builds a **content-based video recommendation system** using YouTube trending videos dataset.  
It recommends similar videos based on the content — specifically the **title**, **description**, and **tags** using NLP techniques.

---

## 📦 Dataset

- Source: [YouTube Trending Videos Dataset - Kaggle](https://www.kaggle.com/datasets/datasnaek/youtube-new)
- File used: `USvideos.csv`

---

## 🧰 Technologies Used

- `pandas`, `numpy`
- `sklearn` (TF-IDF, cosine similarity)
- `matplotlib`, `wordcloud` for visualization

---

## 🔍 Project Steps

1. Loaded the dataset and selected `title`, `description`, and `tags`.
2. Preprocessed the text and merged features into one `text` column.
3. Applied **TF-IDF vectorization** to convert text to vectors.
4. Computed **cosine similarity** between video entries.
5. Implemented a function to recommend top-5 most similar videos to a given title.

---

## 📊 Visualization

- **Top 15 Tags** in trending videos
- **Most Frequent Words** in video titles
- **WordCloud** from video titles

---

## 📌 How to Use

```bash
pip install -r requirements.txt
jupyter notebook youtube_recommender.ipynb


youtube-recommendation/
├── USvideos.csv
├── youtube_recommender.ipynb
├── requirements.txt
└── README.md


✍️ Author
Hande Çarkcı
📫 GitHub | 💡 Data Science & AI Learner



---

### 📦 Ekstra: `requirements.txt`

```txt
pandas
numpy
scikit-learn
matplotlib
wordcloud
