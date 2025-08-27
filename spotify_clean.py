# Connecting to MySql via Sql Alchemy and Importing Pandas
import pandas as pd
from sqlalchemy import create_engine
import pymysql

# Load Dataset
# Function -- Reads the CSV into a pandas Dataframe (df)
# Why: Need the dataset in memory to inspect and manipulate
# Make sure csv name matches what the file name is

file_path = "Most Streamed Spotify Songs 2024.csv"
df = pd.read_csv(file_path, encoding='latin1')

print("🔍 First 5 rows of data:")
print(df.head(), "\n")

# Inspection
# df.shape -- number of rows & columns
# df.info -- column data type (int, float, datetime)
# df.isnull().sum() -- counts null values in each column
# df.duplicated().sum() -- counts exact duplicate rows
# df.columns.duplicated() -- returns a boolean array marking repeated column names
# df.columns[df.columns.duplicated()].tolist() -- list all duplicates

print("Dataset shape:", df.shape)
print("\nColumn info:")
print(df.info(), "\n")

print("Null values per column:")
print(df.isnull().sum(), "\n")

print("Duplicate rows:", df.duplicated().sum(), "\n")

duplicates = df.columns[df.columns.duplicated()].tolist()
if duplicates:
    print("Duplicate columns found:", duplicates)
else:
    print("No duplicate columns found")

# Removes duplicates --- Cleaning step 
df.drop_duplicates(inplace=True)

# Standardize column names -- Cleaning step to format column names
# Removes leading/trailing spaces
# Converts to lowercase
# Replaces spaces with underscores (Spotify Streams to spotify_streams)

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Convert Release Date -- Cleaning for format consistency 
# Converts release dates into proper date time format
# If a value isn't a valid date, it becomes a null date time

if "release_date" in df.columns:
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")


# Clean Text Columns -- Cleaning to change string formatting
# Convert to string
# Removes leading/trailing spaces
# Converts text to title case (drake to Drake)

text_cols = ["track", "album_name", "artist", "isrc"]
for col in text_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.title()


# Clean Numeric Columns -- Cleaning for number consistency, missing values
# Handles numbers stored as text
# Replaces dashes with 0
# Converts to integers
# Fill nulls with 0

numeric_cols = [
    "all_time_rank", "track_score", "spotify_streams", "spotify_playlist_count",
    "spotify_playlist_reach", "spotify_popularity", "youtube_views", "youtube_likes",
    "tiktok_posts", "tiktok_likes", "tiktok_views", "youtube_playlist_reach",
    "apple_music_playlist_count", "airplay_spins", "siriusxm_spins",
    "deezer_playlist_count", "deezer_playlist_reach", "amazon_playlist_count",
    "pandora_streams", "pandora_track_stations", "soundcloud_streams",
    "shazam_counts", "tidal_popularity"
]

for col in numeric_cols:
    if col in df.columns:
        # Remove commas or replace "-" with 0
        df[col] = df[col].astype(str).str.replace(",", "").str.replace("-", "0")
        # Convert to numeric
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)


# Convert Explicit Track Column -- Cleaning for Categorical Standardization
# Converts values like Yes, Explicit, or True to 1, No False Clean to 0
# Fills nulls as 0

if "explicit_track" in df.columns:
    df["explicit_track"] = df["explicit_track"].astype(str).str.strip().str.lower()
    df["explicit_track"] = df["explicit_track"].map(
        {"yes": 1, "explicit": 1, "true": 1, "1": 1,
         "no": 0, "false": 0, "clean": 0, "0": 0}
    ).fillna(0).astype(int)


# Final Check -- Validation of Changes

# print("\nCleaned dataset info:")
# print(df.info())
# print("\nPreview of cleaned data:")
# print(df.head())

# Saved Cleaned Dataset -- Can comment back in (remove #)

# df.to_csv("spotify_cleaned.csv", index=False)
# print("\n Cleaned dataset saved as 'spotify_cleaned.csv'")

# Push to MySql
# username = "root"
# password = "BFree2013!"
# host = "127.0.0.1"
# database = "spotify_streams_2024"

# engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

# df.to_sql("spotify_songs", con=engine, if_exists="replace", index=False)

# print("Data cleaned and loaded into MySQL (table: spotify_songs)")