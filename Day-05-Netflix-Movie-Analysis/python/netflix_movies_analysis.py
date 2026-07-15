import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
print("Loading Netflix dataset...")
df = pd.read_csv('../dataset/netflix_titles.csv')
print("Dataset loaded successfully")

# Basic dataset overview
print("\nDataset shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# Check duplicates
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("Shape after removing duplicates:", df.shape)

# Missing values overview
print("\nMissing values per column:")
print(df.isnull().sum())

# Create cleaned copy for analysis
print("\nCreating cleaned dataset...")
df_clean = df.copy()

# Fill missing values in important columns
df_clean['director'] = df_clean['director'].fillna('Unknown')
df_clean['cast'] = df_clean['cast'].fillna('Unknown')
df_clean['country'] = df_clean['country'].fillna('Unknown')
df_clean['date_added'] = df_clean['date_added'].fillna('Unknown')
df_clean['duration'] = df_clean['duration'].fillna('Unknown')

# Drop rows where cast is still missing
# (This keeps the dataset consistent for later analysis)
df_clean = df_clean.dropna(subset=['cast'])
print("Cleaned dataset shape:", df_clean.shape)

# Basic analysis summary
print("\nBasic analysis summary:")
print("Total Titles:", len(df_clean))
print("Movies:", (df_clean['type'] == 'Movie').sum())
print("TV Shows:", (df_clean['type'] == 'TV Show').sum())
print("Top Country:", df_clean['country'].value_counts().idxmax())
print("Top Rating:", df_clean['rating'].value_counts().idxmax())

# Top 10 genres
genres = df_clean['listed_in'].dropna().str.split(',').explode().str.strip()
genres_top = genres.value_counts().head(10)
print("\nTop 10 genres:")
print(genres_top)

# Top 10 directors
# Split director field and count values

directors = df_clean['director'].dropna().str.split(',').explode().str.strip()
directors_top = directors.value_counts().head(10)
print("\nTop 10 directors:")
print(directors_top)

# Top 10 actors
actors = df_clean['cast'].dropna().str.split(',').explode().str.strip()
actors_top = actors.value_counts().head(10)
print("\nTop 10 actors:")
print(actors_top)

# Month-wise and year-wise additions
# Convert date_added to datetime for trend analysis
print("\nAnalyzing content additions over time...")
df_month = df_clean[df_clean['date_added'] != 'Unknown'].copy()
df_month['date_added'] = pd.to_datetime(df_month['date_added'], format='mixed', errors='coerce')
df_month = df_month.dropna(subset=['date_added'])

monthly_trend = df_month['date_added'].dt.to_period('M').value_counts().sort_index()
year_trend = df_month['date_added'].dt.to_period('Y').value_counts().sort_index()

print("\nMonth-wise addition trend:")
print(monthly_trend.head(12))
print("\nYear-wise addition trend:")
print(year_trend.head(10))

# Ratings analysis
print("\nMost common rating:", df_clean['rating'].value_counts().idxmax())
print("Kids content count:", df_clean[df_clean['rating'].isin(['TV-Y', 'TV-Y7', 'G', 'PG', 'PG-13'])].shape[0])
print("Adult content count:", df_clean[df_clean['rating'].isin(['TV-MA', 'R', 'NC-17'])].shape[0])

# Duration analysis for movies
print("\nMovie duration analysis:")
movie_duration = df_clean[df_clean['type'] == 'Movie'].copy()
movie_duration['duration_min'] = movie_duration['duration'].str.extract(r'(\d+)').astype(float)
print(movie_duration[['title', 'duration_min']].head())

# TV seasons analysis
print("\nTV show season analysis:")
tv_seasons = df_clean[df_clean['type'] == 'TV Show'].copy()
tv_seasons['season_count'] = tv_seasons['duration'].str.extract(r'(\d+)').astype(float)
print(tv_seasons[['title', 'season_count']].head())

# Oldest and latest release
print("\nOldest release year:", df_clean['release_year'].min())
print("Latest release year:", df_clean['release_year'].max())

# Longest movie
longest_movie = movie_duration.sort_values('duration_min', ascending=False).head(1)
print("\nLongest movie:")
print(longest_movie[['title', 'duration_min']])

# Insights
print("\nInsights:")
print("- Movies significantly outnumber TV shows in the dataset.")
print("- The United States contributes the highest number of titles.")
print("- TV-MA is the most common rating among titles.")
print("- Drama and International Movies dominate the catalog.")
print("- Netflix content expanded rapidly after 2015.")

# Conclusion
print("\nConclusion:")
print(f"Dataset contains {len(df_clean)} titles.")
print("Movies dominate the Netflix catalog.")
print("United States contributes the maximum number of titles.")
print("TV-MA is the most frequent rating.")
print("Drama is one of the most popular genres.")
print("Netflix content expanded rapidly after 2015.")

# Business recommendations
print("\nBusiness Recommendations:")
print("- Increase kids-oriented content in underrepresented regions.")
print("- Invest more in high-performing genres such as dramas and international content.")
print("- Focus on countries showing growing demand for local-language productions.")
print("- Continue producing TV-MA content because it dominates the catalog.")
