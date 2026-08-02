import pandas as pd
# load CSV file
url = 'https://raw.githubusercontent.com/keithgalli/pandas/master/pokemon_data.csv'
df = pd.read_csv(url)

print("\n===First 5 rows===")
print(df.head())

print('\n===Column Names===')
print(df.columns.tolist())

print("\n===Number of rows and column===")
print("Rows:",df.shape[0], "column:",df.shape[1])

print("\n===Summary Statistics===")
print(df.describe())
