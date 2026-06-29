import pandas as pd 
import numpy as np

print("\033[1m"+ "===Corporate Employee Performance Analyzer==="+ "\033[0m\n")

company_data = {
    'Emp_Id':[101, 102, 103, 104, 105, 106],
    'Nmae': ['Zaynul', 'Rahul', 'Amit', 'Sana', 'Sohil', 'Varish'],
    'Department':['AI Tech', 'Sales', 'HR', 'Sales', 'HR', 'AI Tech'],
    'Current_salary': [850000, 45000, 60000, 300000, 600000, 700000],
    'Project_completed': [5, 4, None, 2, 5, 3],
    'Review_score':[9.5, 6.4, 4.5, None, 5.4, 8.5]
}

df= pd.DataFrame(company_data)
print("\n==Raw data Recieved==")
print(df)

df['Project_completed'] = df['Project_completed'].fillna(0)

new_rating = df['Review_score'].mean()
df['Review_score'] = df['Review_score'].fillna(new_rating)

condition = (df['Project_completed'] > 3) & (df['Review_score'] > 7.5)
df['Performance_Rating'] = np.where(condition, 'Star_Performance', 'Regular')

df['Bonus'] = np.where(df['Performance_Rating'] == 'Star_Performance',
                       df['Current_salary'] * 0.16,
                       df['Current_salary'] * 0.09)

df['New_Salary'] = df['Current_salary'] + df['Bonus']

dep_salary = df.groupby('Department')['New_Salary'].sum()

print("\033[1m" + "==Cleaned & Processed Employee Data=="+ "\033[0m\n")
print(df)

print("\033[1m" + "==Department-Wise total salary expense=="+ "\033[0m\n")
print(dep_salary)

df.to_csv("Employee_Final_Hike_Report.csv", index=False)
print("\n==REPORT GENERATED! 'Employee_Final_Hike_Report.csv' succesfully saved in your folder.....")