#Day 1 of pandas

import pandas as  pd 
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv'

print("\nInternet se data magay hai....")
df = pd.read_csv(url)


df.to_csv('california_housing', index=False)
print("File save as 'calipornia_housing.csv'!\n")

print("\ndata load ho gya hai..")

print("Total ghar faeture(Row, Columns):")
print(df.shape)

print("\n--Top 3 House--")
print(df.head(3))

print("Gharo ka data....")
df['total_bedrooms'] = df["total_bedrooms"].fillna(0)
print(df.isnull().sum())
print(df.info())


plt.figure(figsize = (9, 7))
sns.barplot(x = 'ocean_proximity', y = 'median_house_value', data = df, palette = 'viridis')

plt.title("California House Prices vs Ocean Proximity", fontsize=16, fontweight='bold')
plt.xlabel("Samandar Se Doori (Ocean Proximity)", fontsize=12)
plt.ylabel("Ghar Ki Keemat (Median House Value in USD)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.1)

plt.show()




#Day 2 of pandas

import pandas as pd 

class DataArregator:
    def __init__(self, file_url):
        print("\nData load ho rha hai....")
        self.df = pd.read_csv(file_url)

    def area_wise_avg(self):
        print("\n--Average House Value by Ocean Proximity--")
        summary = self.df.groupby('ocean_proximity')['median_house_value'].mean().reset_index()
        print(summary)

    def grt_area_wise_stats(self):
        print("\n--Population (Total) & House Value (Max) by Area--")
        advaced_summary = self.df.groupby('ocean_proximity').agg({
            'median_house_value' : 'max',
            'population' : 'sum'
              })
        print(advaced_summary)

if __name__ == "__main__":
         url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

agg_bot = DataArregator(url)
agg_bot.area_wise_avg()
agg_bot.grt_area_wise_stats()



#Sorted Aggregation Class

import pandas as pd 

class SortedDataAnalyzer:
    def __init__(self, file_url):
        print("\n--Data load ho rha hai--")
        self.df = pd.read_csv(file_url)
        print("\n--Data ;oad ho gya hai--")

    def get_top_expensive_areas(self):
        print("\n--Area Ranked by Average House Value (Highest to Lowest)--")
        summary = self.df.groupby('ocean_proximity')['median_house_value'].mean().reset_index()
        summary = summary.rename(columns = {'median_house_value' : 'Avg_value'})
        sorted_summary = summary.sort_values(by = 'Avg_value', ascending=False)
        print(sorted_summary)
if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
rank_bot = SortedDataAnalyzer(url)
rank_bot.get_top_expensive_areas()



import pandas as pd

class DataCleaner:
    def __init__(self, file_url):
        print("--Data load ho rha hai--")
        self.df = pd.read_csv(file_url)
        print("--Data load ho gya hai--")
    
    def check_missing_data(self):
        print("\n--Missing value in each column--")
        missing_val_count = self.df.isnull().sum()
        print(missing_val_count)

    def fill_missing_val(self):
        print("\n--Fixing Missing Values--")
        bedrooms_median = self.df['total_bedrooms'].median()
        print(f"Total bedroom ka median : {bedrooms_median}")
        self.df['total_bedrooms'] = self.df['total_bedrooms'].fillna(bedrooms_median)

        print("\n--Missing value ko succesfully fill kar diya gya hai--")
        print("\n--Re-checking Missing values to confirm--")
        print(self.df.isnull().sum())

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

clear_bot = DataCleaner(url)
clear_bot.check_missing_data()
clear_bot.fill_missing_val()