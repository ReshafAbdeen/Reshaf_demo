import pandas as pd 
import numpy as np

print("\n===Numpy + Pandas Power combo===")
data = {
    "student" : ['Zaynul', 'Rahul', 'Amit', 'Sana', 'Vikram'],
    "Python_score" : [95, 89, 23, 4, 34],
    "Attendence": [90, 58, 29, 34, 85]
}

df = pd.DataFrame(data)
print("\n==Asli Data==")
print(df)

df['Status'] = np.where(df['Python_score'] >= 75, 'Pass', 'Fail')
# condition = 
print("\n==Status ke baad ka Data")
print(df)

condition = (df['Python_score'] > 80) & (df['Attendence'] > 80)
df['Category'] = np.where(condition, 'scholar', 'standard')

df['Detained'] = np.where(df['Attendence'] >= 75, 'No', 'Yes')
print("\n==Final AI filtered Data==")
print(df)