import pandas as pd

# Load cleaned dataset
df = pd.read_csv("spotify_cleaned.csv")

# Ensure release_date is datetime
df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")

"""
# Exploratory Data Analysis
# Top streamed songs and artist
# Distribution of release years
# Average popularity, streams, playlist reach, etc.

# Top 10 streamed songs
top_songs = df.sort_values("spotify_streams", ascending=False).head(10)[["track", "artist", "spotify_streams"]]
print(top_songs)

# Save top songs
top_songs.to_csv("top_songs.csv", index=False)


# Top 10 artists by total streams (.reset_index() makes it a proper column and not an index)
top_artists = (
   df.groupby("artist")["spotify_streams"]
   .sum()
   .reset_index()
   .sort_values("spotify_streams", ascending=False)
   .head(10)
  )
print(top_artists)

# Save top artists
top_artists.to_csv("top_artists.csv", index=False)

# Average Spotify popularity
print("Average popularity:", df["spotify_popularity"].mean())

# Extract year from release_date
df["release_year"] = df["release_date"].dt.year

# Streams by year
streams_by_year = df.groupby("release_year")["spotify_streams"].sum().reset_index()
print(streams_by_year)

# Save streams by year
streams_by_year.to_csv("streams_by_year.csv", index=False)

"""

"""
# Correlation between Spotify and YouTube
spotify_youtube_correlation = df[["spotify_streams", "youtube_views", "spotify_popularity"]].corr()
print(spotify_youtube_correlation)

# Save Spotify vs YouTube correlation
spotify_youtube_correlation.reset_index().to_csv("spotify_youtube_correlation.csv", index=False)

"""
"""
# Sum total engagement by artist across platforms
artist_platform_totals = df.groupby("artist")[
    ["spotify_streams", "youtube_views", "tiktok_posts", "tiktok_likes", "tiktok_views"]
].sum().reset_index()

# Optional: normalize or rank by each platform
artist_platform_totals["spotify_rank"] = artist_platform_totals["spotify_streams"].rank(ascending=False)
artist_platform_totals["youtube_rank"] = artist_platform_totals["youtube_views"].rank(ascending=False)
artist_platform_totals["tiktok_rank"] = artist_platform_totals["tiktok_views"].rank(ascending=False)

# Calculate overall rank (sum of ranks)
artist_platform_totals["overall_rank"] = artist_platform_totals[["spotify_rank", "youtube_rank", "tiktok_rank"]].sum(axis=1)

# Top artists across all platforms
top_artists_all_platforms = artist_platform_totals.sort_values("overall_rank").head(10)
print(top_artists_all_platforms)

# Save top artist on across platforms
top_artists_all_platforms.to_csv("top_artists_all_platforms.csv", index=False)

"""
""" 
# Correlation between playlist count and Spotify popularity
playlist_popularity_corr = df[["spotify_playlist_count", "spotify_popularity"]].corr()
print(playlist_popularity_corr)

# Optional: visualize with a scatter plot
import matplotlib.pyplot as plt

plt.scatter(df["spotify_playlist_count"], df["spotify_popularity"], alpha=0.5)
plt.xlabel("Spotify Playlist Count")
plt.ylabel("Spotify Popularity")
plt.title("Playlist Count vs Spotify Popularity")

# Save plot as an image file (png, jpg, etc.)
plt.savefig("playlist_vs_popularity.png")
plt.show()

# Save spotify vs playlist
playlist_popularity_corr.reset_index().to_csv("playlist_popularity_corr.csv", index=False)

"""

# Make sure release_year exists
df["release_year"] = pd.to_datetime(df["release_date"], errors="coerce").dt.year

# Total Spotify streams by release year
streams_by_year = df.groupby("release_year")["spotify_streams"].sum().reset_index()
streams_by_year = streams_by_year.sort_values("spotify_streams", ascending=False)
print(streams_by_year.head(10))  # Top 10 years with most streams

# Optional: visualize
plt.bar(streams_by_year["release_year"], streams_by_year["spotify_streams"])
plt.xlabel("Release Year")
plt.ylabel("Total Spotify Streams")
plt.title("Total Spotify Streams by Release Year")
plt.show()
