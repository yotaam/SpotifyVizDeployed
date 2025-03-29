# 🌍 Spotify Global Music Trends Visualization

Explore how popular music differs across countries and over time with our interactive 3D globe. This project combines audio features, lyrical sentiment analysis, and dynamic visualizations to help users uncover patterns in global song trends.

---

## 📅 Overview

This app visualizes a year's worth of Spotify Top 50 data across 73 countries. Users can:

- Select audio features (energy, danceability, valence) or lyrical moods (joy, sadness, anger, etc.)
- View RGB audio composites
- Use a time slider to observe changes over time
- Click on countries for song details and word clouds
- View historical trends via line charts

### ✨ Live Demo (deprecated, no longer paying for it)

https://spotifyvizdeployed.onrender.com/

Demo video: https://drive.google.com/file/d/19A90NTm3j6pwN5l9hW6MwFD7uLonLdmZ/view?usp=sharing&usp=embed_facebook

---

## 📂 Project Structure

```
SpotifyVizDeployed/
├── songmap/
│   ├── templates/
│   ├── static/
│   │   ├── universal_top_spotify_songs.csv
│   │   ├── lyrics_data.csv
│   │   ├── song_lyric_word_dict.csv
│   │   └── song_data_with_mood_scores.csv
│   ├── songmap.py
│   └── requirements.txt
```

---

## 🛠️ Installation & Running Locally

Follow these steps to run the app on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/ytaa2021/SpotifyVizDeployed.git
cd SpotifyVizDeployed/songmap
```

### 2. Install dependencies

Make sure you have Python 3.11+ installed, then create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Add the datasets

Place the following CSV files into the `songmap/static/` directory:

- `universal_top_spotify_songs.csv`
- `lyrics_data.csv`
- `song_lyric_word_dict.csv`
- `song_data_with_mood_scores.csv`

> These files are large and were excluded from GitHub. You can locate them [here](https://drive.google.com/drive/folders/1k8Bg9z87bUgniSat5IC0hNW40Ab3m-yg?usp=sharing)

### 4. Run the Flask app

From within the `songmap` directory:

```bash
python songmap.py
```

You should see output like:

```
 * Running on http://127.0.0.1:5000/
```

### 5. Open in browser

Visit [http://localhost:5000](http://localhost:5000) to explore the interactive globe!

---

## 🚀 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
  - Three.js + Three-Globe
  - D3.js (for data wrangling)
  - Chart.js (for country feature timelines)
  - D3-cloud (for word clouds)

- **Backend:** Python Flask
  - Loads and serves CSV data for frontend use

- **Data Sources:**
  - [Top Spotify Songs in 73 Countries](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated)
  - Spotify API (audio features)
  - Genius API + web scraping (lyrics)
  - NRC Word-Emotion Lexicon (mood analysis)

---

## 📖 Citation

If you use this project for academic purposes, please cite the authors and original data sources appropriately.

---

## ❤️ Authors

- [Yotam Twersky](https://github.com/ytaa2021)
- [Priya Julian](https://github.com/) *(placeholder)*

---

## 🙌 Acknowledgments

- Thanks to the creators of Three-Globe, Chart.js, and the open-source contributors who made this project possible.
- Special appreciation to Spotify and Genius for their APIs and open access to musical data.

---

## 🔧 License

MIT License
