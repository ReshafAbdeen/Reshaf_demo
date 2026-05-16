#MY DAY 29 OF LEARNING PYTHON

import pandas as pd
from tabulate import tabulate

pd.set_option('display.float_format', lambda x: '%.2f' % x)

raw_data = {
    'Emd_ID': [1, 2, 3, 4, 5, 6, 7], 
    'Name': ['Zaynul', 'Shoeb', 'Varish', 'Sohil', 'Farman', 'Faizan', 'Amaan' ],
    'Department': ['IT', 'HR', 'IT', 'SALES', 'HR', 'IT', 'SALES'],
     'Salary': [100000, 90000, None, 70000, 84000, 65000, None ],   
     'Performance_Score': [4.6, 4.3, 3.5, 2.6, 4.0, 4.9, 3.5]
}

df = pd.DataFrame(raw_data)

print("---1. Oringinal Data ( With Missing Value)---")
print(tabulate(df,headers = 'key', tablefmt = 'psql', showindex = False))
print("-" * 40)

avg_salary = df['Salary'].mean()
df['Salary'] = df['Salary'].fillna(avg_salary)

high_performance = df[df['Performance_Score'] > 4.0]

dept_summary = df.groupby('Department').agg({'Salary': 'mean','Performance_Score': 'mean'
})

sorted_df = df.sort_values(by= 'Salary', ascending=False)

print("\n---2. Clean Data ( Missing Salary Filled)")
print(tabulate(df,headers = 'keys', tablefmt = 'pqsl', showindex = False))

print("\n---3. High Performance---")
print(tabulate(high_performance[['Name', 'Department', 'Performance_Score']], headers = 'keys', tablefmt = 'psql', showindex = False))

print("\n---4. Department Wise Summary---")
print(tabulate(dept_summary,headers = 'keys', tablefmt = 'pqsl', showindex = False))

print("\n--5. Employee Sorted By Salary (Highest First)--- ")
print(tabulate(sorted_df,headers = 'keys', tablefmt = 'pqsl', showindex = False))
