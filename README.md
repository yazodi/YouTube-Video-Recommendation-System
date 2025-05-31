# 🎬 YouTube Video Recommendation System (Content-Based Filtering)

Bu proje, YouTube'daki videolara benzer içerikleri öneren bir **content-based filtering** sistemidir.  
Kullanıcı bir video başlığı girer ve sistem, **başlık**, **açıklama** ve **etiketleri** temel alarak benzer 5 videoyu önerir.

---

## 📦 Dataset

- Kaynak: [YouTube Trending Videos - Kaggle](https://www.kaggle.com/datasets/datasnaek/youtube-new)
- Kullanılan dosya: `USvideos.csv` (küçültülmüş örneği: `USvideos_sample.csv`)

---

## 🧠 Kullanılan Teknolojiler

- Python, pandas, numpy
- scikit-learn → **TF-IDF Vectorizer**, **cosine similarity**
- joblib (model kaydetme)
- matplotlib, wordcloud (görselleştirme)
- Streamlit (web uygulaması)

---

## 🔍 Proje Adımları

1. `title`, `description`, `tags` sütunları seçildi ve temizlendi.
2. Bu sütunlar birleştirilerek tek bir `text` kolonu oluşturuldu.
3. **TF-IDF** ile metin vektörleştirildi.
4. **Cosine similarity** ile videolar arası benzerlik hesaplandı.
5. Kullanıcı başlığına en çok benzeyen ilk 5 video önerildi.

---

## 💻 Web Uygulaması (Streamlit)

Projeye bir Streamlit arayüzü entegre edildi.

### 🚀 Uygulamayı Başlatmak:

```bash
pip install -r requirements.txt
streamlit run app.py




Kullanıcı arayüzü üzerinden bir video başlığı girerek önerileri alabilirsiniz.(verisetindene varsa)

📊 Görselleştirme
En sık kullanılan 15 YouTube etiketi

Başlıklarda en sık geçen 15 kelime

Kelime bulutu (word cloud) gösterimi

📁 Dosya Yapısı
youtube-recommendation/
├── USvideos_sample.csv
├── app.py
├── youtube_recommender.ipynb
├── tfidf_vectorizer.pkl
├── cosine_similarity.pkl
├── youtube_df.pkl
├── title_indices.pkl
├── requirements.txt
└── README.md


🌐 Model Paylaşımı (Opsiyonel)
Eğitilen modeller Hugging Face üzerine yüklenebilir:
https://huggingface.co/yazodi/youtube-video-recommender

✍️ Yazar
Hande Çarkcı
📫 GitHub | 💡 Data Science & AI Öğrencisi

📦 Requirements

streamlit
pandas
numpy
scikit-learn
joblib
matplotlib
wordcloud


---