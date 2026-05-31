# # #AI Data Slicer Class
import pandas as pd 
class DataSlicer:
    def __init__(self, file_url):
        print("Data load ho rha hai....")
        self.df = pd.read_csv(file_url)
        print("Data succesfully load ho gya hai.")


    def show_head(self, row=5):
        print("\n---Print first row---")    
        print(self.df.head(row))


    def slice_with_iloc(self):
        print("\n---slicing using .iloc (pehle 5 rwo or pehle 3 column)---")
        sliced_data = self.df.iloc[0:5, 0:3]
        print(sliced_data)
        print("\n")

    def filter_with_loc(self):
        print("\n---Filtering with .loc (island wale ghar unki kiimat)---")
        condition = self.df['ocean_proximity'] == 'ISLAND'
        filtered_data = self.df.loc[condition, ['median_house_value', 'ocean_proximity']]
        print(filtered_data)


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
     

    bot = DataSlicer(url)
    bot.show_head(3)
    bot.slice_with_iloc()
    bot.filter_with_loc() 






# #Advanced Data Filtering Class
import pandas as pd 

class AdvancedDataFilter:
    def __init__(self, file_url):
        print("\n--Advanced Data filter--")
        self.df = pd.read_csv(file_url)
        print("\nData load ho gya hai....")

    def filter_luxury_and_old_house(self):
        print("---Luxury & old house---")
        cod1 = self.df['ocean_proximity'] == 'NEAR BAY'
        cod2 = self.df['housing_median_age'] > 50

        result = self.df.loc[cod1 & cod2, ['housing_median_age', 'median_house_value', 'ocean_proximity']]
        print(result.head(5))
        print(f"Total aise ghar mile : {len(result)}\n")

    def filter_budget_or_island(self):
        print("--Filter : Ghar jo usland oer hai yaa to $50,000 se saste hai..")
        
        cond_island = self.df['ocean_proximity'] == 'ISLAND'
        cond_budget = self.df['median_house_value'] < 50000

        final = self.df.loc[cond_island | cond_budget, ['housing_median_age', 'median_house_value', 'ocean_proximity' ]]
        print(final)
        print("\n")


if __name__ == "__main__":

    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

    filter_bot = AdvancedDataFilter(url)
    filter_bot.filter_budget_or_island()
    filter_bot.filter_luxury_and_old_house()




#Advanced Class with NumPy
import pandas as pd
import numpy as np

class NumpyDataTransfer:
    def __init__(self, file_url):
        print("--Data load hao rha hai--")
        self.df = pd.read_csv(file_url)


    def category(self):
        print("\n--Numpy + Pandas bot started--")
        condition1 = self.df['median_house_value'] > 200000
        self.df['house_category'] = np.where(condition1, 'Luxury', 'Budget')
        print(self.df[['median_house_value', 'house_category']].head(10))


    def apply_log_transform(self):
        print("Applying log Transfering using np.log")

        self.df['log_house_value'] = np.log(self.df['median_house_value'])
        print(self.df[['median_house_value', 'log_house_value']].head(5))

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
    
    numpy_bot = NumpyDataTransfer(url)
    
    numpy_bot.category()
    
    numpy_bot.apply_log_transform()        