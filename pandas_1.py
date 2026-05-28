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