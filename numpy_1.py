import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
class AdvanceNumpy:
    def __init__(self, file_url):
        print("===Data load ho rha hai===")
        df = pd.read_csv(file_url)
        print("\n===Data load ho gya hia===")

        self.price = df['median_house_value'].to_numpy() 
        self.age = df['housing_median_age'].to_numpy()
        self.area = df['ocean_proximity'].to_numpy()     

    def process_and_tax(self):
        print("\n===Filtering & Advanced Math using===")
        mask = np.logical_and(self.price < 150000, self.age > 50)
        filterred_price = self.price[mask  ]
        filterred_age = self.age[mask]
        filterred_area = self.area[mask]
        print(f"Saste purane gharo ki ginti ; {len(filterred_price)}")

        price_with_tax = (filterred_price * 1.12)
        price_in_lakh = (price_with_tax / 100000)

        print("\n===Pehle 5 Gharo ka Data===")
        for i in range(5):
            print(f"Ghar {i+1} Age:{filterred_age[i]} , Original Price:{filterred_price[i]} , Taxed Price:{price_in_lakh[i]:.2f} lakh , Area:{filterred_area[i]}")

        top_10_prices = price_in_lakh[:10]
        ghar_numbers = np.arange(1, 11)
        
        plt.figure(figsize=(10, 5))
        plt.bar(ghar_numbers, top_10_prices, color='skyblue', edgecolor='black')
        
        plt.title('Pehle 10 Saste aur Purane Gharo Ka Taxed Price (In Lakhs)', fontsize=14, fontweight='bold')
        plt.xlabel('Ghar Number', fontsize=12)
        plt.ylabel('Price (Lakhs mein)', fontsize=12)
        plt.xticks(ghar_numbers) 
        plt.grid(axis='y', linestyle='--', alpha=0.7) 
        
        plt.show()




if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.csv"

analyzer = AdvanceNumpy(url)
analyzer.process_and_tax()