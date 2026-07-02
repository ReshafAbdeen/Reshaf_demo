#The Fitness Gym Club Analytics

import pandas as pd 
import numpy as np 

print("\033[1m" + "=== Bareilly Gym Center Advanced Analytics ===" + "\033[0m\n")

gym_data = {
    "Member": ["Zaynul", "Rahul", "Amit", "Sana", "Zaynul", "Rahul", "Amit", "Sana"],
    "Month": ["May", "May", "May", "May", "June", "June", "June", "June"],
    "Workout_Type": ["Weightlifting", "Cardio", "Weightlifting", "Cardio", "Weightlifting", "Cardio", "Cardio", "Weightlifting"],
    "Attendance_Days": [24, 12, 8, 22, 26, None, 18, 20],
    "Fees_Paid": [2000, 1500, 2000, 1500, 2200, 1500, 1500, 2000]
}

df = pd.DataFrame(gym_data)
print("===Raw Gym Data Recieved===")
print(df)


df['Attendance_Days'] = df['Attendance_Days'].fillna(df["Attendance_Days"].mean())
gym_pivot = df.pivot_table(
    values = "Fees_Paid",
    index = 'Month',
    columns = 'Workout_Type',
    aggfunc = 'mean'
)

print("\n===Report Pivot : Month & Workout Wise Total Revenue===")
print(gym_pivot)