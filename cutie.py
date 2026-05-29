import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/wtitze/3E4A28/master/IMDb-movies.csv'

print("\nMovie Dataset load ho raha hai, thoda sa intezar karein...")
columns_needed = ['title', 'year', 'genre', 'duration', 'votes', 'budget', 'usa_gross_income']
df = pd.read_csv(url, usecols=columns_needed)

print("Data successfully load ho gaya!")
print(f"Total Movies ka Data: {df.shape[0]} Rows, {df.shape[1]} Columns\n")

print("--- Cleaning Missing Data ---")
df['budget'] = df['budget'].fillna(0)
df['usa_gross_income'] = df['usa_gross_income'].fillna(0)
print("✔ Missing values ko clean kar diya gaya hai.\n")

top_movies = df.nlargest(5, 'votes')

print("--- Top 5 Most Popular Movies ---")
print(top_movies[['title', 'year', 'genre', 'votes']])

print("\nGraph taiyar ho raha hai...")
plt.figure(figsize=(10, 6))

sns.barplot(x='votes', y='title', data=top_movies, palette='coolwarm')

plt.title("IMDB Top 5 Most Voted Movies", fontsize=16, fontweight='bold')
plt.xlabel("Total Votes (Popularity)", fontsize=12)
plt.ylabel("Movie Name", fontsize=12)

print(" Graph khulne wala hai...")
plt.show()