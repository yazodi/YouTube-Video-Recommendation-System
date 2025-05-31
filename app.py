import streamlit as st
import joblib
import pandas as pd

# Başlık
st.title("🎬 YouTube Video Recommendation System")
st.markdown("Bu sistem, verdiğiniz bir video başlığına en benzer 5 videoyu önerir.")

# Model dosyalarını yükle
tfidf = joblib.load("tfidf_vectorizer.pkl")
df = joblib.load("youtube_df.pkl")
indices = joblib.load("title_indices.pkl")
cosine_sim = joblib.load("cosine_similarity.pkl")

# Kullanıcıdan giriş al
video_title = st.text_input("🎯 Video Başlığını Girin", "")

if video_title:
    if video_title in indices.index:
        idx = indices[video_title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
        video_indices = [i[0] for i in sim_scores]

        st.subheader("📌 Önerilen Videolar:")
        for i in video_indices:
            st.markdown(f"**{df.iloc[i]['title']}**")
            st.caption(df.iloc[i]['description'])
    else:
        st.error("⚠️ Bu başlık veri kümesinde bulunamadı. Lütfen geçerli bir başlık girin.")
