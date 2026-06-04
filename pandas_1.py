#Pandas Series

import pandas as pd 
url ="https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
print("==URL se data load ho rha hai===")
try:        
    row_df = pd.read_csv(url)
    print("===Data load ho gya hai===")
    print(f"\nTotal Row loaded : {len(row_df)}")
    print("\n===Suruati 5 line print hogi===")
    print(row_df.head())
    print("-"*50)

    cleaned_df = row_df.dropna(subset=['Year', 'Value'])
    cleaned_df = cleaned_df.drop_duplicates()

    filtered_df = cleaned_df[(cleaned_df['Country Name'] == 'India') & (cleaned_df['Year'] > 2010)]
    print(filtered_df)
    print('-'*50)

except:
    print("URl se gaandu data nhi load hua saaalala")
    
pop_2011 = filtered_df['Value'].iloc[0] 
pop_2024 = filtered_df['Value'].iloc[-1] 

growth_avg = ((pop_2024 - pop_2011) /pop_2011) * 100
print(f"India ki badti abaadi ki Percentage Growth : {growth_avg:.2f}%")




#Movies Rating Analyzer
import pandas as pd 
url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/bechdel/movies.csv"
print("==Data load ho rha hai URl se==")

try:
    movies_df = pd.read_csv(url) 
    cleaned_df = movies_df[['binary', 'budget', 'year']].copy()
    print("===Data load ho gya hai===")
    rating_avg = cleaned_df.groupby('binary')['budget'].mean()
    print(rating_avg)

except Exception as e:
    print(f"Kuch Gadbad hui hai : {e}")