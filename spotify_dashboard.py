import streamlit as st
import pandas as pd
import plotly.express as px

# Load your cleaned Spotify dataset
df = pd.read_csv("spotify_cleaned.csv")

# Add a dashboard title
st.title("Spotify Data Dashboard")

# Preview dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Show basic metrics
st.subheader("Quick Stats")
st.metric("Total Songs", len(df))
st.metric("Total Streams", f"{df['spotify_streams'].sum():,}")
st.metric("Average Popularity", round(df["spotify_popularity"].mean(), 2))

# Top 10 songs Title
st.header("Top Songs by Spotify Streams")

# Top 10 songs
top_songs = df.sort_values("spotify_streams", ascending=False).head(10)

fig_songs = px.bar(
    top_songs,
    x="spotify_streams",
    y="track",  # put song titles on y-axis
    orientation="h",  # makes it horizontal
    title="Top 10 Most Streamed Songs on Spotify",
    labels={"spotify_streams": "Streams", "track": "Song"}
)

fig_songs.update_layout(yaxis=dict(autorange="reversed"))  # keeps highest at the top
st.plotly_chart(fig_songs, use_container_width=True)


# Aggregate streams by artist
artist_streams = df.groupby("artist", as_index=False)["spotify_streams"].sum()

# Adding Title
st.header("Top Artists by Spotify Streams")

# Top 10 artists
top_artists = (
    df.groupby("artist")["spotify_streams"]
    .sum()
    .reset_index()
    .sort_values("spotify_streams", ascending=False)
    .head(10)
)

fig_artists = px.bar(
    top_artists,
    x="spotify_streams",
    y="artist",  # put artists on y-axis
    orientation="h",
    title="Top 10 Most Streamed Artists on Spotify",
    labels={"spotify_streams": "Streams", "artist": "Artist"}
)

fig_artists.update_layout(yaxis=dict(autorange="reversed"))
st.plotly_chart(fig_artists, use_container_width=True)

# Load cleaned dataset (if not already loaded)
df = pd.read_csv("spotify_cleaned.csv")

# Ensure release_date is datetime (if needed)
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

# --- Platform Correlation Analysis ---
st.header("Spotify vs YouTube Popularity")

# Calculate correlation between Spotify popularity and YouTube views
correlation_df = df[["spotify_popularity", "youtube_views", "spotify_streams"]].corr()
st.write("Correlation Table:")
st.dataframe(correlation_df)

# Scatter plot: Spotify streams vs YouTube views
fig_regression = px.scatter(
    df,
    x="spotify_popularity",
    y="youtube_views",
    trendline="ols",  # adds regression line
    hover_data=["track", "artist"],
    title="Spotify Popularity vs YouTube Views"
)

st.plotly_chart(fig_regression, use_container_width=True)

# Load streams by year data
streams_by_year = pd.read_csv("streams_by_year.csv")

# Header
st.header("Spotify Streams by Release Year")

# Identify top 3 years
top_years = streams_by_year.nlargest(3, "spotify_streams")["release_year"].tolist()

# Add a new column for coloring
streams_by_year["highlight"] = streams_by_year["release_year"].apply(
    lambda x: "Top 3" if x in top_years else "Other"
)

# Bar chart with highlighted top years
fig_year = px.bar(
    streams_by_year,
    x="release_year",
    y="spotify_streams",
    color="highlight",
    title="Total Spotify Streams by Release Year",
    labels={"release_year": "Release Year", "spotify_streams": "Total Streams"},
    text="spotify_streams",
    color_discrete_map={"Top 3": "crimson", "Other": "lightblue"}
)

fig_year.update_traces(texttemplate='%{text:,}', textposition='outside')  # formatted numbers above bars
fig_year.update_layout(xaxis=dict(tickmode='linear'), showlegend=True)

# Display chart in Streamlit
st.plotly_chart(fig_year, use_container_width=True)

# --- Load your datasets ---
df = pd.read_csv("spotify_cleaned.csv")  # main cleaned dataset
playlist_corr = pd.read_csv("playlist_popularity_corr.csv")  # playlist vs popularity

# Compute total streams across all platforms for top artists
top_artists_all = pd.read_csv("top_artist_all_platforms.csv")
top_artists_all["total_streams_all_platforms"] = (
    top_artists_all["spotify_streams"] +
    top_artists_all["youtube_views"] +
    top_artists_all["tiktok_views"]
)

# -------------------------------
# 1️⃣ Playlist Count vs Popularity
# -------------------------------
st.header("Playlist Count Impact on Spotify Popularity")

# Load the playlist-popularity correlation dataset
playlist_corr = pd.read_csv("playlist_popularity_corr.csv")

# Scatter plot
fig_playlist = px.scatter(
    playlist_corr,
    x="spotify_playlist_count",
    y="spotify_popularity",
    title="Spotify Popularity vs Playlist Count",
    hover_data=["spotify_playlist_count", "spotify_popularity"]
)

# Show in Streamlit
st.plotly_chart(fig_playlist, use_container_width=True)

# -------------------------------
# 2️⃣ Top Artists Across All Platforms
# -------------------------------
st.header("Top Artists Across Spotify, YouTube, and TikTok")

# Sum streams across platforms
top_artists_all["total_streams_all_platforms"] = (
    top_artists_all["spotify_streams"] +
    top_artists_all["youtube_views"] +
    top_artists_all["tiktok_views"]
)

# Sort top artists by total streams
top_artists_all_sorted = top_artists_all.sort_values(
    "total_streams_all_platforms", ascending=False
).head(10)

# Plot horizontal bar chart
fig_top_artists_all = px.bar(
    top_artists_all_sorted,
    x="total_streams_all_platforms",
    y="artist",
    orientation="h",
    title="Top 10 Artists Across All Platforms",
    labels={"total_streams_all_platforms": "Total Streams (All Platforms)", "artist": "Artist"}
)

fig_top_artists_all.update_layout(yaxis=dict(autorange="reversed"))  # highest at top
st.plotly_chart(fig_top_artists_all, use_container_width=True)

page_bg_pattern = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f4f4f9;
    background-image: radial-gradient(#e5e5e5 1px, transparent 1px);
    background-size: 20px 20px;
}
</style>
"""
st.markdown(page_bg_pattern, unsafe_allow_html=True)
