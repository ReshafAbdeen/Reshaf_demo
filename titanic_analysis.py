# Titanic Data Analysis

import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(df.head(100))
print(df['Sex'].value_counts())

print("\n---marne walo ki sankhiya class wise---")
print(df.groupby('Pclass')['Survived'].value_counts())

print("\n--- 🧑‍🤝‍🧑 Class 2 mein Gender ke hisab se kaun bacha aur kaun mara ---")
class_2 = df[df['Pclass'] == 2]
print(class_2.groupby('Sex')['Survived'].value_counts())  


sabse_zyada = df.groupby('Embarked')['Survived'].value_counts()


print("\n---Kis city ke log zyada the---")
print(sabse_zyada)

class_2 = df[df['Pclass'] == 2]
print(class_2.groupby('Sex')['Survived'].value_counts())