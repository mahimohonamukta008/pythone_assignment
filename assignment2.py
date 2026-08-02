import pandas as pd

url = "https://raw.githubusercontent.com/danielgrijalva/movie-stats/master/movies.csv"
df = pd.read_csv(url)

# Create a new column called 'Average_Score' using score and runtime
df['Average_Score'] = (df['score'] + df['runtime'] / 20) / 2

# Apply a condition: If the IMDB score is 7 or higher, mark as 'Hit'; otherwise, mark as 'Average'
df['Category'] = df['score'].apply(lambda x: 'Hit' if x >= 7 else 'Average')

# Display the first 5 rows with selected columns
print(df[['name', 'score', 'runtime', 'Category']].head())

print("\n=== Number of Hit and Average Movies ===")
print(df['Category'].value_counts())