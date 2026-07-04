#Min-Max Scaling & Filtering

import pandas as pd
import numpy as np
print("\033[1m"+ "===Advanced Numpy Math inside Pandas===" +"033[0m\n")

gym_stats = {
    'Member':['Zaynul', 'Rahul', 'Amit', 'Sana', 'Vikram', 'Sohil'],
    "Max_Lift_Kg":[140, 40, 65, 150, 70, 35]
}
df = pd.DataFrame(gym_stats)
print("===Original Table===")
print(df)

min_val = df['Max_Lift_Kg'].min()
max_val = df['Max_Lift_Kg'].max()

df['Performance_Score'] = (df['Max_Lift_Kg']- min_val) / (max_val - min_val)

cutoff = np.percentile(df['Max_Lift_Kg'], 70)

df['Elite_Status'] = np.where(df['Max_Lift_Kg'] >= cutoff, "Heavy Lister", "Regular")

print("\033[1m" + "===Numpy Scaling & Precentile Ke Baad Data==="+ "\033[0m\n")
print(df)