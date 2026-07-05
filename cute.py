import pandas as pd

# Create a sample dataset of employees
data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Neha', 'Vikram', 'Sneha'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'Finance', 'HR'],
    'Salary': [65000, 52000, 72000, 85000, 48000, 56000],
    'Experience_Yrs': [3, 2, 5, 8, 1, 4]
}

df = pd.DataFrame(data)

experienced = df[df['Experience_Yrs'] > 2]

avg_salary_dept = experienced.groupby('Department')['Salary'].mean()

print(avg_salary_dept.sort_values(ascending=False))