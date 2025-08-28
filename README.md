# Spotify-dashboard
Interactive dashboard analyzing Spotify, Youtube, and Tiktok streaming data

**Live Demo:** [Streamlit App](https://spotify-dashboard-yourname.streamlit.app)  

 **Source Code:** [GitHub Repo](https://github.com/yourusername/spotify-dashboard)  

Overview:

This project explores and analyzes the most streamed Spotify songs of 2024, providing insights on streaming trends, artist popularity, and playlist impact. Using Python for data cleaning and analysis, and Streamlit for an interactive dashboard, the project demonstrates the ability to turn raw data into actionable insights and visualizations.

Project Goals:

Data Cleaning & Exploration

 -  Inspect and clean the raw Spotify dataset for analysis.
  
  - Standardize columns, handle missing values, and format dates and numeric fields.
  
Exploratory Data Analysis (EDA)

  - Identify top songs and top artists on Spotify.
  
  - Explore trends over time, including streams by release year.
  
  - Analyze the relationship between playlist count and popularity.
  
  - Compare Spotify streams with YouTube views.
  
Advanced Insights

  - Determine which artists dominate across Spotify, YouTube, and TikTok.
  
  - Examine the impact of playlists on stream counts.
  
  - Identify eras/years producing the most long-term hits.
  
Interactive Dashboard

  - Built with Streamlit to visualize trends and insights.
  
  - Includes bar charts, scatter plots, and summary metrics for quick insights.
  
Dataset:

  - Source: Spotify Most Streamed Songs 2024 (CSV)
  
  - Rows: 4,598 songs
  
  - Columns: 29 (including track, album, artist, release date, streams, playlist info, and social metrics)
  
Key CSV Files included in this repo:

  - spotify_cleaned.csv --> cleaned and processed dataset for analysis
  
  - top_songs.csv --> Top 10 most streamed songs

  - top_artists.csv --> Top 10 most streamed artists  
  
  - streams_by_year.csv --> Spotify streams aggregated by release year
  
  - playlist_popularity_corr.csv --> Data for analyzing plalist count vs. popularity
  
  - top_artist_all_platforms.csv --> Top artists across Spotify, Youtube, and Tiktok
  
  - spotify_youtube_correlation.csv --> Correlation between Spotify popularity and Youtube views

Technologies Used:

  - Python --> Pandas, NumPy for data analysis
  
  - Plotly --> Visualizations (bar charts, scatter plots)
  
  - Streamlit --> Interactive dashboard
  
  - MySql --> Optional storage for cleaned dataset

Usage:

Clone the repository:

    git clone https://github.com/YOUR-USERNAME/spotify-dashboard.git

Navigate to the project folder:

    cd spotify-dashboard

Install required packages:

    pip install -r requirements.txt

Run the Streamlit dashboard:

    streamlit run spotify_dashboard.py

Dashboard Features:

- Dataset Overview --> First 5 rows, total songs, total streams, and average popularity.

- Top 10 Songs & Artists --> Horizontal bar charts for quick insight.

- Spotify vs Youtube --> Correlation visualization between streams and Youtube views.

- Streams by Year --> Trend analysis of streams over time.

- Playlist Impact --> Scatter plot to explore the relationship between playlist count and popularity

- Top Artists Across All Platforms --> Horizontal bar chart showing total streams across Spotify, Youtube, and Tiktok

Insights:

 - Lower overall ranks indicate artist with higher dominance across platforms.

 - Spotify streams generally correlate with Youtube views, indicating cross-platform popularity.

 - Songs added to more playlists tend to receiver higher streams, showing playlist impact.

 - Certain years/eras produce more long-term hits, helping identify trends over time.

Recommendations:

Top Songs & Artists

 - Spotify could feature playlists or promotions around these high-performing artists to increasse engagement further.

Platform Correlation
 - Cross-platform promotions can help artists reach audiences on multiple platforms simutaneously.

Trends Over Time

 - Spotify can highlight "classic hits" alongside trending tracks to engage users with both nostalgia and current hits.

Playlist Impact

 - Curating playlists that highlight emerging artists or underrepresented tracks can boost engagement and discoverability.

Top Artists Across All Platforms

 - Identify these multi-platform stars for partnerships, exclusive content, or marketing campaigns.


License:

This project is for personal and educational purposes.
