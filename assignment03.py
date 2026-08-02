import pandas as pd

url = "https://raw.githubusercontent.com/danielgrijalva/movie-stats/master/movies.csv"
df = pd.read_csv(url)

# Sort the data in ascending order based on the 'score' column (lowest rating first)
sorted_df = df.sort_values(by='score', ascending=True)

print("=== Movies Sorted by IMDB Score (Ascending Order - Lowest 10 Ratings) ===")
print(sorted_df[['name', 'score']].head(10))