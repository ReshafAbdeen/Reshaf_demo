#Pandas series
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

class SeriesMaster:
    def __init__(self, file_url):
        print("--Data load ho rha hai--")
        self.df = pd.read_csv(file_url)
        print ("--Data loa ho gya hai--")

    def find_ocean_trend(self):
        print("Counting House eanch areas (Trend)")
        area_count = self.df['ocean_proximity'].value_counts()
        print(area_count)


    def lowercase_ocean_text(self):
        print("Converting Ocean proximity to lowercase using apply method...")
        def make_lowercase(text):
            return text.lower()
        
        self.df['ocean_proximity_clean'] = self.df['ocean_proximity'].apply(make_lowercase)
    
    def plot_ocean_data(self):
        print("Bar plot chart ban ke ready ho rha hia ...")
        area_count = self.df['ocean_proximity_clean'].value_counts().reset_index()

        plt.figure(figsize = (7,8))
        sns.barplot(x ='ocean_proximity_clean', y = 'count', palette = 'viridis', data = area_count )
        plt.title('Ocean ke  kinare ke ghar', fontsize = 14)
        plt.xlabel('House name', fontsize = 22)
        plt.ylabel('Ghar ki keemte', fontsize = 22)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

Master_bot = SeriesMaster(url)
Master_bot.find_ocean_trend()
Master_bot.lowercase_ocean_text()
Master_bot.plot_ocean_data()
  


#Advanced Methods Ki Nayi Class
import pandas as pd
class AdvanceMethod:
    def __init__(self, file_url):
        print("--Data load ho rah hai--")
        self.df = pd.read_csv(file_url)
        print("data load ho gya hai''''")


    def get_data_summary(self):
        print('\n-----Statistics summary of Dataset----- ')
        print(self.df[['houing_median_age', 'median_house_value']].describe())

    def filter_with_isin(self):
        print("\n---Only targeted areas Island and Near Bay-----")
        area_target = ['ISLAND', 'NEAR BAY']
        targetd_df = self.df[self.df['ocean_proximity'].isin(area_target)]
        print(f"Match hone wale kul gharo ki sankhiya : {len(targetd_df)}")
        print(targetd_df[['ocean_proximity', 'median_house_value']].head(3))


    def filter_with_querry(self):
        print("-----Filtering using querry (Age > 50 & Price < 150000)-----")
        query_df = self.df.query('housing_median_age > 50 and median_house_value < 150000')
        print(f"Puran or saste gharo ki ginti : {len(query_df)}")
        print(query_df[['housing_median_age', 'median_house_value']].head(3))

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

advanced_bot = AdvanceMethod(url)
advanced_bot.filter_with_querry()
advanced_bot.filter_with_isin()
advanced_bot.filter_with_querry()


#Advanced Methods Part-B Ki Nayi Class
import pandas as pd 

class PandasTransformer:
    def __init__(self, file_url):
        print("---Data loa ho rha hai---")
        self.df = pd.read_csv(file_url)
        print("---Data load ho gaya hai---")

    def drop_faulty_columns(self):
        print("---Faltu columns ko draop kar dete hai to easy to read---")
        cleaned_of = self.df.drop(columns=['longitude', 'latitude'])

        print(f"Pegle ka ganda data : {len(self.df.columns)}")
        print(f"Saaf hone ke Baad ka data : {len(cleaned_of.columns)}")
        print("Bache hue columns :", list(cleaned_of.columns))


    def rename_mycolumns(self):
        print("---Naam badlne ke baad ka data kaisa dikhta hai---")
        rename_df = self.df.rename(columns = {
            'housing_median_age': 'house_age',
            'median_house_value' : 'price'
        })

        print(rename_df[['house_age', 'price']].head(3))


    def get_randome_sample(self):
        randome_rows = self.df.sample(n=3)
        print(randome_rows[['ocean_proximity','housing_median_age' ]])

if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

transformer_bot = PandasTransformer(url)
transformer_bot.drop_faulty_columns()
transformer_bot.rename_mycolumns()
transformer_bot.get_randome_sample()

