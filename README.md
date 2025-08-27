# Spotify-dashboard
Interactive dashboard analyzing Spotify, Youtube, and Tiktok streaming data

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
