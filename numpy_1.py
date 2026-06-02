import numpy as np
import pandas as pd 
class NumpyFilter:
    def __init__(self, file_url):
        print("---Data load ho  rah hai ---")
        df = pd.read_csv(file_url)
        
        self.price = df['median_house_value'].to_numpy()
        self.age = df['housing_median_age'].to_numpy()
        self.area = df['ocean_proximity'].to_numpy()

    def filter_with_numpy(self):
        print("\n---Filtering using Numpy---")
        print("\n---Condition : Age > 50 & price < 150000")
        mask = np.logical_and(self.age > 50, self.price < 150000)
        filetr_price = self.price[mask]
        filter_age = self.age[mask]
        filter_area = self.area[mask]


        print(f"Numpy se mile saste or purane gharo ki ginti: {len(filetr_price)} " )
        print("\n---pehle 3 gharo ki ginti---")
        for i in range(3):
          print(f"Ghar {i+1} Age = {filter_age[i]} , Price = {filetr_price[i]}, Area = {filter_area[i]}")

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

numpy_bot = NumpyFilter(url)
numpy_bot.filter_with_numpy()




