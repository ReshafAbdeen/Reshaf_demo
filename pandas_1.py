#PANDAS SERIES

import pandas as pd 
import numpy as np

class AdvancedNumpyDataFixer:
    def __init__(self, file_url):
        print("=====Data load ho rha hai=====")
        self.df = pd.read_csv(file_url)
        print("====Data ek num load hua hai====")
        self.bedrooms = self.df['total_bedrooms'].to_numpy().copy()
        print(f"\nTotal element in Array : {len(self.bedrooms)}")

    def fixing_missing_value(self):
        print("===Fixing values using Numpy===")
        fixing_eee = np.isnan(self.bedrooms)
        print(f"====Pehle gharo ki ginti : {np.sum(fixing_eee)}")

        fix_median = np.nanmedian(self.bedrooms)
        print(f"====Bache hue gharo ka Median : {fix_median}")

        self.bedrooms[fixing_eee] = fix_median

        new_fixing_df = np.isnan(self.bedrooms)
        print(f"\nBaad me khali wale Gharo ki Ginti : {np.sum(new_fixing_df)}")

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

    numpy_bot = AdvancedNumpyDataFixer(url)
    numpy_bot.fixing_missing_value()

import pandas as pd 
class PandasMasterClass:
    def __init__(self, file_url):
        print("===Pandas Group & Aggretion Bot===")
        self.df = pd.read_csv(file_url)
        print("==Data succesfully loaded==")

    def analyze_area_wise_price(self):
        print("===\nArea wise Avverage House===")
        area_group = self.df.groupby('ocean_proximity')['median_house_value'].mean()
        print("==Har ghar ki avg Value==")
        print(area_group.round(2))

    def advanced_multi_aggretion(self):
        print("\n==Advanced Multi stats (Mean , Count , Max)===")

        stats = self.df.groupby('ocean_proximity').agg({
            'median_house_value': 'mean',
            'ocean_proximity' : 'count',
            'housing_median_age' : 'max'
        })


        stats.columns = ['Max_price','Total_house','Avg_age']
        print(stats)

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

analyze_bot = PandasMasterClass(url)
analyze_bot.analyze_area_wise_price()
analyze_bot.advanced_multi_aggretion()