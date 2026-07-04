#The Range Splitter

import pandas as pd
import numpy as np

gym_data = {
    'Member':['Zaynul', 'Rahul', 'Sana', "Ankit", 'Vikram', 'Sohil'], 
    'Max_Lift_kg':[140, 40, 65, 130, 95, 35]
}

df = pd.DataFrame(gym_data)
print("\033[1m" + "==Original Table=="+ "\033[0m\n")
print(df)


Weight_bins = [0, 50, 100, 200]
group_lables = ['Light Weight', 'Medium Weight', 'Heavy Weight']

df['Weight_Category'] = pd.cut(df['Max_Lift_kg'], bins=Weight_bins, labels=group_lables)

Diet_setup = {
    'Light Weight' : "Protien & Carbs",
    'Medium Weight': "Balance Diet",
    'Heavy Weight': "High Protien & Diet"
}

df['Asigned_Diet'] = df['Weight_Category'].map(Diet_setup)

print("\033[1m" + "===Data Bining & Mapping ke baad Report===" + "\033[0m\n")
print(df)