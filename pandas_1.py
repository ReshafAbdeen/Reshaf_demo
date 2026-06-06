import pandas as pd 
class Neural:
    def __init__(self, file_url):
        print("===Data load ho rha hai===")
        self.df = pd.read_csv(file_url)
        print("Data load ho gya hai")

    def Firse_Neural(self):
        
        table1 = self.df.head(10)
        table2 = self.df.tail(12)

        merge_data = pd.merge(table1,table2 , on='ocean_proximity')
        print(merge_data[['ocean_proximity']].head(10))

if __name__=="__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"
nn = Neural(url)
nn.Firse_Neural()