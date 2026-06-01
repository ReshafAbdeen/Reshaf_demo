import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


class NumPyDataCleaner:
    def __init__(self, file_url):
        print("Data load ho rha hia --")
        self.df = pd.read_csv(file_url)
        print("Data load ho gay hai")

    def clean_with_numpy(self):
        print(f"Total khali gahde : {self.df['total_bedrooms'].isnull().sum()}")
        bedroom_median = np.nanmedian(self.df['total_bedrooms'])
        print(f"Numpy se mila median : {bedroom_median}")

        self.df.loc[np.isnan(self.df['total_bedrooms']), 'total_bedrooms'] = bedroom_median
        print("---checking after numpy---")
        print(f"Total khali ghade bache :{self.df['total_bedrooms'].isnull().sum()}")

        
        print("\n--Generating bar Chart--")
        summary = self.df.groupby('ocean_proximity')['median_house_value'].mean().reset_index()

        plt.figure(figsize=(7, 6))
        plt.bar(summary['ocean_proximity'], summary['median_house_value'], color = 'skyblue', edgecolor = 'black')
        plt.title('Average House Value by Ocean Proximity', fontsize=14, fontweight='bold')
        plt.xlabel('Ocean Proximity (Area)', fontsize=12)
        plt.ylabel('Avg House Value ($)', fontsize=12)
        plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
        plt.show()
if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

np_bot = NumPyDataCleaner(url)
np_bot.clean_with_numpy()

